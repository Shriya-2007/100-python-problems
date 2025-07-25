# Find the Sum of Numbers in a given Range in Python

while True :
    a = input("Enter the first number of range: ")
    b = input("Enter the last number of range: ")
    try :
        a = int(a)
        try :
            b = int(b)
            total = 0
            if a <= b :
                for i in range(a, b+1):
                    total += i
            else : 
                for i in range(a, b-1, -1):
                    total += i
            print(f"The sum of numbers in range from {a} to {b} is: {total}")
            break
        except ValueError :
            print("You entered the last number of range incorrectly. Please enter a number.")
    except ValueError :
        print("You entered the first number of range incorrectly. Please enter a number.")