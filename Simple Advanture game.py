""" Text based Adventure game """
print("Wellcome to Adventure game... Now you in a situation to must choose one")
print("\nPlease press 1 to Start \n")
start = input(":").lower().strip()
if start == "1":
    print("Red pill or Blue pill")
    v1 = input(":").lower().strip()
    if v1 == "red":
        print("\nwellcome to hell, do you want to get out")
        v11 = input(":").lower().strip()
        if v11 == "yes":
            print("\nkill someone from around you?")
            v111= input(":").lower().strip()
            if v111 == "yes":
                print("\nWell done you are out of hell for now but you will comeback for killing a human")
            else:
                print("\nWell enjo hell")
        else:
            print("Well enjoy Hell")
    elif v1 == "blue":
        print("\ndo you want to go heaven?")
        v12 = input(":").lower().strip()
        if v12 == "yes":
            print("\nwill you give away everything you have?")
            v122 = input(":").lower().strip()
            if v122 == "yes":
                print("wellvthere is no heaven, you are played, goodby")
            else:
                print("there is no place for you in heaven, so goodby")
        elif v12 == "no":
            print("seriously?, heaven is a good place to go, you're a looser, goodby")
        else:
            print("you entered wrong answer")
    else:
        print("you entered the wrong pill, goodby")
else:
    print("goodby you are not for adventure")