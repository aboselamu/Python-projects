""" Guess number Game  """
import random 
def takeInput():
    return  input("Enter your number: \n")
def randomFun():
    for i in range(3):
        var = random.choice([0,1,2])
        Num = int(takeInput())
        if Num == var:
            print("wow you win!!!!!"+ "G\n\n\n\n" +"/*\_/*\_/*\\t\t\t"+"\_/\_/")
            break
        else:
            print("You lost sucker")
print("I bet you can't Guess the number\nYou have 3 chances to win this game\n ")
randomFun()