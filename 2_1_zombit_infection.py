def validationCheck(newMove,currentMoves,population):
    try:
        return newMove not in currentMoves and newMove[0] >= 0 and newMove[0] < len(population) and newMove[1] >=0 and newMove[1] < len(population[newMove[0]])
    except IndexError as e:
        pass
    return False
    
def answer(population, x, y, strength):
    movement = []
    movement.append([x,y])
    mX = 1
    while mX <= len(movement):
        try:
            if population[movement[mX-1][0]][movement[mX-1][1]] <= strength:
                population[movement[mX-1][0]][movement[mX-1][1]] = -1
                newMovementLeft = [movement[mX-1][0],movement[mX-1][1]-1]
                if validationCheck(newMovementLeft,movement,population):
                    movement.append(newMovementLeft)
                newMovementUp = [movement[mX-1][0]-1,movement[mX-1][1]]
                if validationCheck(newMovementUp,movement,population):
                    movement.append(newMovementUp)
                newMovementRight = [movement[mX-1][0],movement[mX-1][1]+1]
                if validationCheck(newMovementRight,movement,population):
                    movement.append(newMovementRight)
                newMovementDown = [movement[mX-1][0]+1,movement[mX-1][1]]
                if validationCheck(newMovementDown,movement,population):
                    movement.append(newMovementDown)
        except:
            pass
        mX = mX + 1
    return population

print answer([[1, 2, 3], [2, 3, 4], [3, 2, 1]],0,0,2)
print answer([[6, 7, 2, 7, 6], [6, 3, 1, 4, 7], [0, 2, 4, 1, 10], [8, 1, 1, 4, 9], [8, 7, 4, 9, 9]],2,1,5)
print answer([[6, 7, 2, 1, 2, 2], [6, 3, 1, 4, 7], [0, 2, 1, 10], [8, 1, 1, 4, 9], [8, 7, 4, 9, 9]],2,1,5)
