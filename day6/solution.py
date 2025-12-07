import pkgutil
import bisect
INPUT = pkgutil.get_data('solution', 'input').decode()

EXAMPLE="""123 328  51 64
 45 64  387 23
  6 98  215 314
*   +   *   +  
"""


def part1(inpt):
    lines = inpt.splitlines()

    nums = lines[:-1]
    op = lines[-1]
    nums = [
        [int(a) for a in num.split(" ") if len(a.strip()) != 0]
        for num in nums
    ]
    op = [op for op in op.split(" ") if len(op.strip()) != 0]
    # print(nums, op)
    assert all(len(num) == len(op) for num in nums)

    total = 0
    for bits in zip(*nums,op):
        nums = bits[:-1]
        op = bits[-1]

        if op == '*':
            op = lambda a,b: a*b
        elif op == '+':
            op = lambda a,b: a+b
        else:
            assert False

        result = nums[0]
        for num in nums[1:]:
            result = op(result, num)

        total += result

    return total

def product(nums):

    acc = next(nums)
    for num in nums:
        acc *= num
    return acc

def part2(inpt):
    lines = inpt.splitlines()

    xmax = max((len(line) for line in lines))

    total = 0
    acc = []
    for x in range(xmax):
        x = xmax - x -1

        bits = [
            line[x] if x<len(line) else ' '
            for line in lines
        ]

        if all(b==' ' for b in bits):
            acc = []
            continue
        
        # print(bits)
        nums = [int(num) for num in bits[:-1] if num != ' ']
        # print(nums)
        op = bits[-1]

        num = sum((num*pow(10, len(nums)-i-1) for i,num in enumerate(nums)))
        # print(num)
        acc.append(num)

        if op == '+':
            ans = sum(a for a in acc)
            print('+', acc, ans)
            total += ans
        if op == '*':
            ans = product(a for a in acc)
            print('*', acc, ans)
            total += ans

        # print(num, op)


    return total

if __name__ == "__main__":
    print()
    assert part1(EXAMPLE) == 4277556 
    assert part2(EXAMPLE) == 3263827
    print(part1(INPUT))
    print(part2(INPUT))
