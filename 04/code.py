with open('input.txt', 'r') as f:
    assignments = [list(map(lambda x : list(map(int, x.split('-'))), r.strip().split(','))) for r in f]

    # Part 1
    print(sum(1 for i in assignments if [min(i[0][0],i[1][0]), max(i[0][1],i[1][1])] in i))

    # Part 2
    print(sum(1 for i in assignments if max(i[0][0],i[1][0]) <= min(i[0][1],i[1][1])))
