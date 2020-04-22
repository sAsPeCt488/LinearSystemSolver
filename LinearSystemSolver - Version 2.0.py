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


# Makes (Graphically) the system
def system_maker(a, b, c, a2, b2, c2, unknown1, unknown2, sign1="=", sign2="="):
    unknown1syst2 = unknown1
    unknown2syst2 = unknown2

    if a == 0:
        unknown1 = ""
        string_a = ""
    elif a == 1:
        string_a = ""
    elif a == -1:
        string_a = "-"
    elif a > 0:
        string_a = str(a)
    elif a < 0:
        string_a = "-" + str(a)

    if a2 == 0:
        unknown1syst2 = ""
        string_a2 = ""
    elif a2 == 1:
        string_a2 = ""
    elif a2 == -1:
        string_a2 = "-"
    elif a2 > 0:
        string_a2 = str(a2)
    elif a2 < 0:
        string_a2 = "-" + str(a2)

    if b == 0:
        unknown2 = ""
        string_b = ""
    elif b == 1:
        string_b = "+"
    elif b == -1:
        string_b = "-"
    elif b > 0:
        string_b = str(b)
    elif b < 0:
        string_b = "-" + str(b)

    if b2 == 0:
        string_b2 = ""
        unknown2syst2 = ""
    elif b2 == 1:
        string_b2 = "+"
    elif b2 == -1:
        string_b2 = "-"
    elif b2 > 0:
        string_a = str(b2)
    elif b2 < 0:
        string_b2 = "-" + str(b2)

    if c == 0:
        c_string = ""
        sign1 = ""
    elif c < 0:
        c_string = "-" + str(c)
    elif c > 0:
        c_string = str(c2)

    if c2 == 0:
        c2_string = ""
        sign2 = ""
    elif c2 < 0:
        c2_string = "-" + str(c)
    elif c2 > 0:
        c2_string = str(c2)

    systems = f'''{string_a}{unknown1}{string_b}{unknown2} {sign1} {c_string}   
{string_a2}{unknown1syst2}{string_b2}{unknown2syst2} {sign2} {c2_string} '''  # Construct the system
    print(systems)


repeat = True

while repeat:
    try:
        # Global values (glbl : global)1
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
