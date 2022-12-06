with open('input.txt', 'r') as f:
    db = f.read().strip()
    chunks = ((i+14,db[i:i+14]) for i in range(0, len(db)))
    for c in chunks:
        if len(set(c[1])) == 14:
            print(c[0])
            break