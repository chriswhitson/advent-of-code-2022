import re 

with open('input.txt', 'r') as f:
    rows, moves = f.read().split("\n\n")
    rows = [[line[x:x+3] for x in range(0, len(line), 4)] for line in  rows[:-2].splitlines()[:-1]] 

    stacks = [[row[h].strip(' []') for row in rows if len(row[h].strip())] for h in range(len(rows[0]))]
    moves =(map(int, re.findall('[0-9]+', m)) for m in moves.splitlines())

    for c, f, t in moves:
        stacks[t-1] = stacks[f-1][0:c] + stacks[t-1]
        stacks[f-1] = stacks[f-1][c:]

    print(''.join(p[0] for p in stacks if len(p)))