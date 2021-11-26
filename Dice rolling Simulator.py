""" Dice rolling Simulator """
import random
def randomizer():
    return random.randint(1,6)
    
def Dice_rolling():
    print("\nRolling the Dice")
    print(randomizer())
    print(randomizer())

def main_simulator():
    print("\nDo you want to play Dice rolling")
    ans= input(":").lower().strip()
    if ans == "yes" or ans=="y":
        willing = "yes"
        while willing == "yes" or willing == "y":
            Dice_rolling()
            willing = input("\nDo you want to continue playing:").lower().strip()        
        print("\nHow was the game please rate us ******")    
    else:
        print("\nYou don't know how to have fun")
        
main_simulator()

 
