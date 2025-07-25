# Python Program to Check Whether a Number is Even or Odd

while True :
    a = input("Enter a number: ")
    try :
        a = int(a)
        if a % 2 == 0 :
            print(f"The number {a} is even.")
        else :
            print(f"The number {a} is odd.")
        break
    except ValueError :
        print("Please enter a number.")
