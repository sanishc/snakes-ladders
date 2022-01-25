
snakes = {31:14, 37:17, 73:53, 78:39, 92:35, 99:7}
ladders = {5:25, 10:29, 22:41, 28:55, 44:95, 70:89, 79:81}

def movePlayer(pos,score):
    newPos = pos + score #updates the user position

    snake = snakes.get(newPos, False) #checks new position has snake
    if snake == False: #if no snake found

        ladder = ladders.get(newPos,False) #checks new position has ladder
        if ladder == False: #if no ladder found

            if newPos == 100: #victory for player
                return newPos #no need to print position
            elif newPos > 100:
                return newPos
            else:
                print("Moved to Position ", newPos)
                return newPos

        else: #if ladder found
            newPos = ladder
            print("Yeh! Climbed With A Ladder To Position ",newPos)
            return newPos

    else: #if snake found
        newPos = snake
        print("OMG! Swallowed By A Snake To Position ",newPos)
        return newPos