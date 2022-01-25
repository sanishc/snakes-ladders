from . import gameConcept
import datetime
import random

def startGame(plyrCount):

    plyrNames = []
    plyrPos = []
    winners = []
    gameStatus = True

    for i in range(1,plyrCount+1): #store names of each player
        print("Player", end="")
        print(i, end="")
        plyrNames.append(input(" Enter Your Name: ").capitalize())
        plyrPos.append(0)

    while gameStatus:
        for i in plyrNames:  # get dice val for each player
            print(i, end="")
            input(" it's your turn press enter to roll dice")
            dice = random.randint(1, 6)
            print(i,"Got ", dice)

            if dice > 0 and dice < 7:
                # pass current position and dice value to func
                newPos = gameConcept.movePlayer(plyrPos[plyrNames.index(i)], dice)
                if newPos == 100:
                    print("Victory For ", i,"\n")
                    plyrPos.pop(plyrNames.index(i))  # removes player from game
                    winners.append(i)  # add player to winners list
                    plyrNames.pop(plyrNames.index(i))
                elif newPos > 100:
                    print("Opz! Can't Make A Move This Time")
                else:
                    plyrPos[plyrNames.index(i)] = newPos
                    print("")

            else:
                print("Incorrect score only values b/w 0 and 7 are accepted")
        if plyrCount == len(winners):
            gameStatus = False

    print("---------------Game Completed---------------")

    file = open('gameHistory.txt','a')
    file.write("\n")
    file.write("\n")
    file.write(str(datetime.datetime.now())[:-10])
    file.write("\n-----------------\n")
    file.close()
    for i in winners:
        print(winners.index(i) + 1, end="")
        print(".", i)
        file = open('gameHistory.txt', 'a')
        file.write(str(winners.index(i) + 1))
        file.write(".")
        file.write(i)
        file.write(" ")
        file.close()