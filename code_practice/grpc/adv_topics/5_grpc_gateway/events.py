from collections import namedtuple
from datetime import datetime, timedelta
from time import sleep

LocationEvent = namedtuple("LocationEvent", "car_id time lat lon")


def rand_events(count):
    time = datetime(2024, 12, 28, 14, 36, 9)
    lat, lon = 51.4871871, -0.1266743
    for _ in range(count):
        yield LocationEvent(
            car_id=7,
            time=time,
            lat=lat,
            lon=lon,
        )

        time += timedelta(seconds=17.3)
        lat += 0.0001
        lon -= 0.0001
        sleep(0.1)
