import random

playerscore = 0
npcscore = 0
def main():
    global playerscore,npcscore
    print("SCORE BOARD")
    print("Your score="+str(playerscore))
    print("NPC's score="+str(npcscore)+"\n\n")
    print("Rock...\nPaper...\nScissors..\n")
    playermove = input("Which one is your choice?\n ")
    playermove=playermove.upper()
    print("Your move="+playermove)
    liste = ["ROCK", "PAPER", "SCISSORS"]
    npcmove = random.choice(liste)
    print("NPC's move="+npcmove)
    if playermove == "ROCK":
        if npcmove == "ROCK":
            print("DRAW")
            if playerscore==3:
                print("YOU WON!")
            elif npcscore==3:
                print("NPC WON!")
            else:
                print("\n")
                main()
            if playerscore==3:
                print("YOU WON!")
            elif npcscore==3:
                print("NPC WON!")
            else:
                print("\n")
                main()
        elif npcmove == "PAPER":
            print("NPC WON THE ROUND")
            npcscore+=1
            if playerscore==3:
                print("YOU WON!")
            elif npcscore==3:
                print("NPC WON!")
            else:
                print("\n")
                main()
        elif npcmove == "SCISSORS":
            print("YOU WON THE ROUND")
            playerscore += 1
            if playerscore==3:
                print("YOU WON!")
            elif npcscore==3:
                print("NPC WON!")
            else:
                print("\n")
                main()
    elif playermove == "PAPER":
        if npcmove == "ROCK":
            print("YOU WON THE ROUND")
            playerscore += 1
            if playerscore==3:
                print("YOU WON!")
            elif npcscore==3:
                print("NPC WON!")
            else:
                print("\n")
                main()
        elif npcmove == "PAPER":
            print("DRAW")
            if playerscore==3:
                print("YOU WON!")
            elif npcscore==3:
                print("NPC WON!")
            else:
                main()
        elif npcmove == "SCISSORS":
            print("NPC WON THE ROUND")
            npcscore += 1
            if playerscore==3:
                print("YOU WON!")
            elif npcscore==3:
                print("NPC WON!")
            else:
                print("\n")
                main()
    elif playermove == "SCISSORS":
        if npcmove == "ROCK":
            print("NPC WON THE ROUND")
            npcscore += 1
            if playerscore==3:
                print("YOU WON!")
            elif npcscore==3:
                print("NPC WON!")
            else:
                print("\n")
                main()
        elif npcmove == "PAPER":
            print("YOU WON THE ROUND")
            playerscore+=1
            if playerscore==3:
                print("YOU WON!")
            elif npcscore==3:
                print("NPC WON!")
            else:
                print("\n")
                main()
        elif npcmove == "SCISSORS":
            print("DRAW")
            if playerscore==3:
                print("YOU WON!")
            elif npcscore==3:
                print("NPC WON!")
            else:
                print("\n")
                main()
    else:
        print("You made a mistake.Please be sure that you entered the correct values.\n\n")
        main()

print("**********************************")
print("       ROCK,PAPER & SCISSORS      ")
print("**********************************\n")
main()