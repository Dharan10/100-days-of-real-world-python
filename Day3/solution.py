# Day 3: Operators (Arithmetic, Comparison, Logical)

print("Easy")
a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
print("Addition:",a+b)
print("Subtraction:",a-b)
print("Multiplication:",a*b)
print("Division:",a/b)

print("\nMedium")

sub=int(input("No of subjects:"))
marks=[]
for i in range(sub):
    marks.append(int(input(f"Enter mark for sub_{i}: ")))
print("Marks:",marks)
for i in marks:
    if i>=40:
        print(f"Pass on subject with mark {i}")
    else:
        print(f"Fail on subject with mark {i}")
for i in marks:
    if i>=80:
        print(f"Good on subject with mark {i}")
    elif i>=60:
        print(f"Medium on subject with mark {i}")
    else:
        print(f"Bad on subject with mark {i}")

print("\nHard")
amt=int(input("Enter total bill amount:"))
rice=int(input("Enter quantity of rice:"))
wheat=int(input("Enter quantity of wheat:"))
discount=0
if amt >=1000:
    discount+=0.1
if rice >=5 and wheat >=5:
    discount+=0.05
finalamt=(amt-(amt*discount))
print("Original Bill:",amt)
print(f"Total Discount:{discount:.2f}%")
print("Final Bill:",finalamt)


 #Easy
 #Enter a number:3
 #Enter a number:4
 #Addition: 7
 #Subtraction: -1
 #Multiplication: 12
 #Division: 0.75

 #Medium
 #No of subjects:2
 #Enter mark for sub_0: 90
 #Enter mark for sub_1: 80
 #Marks: [90, 80]
 #Pass on subject with mark 90
 #Pass on subject with mark 80

 #Good on subject with mark 90
 #Good on subject with mark 80

 #Hard
 #Enter total bill amount:35000
 #Enter quantity of rice:5
 #Enter quantity of wheat:9
 #Original Bill: 35000
 #Total Discount:0.15%
 #Final Bill: 29750.0
