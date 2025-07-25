# Find the Greatest of the Three Numbers​ in Python

while True :
    a = input("Enter first number: ")
    b = input("Enter second number: ")
    c = input("Enter third number: ")
    try :
        a = int(a)
        b = int(b)
        c = int(c)
        if a > b and a > c :
            print(f"{a} is the greatest number.")
        elif b > a and b > c :
            print(f"{b} is the greatest number.")
        else :
            print(f"{c} is the greatest number.")
        break
    except ValueError :
        print("Please enter valid numbers only.")