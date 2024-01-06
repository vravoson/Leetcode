class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        road = [0]*1000
        for elem in trips:
            nb_passengers = elem[0]
            from_i, to_i = elem[1], elem[2]
            for i in range(from_i, to_i):
                road[i] += nb_passengers
        return max(road) <= capacity
