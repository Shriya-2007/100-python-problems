# Prime Number Program in Python

while True :
    a = input("Enter a number: ")
    try :
        a = int(a)
        flag = 0
        for i in range(2, int(a ** 0.5) + 1):
            if a % i == 0 :
                flag = 1
                break
        if flag == 1 :
            print(f"{a} is not a prime number.")
        else :
            print(f"{a} is a prime number.")
                
    except ValueError :
        print("Please enter a valid number only.")