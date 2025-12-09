import pkgutil
INPUT = pkgutil.get_data('solution', 'input').decode()

EXAMPLE=""".......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............
"""

def solve(inpt):
    lines = inpt.splitlines()

    lines = iter(lines)

    starting = next(lines)

    current = [1 if c=='S' else 0 for c in starting ]

    def fold(current_split_count, current, line):
        vals = [c if l == '.' else 0 for l, c in zip(line,current)]
        splits = 0
        for i in range(len(line)):
            if line[i] != '^':
                continue
            v = current[i]
            if v>0:
                splits += 1
            
            if (i-1)>=0 and line[i-1] == '.':
                vals[i-1] += v 

            if (i+1)<len(vals) and line[i+1] == '.':
                vals[i+1] += v

        return vals, current_split_count + splits

    current_split_count = 0
    for line in lines:
        (current, current_split_count) = fold(current_split_count, current, line)
        print(''.join('|' if c>0 else '.' for c in current))
    
    return current, current_split_count

def part1(inpt):
    return solve(inpt)[1]

def part2(inpt):
    return sum(solve(inpt)[0])

if __name__ == "__main__":
    print()
    assert part1(EXAMPLE) == 21
    assert part2(EXAMPLE) == 40
    print(part1(INPUT))
    print(part2(INPUT))
