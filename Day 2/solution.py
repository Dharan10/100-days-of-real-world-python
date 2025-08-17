# Day 2: Input & Type Casting

print("#Easy")
age=input("Enter Your Age:")
age=int(age)
print(f"Your age in 2050 will be {age+25}")

print("\n#Medium")
total_bill=float(input("Enter Total Bill:"))
mem=int(input("Enter Number of Members:"))
print(f"Each person should pay {round(total_bill/mem,2)}")

print("\n#Hard")
no1=input("Enter first number: ")
no2=input("Enter second number: ")
print(f"Type of first input: {type(no1)}\nType of second input: {type(no2)}")
no1,no2=float(no1),float(no2)
print(f"Sum of two float inputs: {no1+no2:.2f}")
no1,no2=int(no1),int(no2)
print(f"Multiplication of two int: {no1*no2}")


# output
#Easy
#Enter Your Age:23
#Your age in 2050 will be 48

#Medium
#Enter Total Bill:450
#Enter Number of Members:6
#Each person should pay 75.0

#Hard
#Enter first number: 45
#Enter second number: 9.0
#Type of first input: <class 'str'>
#Type of second input: <class 'str'>
#Sum of two float inputs: 54.00
#Multiplication of two int: 405