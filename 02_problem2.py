import random
 
def game():
    print("you are playing the game ..")
    score  = random.randint(2 , 89)

    #fetch the Hiscore
    with open("Hiscore.txt") as f:
        Hiscore = f.read()
        if(Hiscore!=""):
            Hiscore = int(Hiscore)
        else:
            Hiscore = 0


    print(f"your score: {score}")
    if(score>Hiscore ):
        #write this his score to the file
     with open("Hiscore.txt", "w") as f:
        f.write(str(score))

    


    return score


game()
 