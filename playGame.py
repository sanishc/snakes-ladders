from GameData import multiPlayer
from GameData import singlePlayer

cont = True

while cont:
    menu = int(input("\n1.Play Game 2.View History: "))
    if menu == 1:
        plyr = int(input("\n1.SinglePlayer 2.Multiplayer: "))
        if plyr == 1:
            singlePlayer.startGame()
        elif plyr == 2:
            plyrCount = int(input("\nEnter No.of Players: "))
            multiPlayer.startGame(plyrCount)
        else:
            print("\nInvalid Option! Run Game Again.")

    elif menu == 2:
        file = open('gameHistory.txt', 'r')
        hist = file.readlines()
        file.close()
        for i in hist:
            print(i,end="")
        print("")

    else:
        print("Invalid Choice")

    ch = input("\nPlay Again (y/n): ")
    if ch == 'y' or ch == "Y":
        pass
    else:
        cont = False
