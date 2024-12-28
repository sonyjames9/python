import grpc

import log
import rides_ser_pb2 as pb2
import rides_ser_pb2_grpc as rpc
from datetime import datetime


class ClientError(Exception):
    pass


class Client:
    def __init__(self, addr):
        self.channel = grpc.insecure_channel(addr)
        self.stub = rpc.RidesStub(self.channel)
        log.info("connected to %s", addr)

    def close(self):
        self.channel.close()

    def ride_start(self, car_id, driver_id, passenger_ids, type, lat, lon, time):
        request = pb2.StartRequest(
            car_id=car_id,
            driver_id=driver_id,
            passenger_ids=passenger_ids,
            type=pb2.POOL if type == "POOL" else pb2.REGULAR,
            location=pb2.Location(lat=lat, lon=lon),
        )
        request.time.FromDatetime(time)
        log.info("ride started: %s", request)
        try:
            response = self.stub.Start(request, timeout=3)
        except grpc.RpcError as err:
            log.error("start: %s (%s)", err, err.__class__.__mro__)
            raise ClientError(f"{err.code()}: {err.details()}") from err

        # response = self.stub.Start(request)
        return response.id


if __name__ == "__main__":
    import config

    addr = f"{config.host}:{config.port}"
    client = Client(addr)
    client.ride_start(
        car_id=7,
        driver_id="Bond",
        passenger_ids=["M", "Q"],
        type="POOL",
        lat=51.9791,
        lon=91.1092,
        time=datetime(2024, 12, 27, 16, 25, 56),
    )
