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
        x = "Not Defined or Impossible"
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
    string_a = "" if a == 1 else str(a)
    string_b = "" if b == 1 else str(b)
    string_a2 = "" if a == 1 else str(a2)
    string_b2 = "" if a == 1 else str(b2)
    if "-" not in string_b:
        string_b = ('+' + string_b)
    if "-" not in string_b2:
        string_b2 = ('+' + string_b2)
    systems = f'''{string_a}{unknown1}{string_b}{unknown2} = {str(c)}   
{string_a2}{unknown1}{string_b2}{unknown2} = {str(c2)} '''  # Construct the system
    print(systems)


repeat = True

while repeat:
    try:
        # Global values (glbl : global)
        glbl_a, glbl_b, glbl_c, glbl_a2, glbl_b2, glbl_c2, glbl_unknown1, glbl_unknown2 = inputs()
        system_maker(glbl_a, glbl_b, glbl_c, glbl_a2, glbl_b2,
                     glbl_c2, glbl_unknown1, glbl_unknown2)
        # Checks if system was made correctly
        system_correct = input("Is that the system you entered?(y/n) ")
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
                    time.sleep(5)
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
