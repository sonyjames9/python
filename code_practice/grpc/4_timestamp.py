from datetime import datetime
import rides_pb2 as pb

loc = pb.Location(
    lat=32.5270941,
    lon=34.9404309,
)

print(loc)

print(pb.POOL)
print(pb.RideType.Name(pb.POOL))
print(pb.RideType.Value("REGULAR"), end="\n\n")

request = pb.StartRequest(
    car_id=95,
    driver_id="McQueen",
    passenger_ids=["p1", "p2", "p3"],
    type=pb.POOL,
    location=pb.Location(
        lat=32.5270941,
        lon=34.9404309,
    ),
)
print(request)

# FromDatetime
time = datetime(2024, 12, 27, 22, 25, 55)
request.time.FromDatetime(time)
print("Request with timestamp : \n", request)

# ToDatetime
time2 = request.time.ToDatetime()
print("Time type, Time:", type(time2), time2)

# time now
from google.protobuf.timestamp_pb2 import Timestamp

now = Timestamp()
now.GetCurrentTime()
print("Time Now:", now)
