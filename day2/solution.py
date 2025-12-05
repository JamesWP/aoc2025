import pkgutil
INPUT = pkgutil.get_data('solution', 'input').decode()
EXAMPLE="""11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"""
def part1(lines):
    lens = {
        x: {
            v for v in range(1, x) if x//v == 2 and any((v*i == x for i in range(x+1)))
        }
        for x in range(1,15)
    }

    # print(lens)

    ranges = [[int(i) for i in range.split('-')] for range in lines.split(',')]

    tot = 0

    for [f, t] in ranges:
        for v in range(f,t+1):
            # print("num", v)
            val = str(v)
            val_len = len(val)
            for l in lens[val_len]:
                pref = val[0:l]
                # print("prefix", pref)
                others = [val[x:x+l] for x in range(l, val_len, l)]
                # print("others", others)
                repeats = all((o == pref for o in others))
                if repeats:
                    # print("repeat!", pref, val)
                    tot += v
    return tot

def part2(lines):
    lens = {
        x: {
            v for v in range(1, x) if x%v==0 and x//v >=2 and any((v*i == x for i in range(x+1)))
        }
        for x in range(1,15)
    }

    # print(lens)

    ranges = [[int(i) for i in range.split('-')] for range in lines.split(',')]

    tot = 0

    for [f, t] in ranges:
        for v in range(f,t+1):
            # print("num", v)
            val = str(v)
            val_len = len(val)
            for l in lens[val_len]:
                pref = val[0:l]
                # print("prefix", pref)
                others = [val[x:x+l] for x in range(l, val_len, l)]
                # print("others", others)
                repeats = all((o == pref for o in others))
                if repeats:
                    # print("repeat!", pref, val)
                    tot += v
                    break
    return tot
if __name__ == '__main__':
    assert part1(EXAMPLE) == 1227775554
    print(part1(INPUT))
    print(part2(EXAMPLE))
    assert part2(EXAMPLE) == 4174379265
    print(part2(INPUT))
