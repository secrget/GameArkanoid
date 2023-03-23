from classes.Brick import Brick

bricks = []

for i in range(50, 200, 30):
    for j in range(50, 700, 70):
        bricks += [Brick([j, i], 50, 20)]