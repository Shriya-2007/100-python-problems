# Python Program to Print Prime Numbers In a Given Range

while True :
    a = input("Enter the first number of range: ")
    b = input("Enter the last number of range: ")
    try :
        a = int(a)
        b = int(b)
        primes = []
        for i in range(a, b+1) :
            if i < 2 :
                continue
            is_prime = True
            for j in range(2, int(i ** 0.5) + 1):
                if i % j == 0 :
                    is_prime = False
                    break
            if is_prime :
                primes.append(str(i))
        print(f"The prime numbers in range {a} to {b} are :")
        print(", ".join(primes))
        break
    except ValueError :
        print("Please enter valid numbers only.")