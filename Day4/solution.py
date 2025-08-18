# Day 4: Conditional Statements

def easy():
    print("#Easy")
    a=int(input("Enter a number:"))
    if a%2 ==0:
        print("Its even number")
    else:
        print("Its odd number")

def medium():
    print("\n#Medium")
    mark={}
    n=int(input("Enter number of subjects:"))
    for i in range(n):
        sub=input(f"Enter subject {i+1} name:")
        m=int(input("Enter marks:"))
        mark[sub]=m
    for sub,m in mark.items():
        if m>=90:
            print(f"{sub} : A")
        elif m >=75 or m <=89:
            print(f"{sub} : B")
        elif m >=50 or m <=74:
            print(f"{sub} : C")
        else:
            print(f"{sub} : F")

def hard():
    print("\n#Hard:")
    year=int(input("Enter a year:"))
    if year%400==0:
        print(f"The year {year} is a leap year")
    elif year%4==0 and year%100!=0:
        print(f"The year {year} is a leap year")
    else:
        print(f"The year {year} is not a leap year")