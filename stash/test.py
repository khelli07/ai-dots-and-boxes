import re


def sanitize_line(string):
    string = re.sub(r"[.[\]]", "", string.strip())
    return string


f = reversed(open("./configs/config2.txt", "r").readlines())
f = list(f)
is_player = f[0].strip() == "1"
array = [[] for _ in range(3)]
moves = []

ctr, i = 0, 0
for line in f[1:]:
    if ctr <= 9:
        i = i + 1 if ((ctr + 1) % 4 == 0) else i
        ln = sanitize_line(line)
        array[i].append([int(num) for num in ln.split()])
    else:
        player, type_, x, y = line.split()
        player = player == "1"
        x, y = int(x), int(y)
        moves.append((player, type_, x, y))

    ctr += 1

print(array)
print(moves)
