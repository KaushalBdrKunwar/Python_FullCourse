#2.The game() function in a program lets a user play a game and returns the 
#score as an integer. You need to read a file 'Hi-score.txt' which is either
#blank or contains the previous Hi-score. You need to write a program to update
#the Hi-score whenever the game() function breaks the Hi-score.

import random

def game():
    print("You are playing the game..")
    score = random.randint(1,62)
    #Fetch the hiscore
    with open(r"C:\Users\legion\Desktop\PythonFullCourse\Chapter9\hiscore.txt") as f:
            hiscore = f.read()
            if(hiscore!=""):
                hiscore = int(hiscore)
            else:
                 hiscore = 0

    print(f"Your score: {score}")
    if(score>hiscore or hiscore ==""):
        #write this hiscore to file
        with open(r"C:\Users\legion\Desktop\PythonFullCourse\Chapter9\hiscore.txt","w") as f:
             f.write(str(score))

    return hiscore

game()
print(f"high score is: {game()}")
