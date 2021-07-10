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
    for x in live:
        if __neighbor_count(*x) == 2 or __neighbor_count(*x) == 3:
            newlive.add(x)
            ...
    for x in dead:
        if __neighbor_count(*x, add_to_dead=False) == 3:
            newlive.add(x)
    live = newlive

if __name__ == "__main__":
    print("This isn't the main file... why are you running this?")
    ...