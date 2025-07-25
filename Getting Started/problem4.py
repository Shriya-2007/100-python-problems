# Python program to print the sum of N numbers starting from 0 in either the positive or negative direction.

while True :
    n = input("Enter the end number for the sum starting from 0: ")
    try :
        n = int(n)
        total = 0
        if n >= 0 :
            for i in range(1, n+1):
                total += i
        else :
            for i in range(-1, n-1, -1):
                total += i
        print(f"The sum from 0 to {n} is: {total}")
        break
    except ValueError :
        print("Please enter a number.")