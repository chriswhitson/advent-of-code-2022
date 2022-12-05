# Part 1
with open('test.txt', 'r') as f:
    moves = ((p1 - ord('A'), p2 - ord('X')) for p1,p2 in (map(ord,game.split()) for game in f))
    print(sum(((3 if p1 == p2 else 6 if p2 == (p1 + 1) % 3 else 0) + (p2 + 1) for p1,p2 in moves)))


# Part 2
with open('test.txt', 'r') as f:
    move_n_outcomes = ((m - ord('A'), o - ord('X')) for m,o in (map(ord,game.split()) for game in f))
    print(sum(((m + o - 1) % 3) + 1 + (o * 3) for m,o in move_n_outcomes))
                
   
