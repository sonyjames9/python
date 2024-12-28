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

# marshal data/serialization
data = request.SerializeToString()
print("type:", type(data))
print("size:", len(data), end="\n\n")


# Unmarshal data/serialization
request2 = pb.StartRequest()
request2.ParseFromString(data)
print(request2)

print("lat:", request.location.lat)
print("lon:", request.location.lon)
