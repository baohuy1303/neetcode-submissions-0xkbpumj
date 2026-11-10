class UndergroundSystem:
    def __init__(self):
        self.active = {} # id -> (name, time_Start)
        self.routes = {} # (start_station, end_station) -> total_time, count_of_rides

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.active[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, start_time = self.active.pop(id)

        key = (start_station, stationName)
        
        total, count = self.routes.get(key, (0, 0))
        self.routes[key] = (total + t - start_time, count + 1) 

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total, count = self.routes[(startStation, endStation)]

        return total/count