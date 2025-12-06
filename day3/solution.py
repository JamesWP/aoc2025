import pkgutil
INPUT = pkgutil.get_data('solution', 'input').decode()
EXAMPLE="""987654321111111
811111111111119
234234234234278
818181911112111"""

class Memoize:
    def __init__(self, f):
        self.f = f
        self.memo = {}
    def __call__(self, *args):
        if not args in self.memo:
            self.memo[args] = self.f(*args)
        #Warning: You may wish to do a deepcopy here if returning objects
        return self.memo[args]

def solve(all_bats, num, offset):
    bats = all_bats[offset:]

    # print(head, tail)
    # print(all_bats, num, offset, " := ", bats)

    if len(bats) == num:
        # the best we can do with one option is that option
        return int(bats)

    head = int(bats[0])

    current_best = solve(all_bats, num, offset+1)
    current_best_str = str(current_best)

    # cant compose
    if num == 1:
        if head>current_best:
            return head
        else:
            return current_best

    # can compose
    # print(current_best_str[len(current_best_str)-num], head)

    if int(current_best_str[len(current_best_str)-num]) <= head:
        # print("composing", current_best_str, head)
        # need to check
        our_best = int(str(head) + str(solve(all_bats, num-1, offset+1)))
        if our_best>current_best:
            return our_best
        else:
            return current_best
    
    return current_best

solve = Memoize(solve)

assert solve("12", 2, 0) == 12
assert solve("990", 2, 1) == 90
assert solve("990", 2, 0) == 99
assert solve("123", 2, 0) == 23
assert solve("123456789", 1, 0) == 9
assert solve("9876543210", 1, 0) == 9
assert solve("9876543210", 1, 1) == 8
assert solve("987654321111111", 1, 14) == 1
assert solve("1111", 2, 0) == 11
assert solve("21111", 2, 0) == 21
assert solve("987654321111111", 2, 0) == 98
assert solve("234234234234278", 2, 0) == 78

def part1(inpt):
    tot = 0
    for line in inpt.splitlines():
        # print("solving", line)
        ans = solve(line, 2, 0)
        # print("solving", line, ans)
        tot+=ans
    return tot

def part2(inpt):
    tot = 0
    for line in inpt.splitlines():
        # print("solving", line)
        ans = solve(line, 12, 0)
        # print("solving", line, ans)
        tot+=ans
    return tot

if __name__ == "__main__":
    print()
    assert part1(EXAMPLE) == 357
    assert part2(EXAMPLE) == 3121910778619
    print(part1(INPUT))
    print(part2(INPUT))
