from concurrent.futures import ThreadPoolExecutor
from time import perf_counter
from uuid import uuid4

import grpc
from grpc_reflection.v1alpha import reflection

import config
import log
import rides_stream_pb2 as pb2
import rides_stream_pb2_grpc as rpc
import validate


def new_ride_id():
    return uuid4().hex


class TimingInterceptor(grpc.ServerInterceptor):
    def intercept_service(self, continuation, handler_call_details):
        start = perf_counter()
        try:
            return continuation(handler_call_details)
        finally:
            duration = perf_counter() - start
            name = handler_call_details.method
            log.info("%s took %.3fsec", name, duration)


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

    def Track(self, request_iterator, context):
        count = 0
        for request in request_iterator:
            # TODO: Store in database
            log.info("track: %s", request)
            count += 1

        return pb2.TrackResponse(count=count)


def load_credentials():
    with open(config.cert_file, "rb") as fp:
        cert = fp.read()

    with open(config.key_file, "rb") as fp:
        key = fp.read()

    return grpc.ssl_server_credentials([(key, cert)])


if __name__ == "__main__":
    import config

    server = grpc.server(
        ThreadPoolExecutor(),
        interceptors=[TimingInterceptor()],
    )
    rpc.add_RidesServicer_to_server(Rides(), server)
    names = (
        pb2.DESCRIPTOR.services_by_name["Rides"].full_name,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(names, server)

    addr = f"[::]:{config.port}"
    credentials = load_credentials()

    server.add_secure_port(addr, credentials)
    server.start()

    log.info("Server ready on %s", addr)
    server.wait_for_termination()
