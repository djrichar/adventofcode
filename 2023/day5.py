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



seed_info = []
source = 'seed'
destination = 'seed'
with open('day5-input.txt', 'r') as input:
    for line in input.readlines():
        if line.startswith("seeds:"):
            data = line[6:].strip().split()
            data = zip(data[0::2],data[1::2])
            for start, length in data:
                seed_info.append(SeedInfo(int(start), int(length)))
        else:
            match = re.search(r'(\w+)-to-(\w+) map', line)
            if match:
                source = match.group(1)
                destination = match.group(2)
                print("processing: ", line)
                continue
            data = [int(i) for i in line.split()]
            if data:
                for seed in seed_info:
                    seed.apply(source, data[1], destination, data[0], data[-1])
                   
# print(seed_info)
for s in seed_info:
    print(s.seed, min(s.location))

print(min([ l[0] for s in seed_info for l in s.location]))