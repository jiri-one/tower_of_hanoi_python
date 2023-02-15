from textwrap import dedent

NUMBER_OD_DISKS: int = 3
INITIAL_TOWER: list[int] = list(reversed(range(1, NUMBER_OD_DISKS+1)))

towers: list[list[int], list[int], list[int]] = [INITIAL_TOWER.copy(), [], []]

move_counter: int = 0

def move_disk(t_from: int, t_to: int):
    t_from = towers[t_from]
    t_to = towers[t_to]
    t_to.append(t_from.pop(-1))
    global move_counter
    move_counter += 1
    print("Tower 1:", towers[0])
    print("Tower 2:", towers[1])
    print("Tower 3:", towers[2])
    print(dedent(f"""---------------------------
state after move {move_counter}
---------------------------"""))

# print initial state of towers
print("Tower 1:", towers[0])
print("Tower 2:", towers[1])
print("Tower 3:", towers[2])
print(dedent(f"""---------------------------
Initial towers state
---------------------------"""))

# get tower with smallest disk on the top
for index, tower in enumerate(towers):
    if len(tower) > 0:
        if tower[-1] == 1:
            tower_with_one = index
            break

# cycle
while True:
    # move smallest disk (one)
    if NUMBER_OD_DISKS % 2 == 0:
        new_tower_with_one = (tower_with_one-1)%3
    else:
        new_tower_with_one = (tower_with_one+1)%3
    move_disk(tower_with_one, new_tower_with_one)
    tower_with_one = new_tower_with_one

    # break cycle when disk one is on final position 
    if towers[1] == INITIAL_TOWER:
        break
    
    # move with another disk (it is only one possible move)
    two = [t for t in range(3) if t != new_tower_with_one] # towers without one
    for ti in two: # ti like tower index
        if len(towers[ti]) == 0:
            tower_to = ti
            two.remove(tower_to)
            tower_from = two[0]
            break
    else:
        if towers[two[0]][-1] > towers[two[1]][-1]:
            tower_to = two[0]
            tower_from = two[1]
        else:
            tower_to = two[1]
            tower_from = two[0]
    move_disk(tower_from, tower_to)

# print FINAL state of towers
print("Tower 1:", towers[0])
print("Tower 2:", towers[1])
print("Tower 3:", towers[2])
print(dedent(f"""---------------------------
FINAL towers state
---------------------------"""))

#sorry guys, I wanted to do a little bit of testing in pytest and light automated testing in Github CI, but it's Valentine's Day .... ;-)
