# Leap Year Program in Python

while True :
    year = input("Enter the year: ")
    try :
        year = int(year)
        if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0) :
            print(f"{year} is a leap year.")
        else :
            print(f"{year} is not a leap year.")
        break
    except ValueError :
        print("Please enter a valid year only.")
        