# Python Program to check if a Number Is Positive Or Negative

while True:
    a = input("Enter a number: ")
    try :
        a = int(a)
        if a > 0 :
            print(f"The number {a} is positive.")
        elif a < 0 :
            print(f"The number {a} is negative.")
        else :
            print(f"The number {a} is zero.")
        break
    except ValueError :
        print("Please enter a integer.")


        