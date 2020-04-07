# Linear System Solver Developed By Thanasis Mitragkas
import time


def solver(a, b, c, a2, b2, c2):  # Finds the solution of the system
    def formatNumber(num):
        if num % 1 == 0:
            return int(num)
        else:
            return num

    D = (a * b2) - (b * a2)
    Dx = (c * b2) - (b * c2)
    Dy = (a * c2) - (c * a2)
    if D == 0:
        x = "Αόριστη η Αδύνατη"
        y = ""
        return x, y
    x = Dx / D
    y = Dy / D
    return formatNumber(x), formatNumber(y)


def inputs():  # Collects inputs from users and returns it
    try:
        def formatNumber(num):  # Remove .0 from intengers
            if num % 1 == 0:
                return int(num)
            else:
                return num

        a, b, c = map(float, input("Value for A,B,Γ ").split())
        a2, b2, c2 = map(float, input("Value for Α₂,B₂,Γ₂ ").split())
        unknown1 = input("Variable name for the first unknown: ")
        unknown2 = input("Variable name for the second unknown: ")
        return formatNumber(a), formatNumber(b), formatNumber(c), formatNumber(a2), formatNumber(b2), formatNumber(
            c2), unknown1, unknown2
    except ValueError:
        pass


def system_maker(a, b, c, a2, b2, c2, unknown1, unknown2):  # Makes (Graphically) the system
    b_string = str(b)
    b2_string = str(b2)
    if "-" not in str(b):
        b_string = ('+' + str(b))
    if "-" not in str(b2):
        b2_string = ('+' + str(b2))
    systems = f'''{str(a)}{unknown1}{str(b_string)}{unknown2} = {str(c)}   
{str(a2)}{unknown1}{str(b2_string)}{unknown2} = {str(c2)} '''  # Construct the system
    print(systems)


repeat = True

while repeat:
    try:
        glbl_a, glbl_b, glbl_c, glbl_a2, glbl_b2, glbl_c2, glbl_unknown1, glbl_unknown2 = inputs()  # Global values (glbl : global)
        system_maker(glbl_a, glbl_b, glbl_c, glbl_a2, glbl_b2, glbl_c2, glbl_unknown1, glbl_unknown2)
        system_correct = input("Is that the system you entered?(y/n) ")  # Checks if system was made correctly
        if system_correct.lower() == "y":
            x, y = solver(glbl_a, glbl_b, glbl_c, glbl_a2, glbl_b2, glbl_c2)
            print(f"The solution is: Α({x},{y})")
            while True:
                cont = input("Do you want to retry(y/n)?  ")
                if cont.lower() == "y":
                    break
                elif cont.lower() == "n":
                    print("GoodBye!")
                    repeat = False
                    break
                else:
                    print("Oops! The answer you entered is invalid. Please try again!")
                    time.sleep(20)
                    continue

        elif system_correct.lower() == "n":
            print("Restarting.....")
            time.sleep(5)
            continue
        else:
            print("Oops! The answer you entered is invalid. Please try again!")
            time.sleep(5)
            continue
    except TypeError:  # Except when user inputs a str instead of a float
        print("Oops!  The numbers you entered are invalid. Please try again!")
        continue
