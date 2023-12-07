import re

class SeedInfo:
    def __init__(self, start, length):
        self.seed = [(start, start + length-1)]

    def apply(self, source_type, source_start, dest_type, dest_start, length) -> bool:
        if(not hasattr(self, dest_type)):
            self.__setattr__(dest_type, [(s[0],s[1]) for s in self.__getattribute__(source_type)])
        source_end = source_start+length-1
        dest_end = dest_start+length-1
        dest_value = self.__getattribute__(dest_type)
        updated_value = []
        print("apply", self.seed, dest_value, source_type, (source_start, source_end), dest_type, (dest_start, dest_end), length)
        for v in dest_value:
            if len(v) == 3:
                updated_value.append(v)
            ## range is inbetween
            elif v[0] < source_start <= source_end < v[1]:
                updated_value.append((v[0],source_start-1))
                updated_value.append((dest_start, dest_end, 'M'))
                updated_value.append((source_end+1, v[1]))
                print("between value")
            ## range is inbetween source
            elif source_start <= v[0] <= v[1] <= source_end:
                start = dest_start + (v[0] - source_start)
                end = dest_end - (source_end - v[1])
                updated_value.append((start,end, "M"))
                print("between source")
            ## start of range is in source range
            elif source_start < v[0] <= source_end <= v[1]:
                start = dest_start + (v[0] - source_start)
                end = dest_end
                updated_value.append((start, end, "M"))
                if v[1] < source_end:
                    updated_value.append((source_end+1, v[1]))
                print("source start")
            ## end of range is in source range
            elif v[0] < source_start <= v[1] <= source_end:
                updated_value.append((v[0], source_start-1))
                end = dest_end
                if v[1] < source_end:
                    end = dest_end - (source_end - v[1])
                updated_value.append((dest_start, end, "M"))
                print("source end")
            else:
                updated_value.append(v)
        if dest_value != updated_value:
            print("update:", len(dest_value), "to", len(updated_value), updated_value[:4])
        self.__setattr__(dest_type, updated_value)
        
    def __repr__(self) -> str:
        value = "{"
        for a in self.__dict__.keys():
            if not a.startswith('__'):
                value += "\t" +a + "=" + str(self.__getattribute__(a)) + "\n"
        return value + "}\n"


def find_looser(dist, time, highside=False):
    low = 0
    high = time
    mid = 0
 
    while low <= high:
        mid = (high + low) // 2
        mid_dist = mid * (time - mid)
        high_dist = (mid-1) * (time-(mid-1))
        low_dist = (mid+1) * (time-(mid+1))
        print("find(",low,mid,high,")", dist, low_dist, mid_dist, high_dist)

        if mid_dist < dist:
            if (high_dist >= dist or low_dist >= dist):
                print("found", mid, "for find(",low,mid,high,")", dist, low_dist, mid_dist, high_dist)
                return mid
            next_low = mid + 1 if not highside else low
            next_high = mid + 1 if highside else high
        elif mid_dist >= dist and low_dist < dist:
            print("found", mid+1, "for find(",low,mid,high,")", dist, low_dist, mid_dist, high_dist)
            return mid+1
        elif mid_dist >= dist and high_dist < dist:
            print("found", mid-1, "for find(",low,mid,high,")", dist, low_dist, mid_dist, high_dist)
            return mid-1
        else:            
            next_low = mid + 1 if highside else low
            next_high = mid + 1 if not highside else high
        ## catch infinite loop error
        if(next_low == low and next_high == high):
            # looser = None
            # if highside:
            #     if low_dist < dist:
            #         looser = low
            #     elif mid_dist < dist:
            #         looser = mid
            #     else:
            #         looser = high
            # else:
            #     if high_dist < dist:
            #         looser = high
            #     elif mid_dist < dist:
            #         looser = mid
            #     else:
            #         looser = low
            print("ERROR found", looser, "for find(",low,mid,high,")", dist, low_dist, mid_dist, high_dist)
            return mid
        else:
            low = next_low
            high = next_high
    # If we reach here, then the element was not present
    return -1

def collect_winner_range(time, distance) -> list:
    low_looser=find_looser(distance, time)
    high_looser=find_looser(distance, time, True)
    winner_range =  (low_looser+1, high_looser-1)
    print("winners:", winner_range,"for distance:",distance, "and time:", time)
    return winner_range

winners = []
times = []
distances = []
with open('day6-input.txt', 'r') as input:
    for line in input.readlines():
        print(line)
        if line.startswith("Time:"):
            times = [int(i.strip()) for i in line[6:].strip().split()]
        if line.startswith("Distance:"):
            distances = [int(i.strip()) for i in line[9:].strip().split()]

for i, time in enumerate(times):
    print(time, distances[i])
    winners.append(collect_winner_range(time, distances[i]))
print(winners)

winner2 = None
time = int("".join([str(t) for t in times]))
distance = int("".join([str(d) for d in distances]))
winner2 = collect_winner_range(time, distance)

value = 1
for w in winners:
    value *= ((w[1]+1)-w[0])
print(value)
print((winner2[1]+1)-winner2[0])
