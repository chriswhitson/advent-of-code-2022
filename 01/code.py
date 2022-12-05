with open('test.txt', 'r') as f:
    print(sum(sorted(sum(map(int, elf.split())) for elf in f.read().split("\n\n"))[-3:]))
    