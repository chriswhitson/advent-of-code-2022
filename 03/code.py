def priority(c: str):
    return ord(c) - (ord('a') - 1 if c.islower() else ord('A') - 27)

# Part 1
with open('input.txt', 'r') as f:
    items = (set(a).intersection(b).pop() for a,b in ((r[:len(r)//2], r[len(r)//2:]) for r in f))
    print(sum(map(priority,items)))

#  Part 2
with open('input.txt', 'r') as f:
    bags = f.read().splitlines()
    groups = (list(map(set,bags[i:i+3])) for i in range(0,len(bags),3))
    items = (g[0].intersection(g[1],g[2]).pop() for g in groups)
    print(sum(map(priority,items)))




