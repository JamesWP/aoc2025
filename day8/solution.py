from collections import defaultdict
import pkgutil
INPUT = pkgutil.get_data('solution', 'input').decode()

EXAMPLE="""162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689
"""

def product(nums):

    acc = next(nums)
    for num in nums:
        acc *= num
    return acc

def parse(inpt):
    lines = inpt.splitlines()
    junctions = [[int(i) for i in line.split(",")] for line in lines]

    dist = {}
    for i in range(len(junctions)):
        for j in range(len(junctions)):
            if i == j:
                continue
            x = junctions[i][0] - junctions[j][0]
            y = junctions[i][1] - junctions[j][1]
            z = junctions[i][2] - junctions[j][2]
            x *= x
            y *= y
            z *= z
            distance = x+y+z
            dist[(i,j)] = distance
            dist[(j,i)] = distance

    sorted_js = [(i,j) for i in range(len(junctions)) for j in range(len(junctions)) if i != j]
    sorted_js.sort(key=lambda x: dist[x])

    return sorted_js, junctions

def solve(sorted_js, junctions, iter):
    connected = {}
    circuit = {}

    for i in range(len(junctions)):
        connected[i] = set()
        circuit[i] = i 

    count = 0
    for l, link in enumerate(sorted_js):
        (i,j) = link

        if j in connected[i]:
            continue

        # print(a,b)
        connected[i].add(j)
        connected[j].add(i)

        # find root of both tree's
        while i != circuit[i]:
            i = circuit[i]

        while j != circuit[j]:
            j = circuit[j]

        (i,j) = (min(i,j), max(i,j))

        circuit[j] = i

        count+=1
        if count==iter:
            break

    (i,j) = sorted_js[l]
    # print(junctions[i], junctions[j])
    
    count = defaultdict(int)

    for i in range(len(junctions)):
        while circuit[i] != i:
            i = circuit[i]
        count[i] += 1
    
    circuits=list(count.values())
    circuits.sort(reverse=True)

    return circuits, l

def part1(inpt, iter):
    (sorted_js, junctions) = parse(inpt)
    circuits, l = solve(sorted_js, junctions, iter)
    # print(circuits)
    return product(circuits[x] for x in range(3)) 

def part2(inpt):
    (sorted_js, junctions) = parse(inpt)
    print("no juncts", len(junctions))

    # for i in range(1, len(sorted_js)):
    #     circuits = solve(sorted_js, junctions, i)
    #     print(i,len(circuits), circuits[:10])
    #     if circuits == [len(junctions)]:
    #         break

    (lb, ub) = (1, len(sorted_js))
    print(lb,ub)
    while lb<ub:
        m = (ub-lb)//2 + lb

        circuits, l = solve(sorted_js, junctions, m)
        # print(lb, ub, m,len(circuits), circuits[:10])

        if len(circuits) > 1:
            lb = m+1
        else:
            ub = m
            
    circuits, l = solve(sorted_js, junctions, lb)
    print("final", lb, l, sorted_js[l], junctions[sorted_js[l][0]][0], junctions[sorted_js[l][1]][0])
    x,y = junctions[sorted_js[l][0]][0], junctions[sorted_js[l][1]][0]

    return x*y

if __name__ == "__main__":
    print()
    assert part1(EXAMPLE, 10) == 40
    assert part2(EXAMPLE) == 25272
    print(part1(INPUT,1000))
    print(part2(INPUT))
