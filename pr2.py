import random
def game():
    score=random.randint(0,100)
    print(f"the score is {score}")
    return score
score=game()
with open("hiscore.txt","r") as f:
    hiscore=int(f.read())
if score>hiscore:
    with open("hiscore.txt","w") as f:
        f.write(str(score))
                