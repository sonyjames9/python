from concurrent.futures import ThreadPoolExecutor
from uuid import uuid4

import grpc
from grpc_reflection.v1alpha import reflection

import log
import rides_ser_pb2 as pb2
import rides_ser_pb2_grpc as rpc
import validate
import time


def new_ride_id():
    return uuid4().hex


class Rides(rpc.RidesServicer):
    def Start(self, request, context):
        log.info("ride : %r", request)

        try:
            validate.start_request(request)
        except validate.Error as err:
            log.error("bad request: %r", err)
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details(f"{err.field} is {err.reason}")
            raise err

        ride_id = new_ride_id()
        return pb2.StartResponse(id=ride_id)


if __name__ == "__main__":
    import config

    server = grpc.server(ThreadPoolExecutor())
    rpc.add_RidesServicer_to_server(Rides(), server)
    names = (
        pb2.DESCRIPTOR.services_by_name["Rides"].full_name,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(names, server)

    addr = f"[::]:{config.port}"
    server.add_insecure_port(addr)
    server.start()
    server.wait_for_termination(10)
    # time.sleep(5)

    log.info("Server ready on %s", addr)
    server.wait_for_termination()
