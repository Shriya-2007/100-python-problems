# Python Program to Find the Sum of First N Natural Numbers0

while True :
    n = input("Enter how many first natural numbers you want to sum up: ")
    try :
        n = int(n)
        total = 0
        for i in range(1, n+1) :
            total += i
        print(f"The sum of first {n} natural numbers is: {total}")
        break
    except ValueError :
        print("Please enter the number of terms.")