
live: set[tuple] = set()
dead: set[tuple] = set()

width, height = int(), int()

def __neighbor_count(x: int, y: int, add_to_dead = True):
    live_count = 0
    for i in range(-1, 2):
        new_y = (y + i + height) % height
        for j in range(-1, 2):
            if not (i == 0 and j == 0):
                new_x = (x + j + width) % width
                if (new_x, new_y) in live:
                    live_count += 1
                elif add_to_dead == True:
                    dead.add((new_x, new_y))
    return live_count
    
def update():
    newlive = set()
    global live
    global dead
    for x in live:
        if __neighbor_count(*x) == 2 or __neighbor_count(*x) == 3:
            newlive.add(x)
    for x in dead:
        if __neighbor_count(*x, add_to_dead=False) == 3:
            newlive.add(x)
    dead = set()
    live = newlive

import re
def rle(string: str):
    g = re.findall(r"\d*b|\d*o|\d*\$", string)
    res: set[tuple] = set()
    x, y = 0, 0

    for sect in g:
        tag = re.search("b|o|\$", sect).string
        number = int(re.search("\d+", sect).group(0)) if re.search("\d+", sect) else 1

        if "b" in sect:
            x += number
        elif "o" in sect:
            for _ in range(number):
                res.add((x, y))
                x += 1
        elif "$" in sect:
            x = 0
            y += number
    return res


if __name__ == "__main__":
    print(rle("bo$2bo$3o"))
    ...