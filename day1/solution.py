import pkgutil
INPUT = pkgutil.get_data('solution', 'input')

EXAMPLE="""L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""

"""
* The dial starts by pointing at `50`.
* The dial is rotated `L68` to point at `82`; during this rotation, it points at `0` *once*.
* The dial is rotated `L30` to point at `52`.
* The dial is rotated `R48` to point at `*0*`.
* The dial is rotated `L5` to point at `95`.
* The dial is rotated `R60` to point at `55`; during this rotation, it points at `0` *once*.
* The dial is rotated `L55` to point at `*0*`.
* The dial is rotated `L1` to point at `99`.
* The dial is rotated `L99` to point at `*0*`.
* The dial is rotated `R14` to point at `14`.
* The dial is rotated `L82` to point at `32`; during this rotation, it points at `0` *once*.
"""

def process(start, move) -> (int,int):
    if move < 0:
        (end, count) = process((100-start)%100, -move)
        return ((100-end)%100, count)

    assert start>=0 and start <=99

    count = (start+move) // 100
    end = (start+move)%100

    return (end, count)
assert process(52, 48) == (0,1)
assert process(95, 60) == (55,1)
assert process(50,1000) == (50, 10)
assert process(55, -55) == (0,1)

def part2(file):
    location = 50
    count = 0
    for line in file.splitlines():
        if line[0] == "R":
            move = int(line[1:])
        else:
            move = -int(line[1:])
        (location, score) = process(location, move)
        count += score
    return count

assert part2(EXAMPLE) == 6
print(part2(INPUT))
