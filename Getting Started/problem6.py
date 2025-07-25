# Find the Greatest of Two Numbers in Python

while True :
    a = input("Enter the one number: ")
    b = input("Enter another number: ")
    try :
        a = int(a)
        try :
            b = int(b)
            if a > b :
                print(f"{a} is greater than {b}.")
            elif a < b :
                print(f"{b} is greater than {a}.")
            else :
                print(f"Both numbers are equal.")
            break
        except ValueError :
            print("You entered the second term incorrectly. Please enter a number.")
    except ValueError :
        print("You entered the first term incorrectly. Please enter a number.")