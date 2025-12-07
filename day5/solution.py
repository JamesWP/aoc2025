import pkgutil
import bisect
INPUT = pkgutil.get_data('solution', 'input').decode()

EXAMPLE="""3-5
10-14
16-20
12-18

1
5
8
11
17
32
"""

class Fresh:
    def __init__(self):
        self.ranges = []

    def add(self, s, e):
        if not self.ranges:
            self.ranges.append((s,e))
            return
        
        (ls, le) = self.ranges[-1]
        # print("append", s,e, ls, le)
        if s <= le: 
            self.ranges[-1] = (ls, max(le, e))
        else:
            self.ranges.append((s,e))

    def __contains__(self, item):
        idx = -1 + bisect.bisect(self.ranges, item, key=lambda i:i[0])
        # print("contains", item, idx, self.ranges)
        if idx >= len(self.ranges):
            return False

        # print("contains", item, idx, self.ranges[idx])
        (s,e) = self.ranges[idx]
        return s <= item <= e
    
    def __repr__(self):
        return str(self.ranges)
    
    def check(self):
        le = None
        for range in self.ranges:
            assert range[0] < range[1] and le == None or range[0] > le
            le = range[1]

def part1(inpt):
    (first, second) = inpt.split("\n\n")
    (first, second) = (first.splitlines(), second.splitlines())

    first = [(int(f.split("-")[0]), int(f.split("-")[1])) for f in first ]
    first.sort()

    # print(first[0])
    # print(first[-1])

    fresh = Fresh()

    for (s,e) in first:
        fresh.add(s,e)

    fresh.check()

    # print(fresh)


    count = 0
    for item in second:
        if int(item) in fresh:
            # print(item)
            count +=1 

    return count 

fresh = Fresh()
fresh.add(3,4)
fresh.add(4,5)
fresh.add(10,14)
fresh.add(16,20)
fresh.add(17,20)
assert 3 in fresh
assert 5 in fresh
assert 6 not in fresh
assert 14 in fresh
assert 17 in fresh
assert 100 not in fresh
assert 0 not in fresh

def part2(inpt):
    return 0

if __name__ == "__main__":
    print()
    assert part1(EXAMPLE) == 3
    assert part2(EXAMPLE) == 0
    print(part1(INPUT))
    print(part2(INPUT))
