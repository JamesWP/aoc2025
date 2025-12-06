import pkgutil
INPUT = pkgutil.get_data('solution', 'input').decode()

EXAMPLE="""..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
"""

def neighbors(x,y):
    yield (x-1,y)
    yield (x+1,y)
    yield (x-1,y-1) 
    yield (x,y-1) 
    yield (x+1,y-1) 
    yield (x-1,y+1) 
    yield (x,y+1) 
    yield (x+1,y+1) 

assert len(list(neighbors(0,0))) == 8

def part1(inpt):
    lines = inpt.splitlines()

    rolls = { (x,y) for y, line in enumerate(lines) for x, c in enumerate(line) if c == '@' }
    count = 0
    for (x,y) in rolls:
        roll_neighbors = { (nx,ny) for (nx,ny) in neighbors(x,y) if (nx,ny) in rolls }
        num_neighbours = len(roll_neighbors)
        if num_neighbours < 4:
            count+=1

    # print(rolls)

    return count

def part2(inpt):
    lines = inpt.splitlines()

    rolls = { (x,y) for y, line in enumerate(lines) for x, c in enumerate(line) if c == '@' }
    count = 0
    while rolls:
        accessable = set()
        for (x,y) in rolls:
            ns = set()
            for (nx,ny) in neighbors(x,y):
                if (nx,ny) in rolls:
                    ns.add((nx,ny))
            if len(ns) < 4:
                accessable.add((x,y))

        # print(len(accessable))
        count += len(accessable)

        for x in accessable:
            rolls.remove(x) 

        if len(accessable) == 0:
            break

    return count

if __name__ == "__main__":
    print()
    assert part1(EXAMPLE) == 13
    assert part2(EXAMPLE) == 43
    print(part1(INPUT))
    print(part2(INPUT))
