import rides_pb2 as pb

print(pb.POOL)
print(pb.RideType.Name(pb.POOL))
print(pb.RideType.Value("REGULAR"), end="\n\n")

request = pb.StartRequest(
    car_id=95,
    driver_id="McQueen",
    passenger_ids=["p1", "p2", "p3"],
    type=pb.POOL,
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
