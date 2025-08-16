# Day 1 – Python Basics: Variables, Data Types, and Print
print("#Easy")
base_rate=120
cup_bought=3
total_price=base_rate*cup_bought
print(f"The total cost for {cup_bought} cups of coffee is {total_price} rupees.")

print("\n#Medium")
name="Dharan"
age=24
sub_1_mark=80
sub_2_mark=50
sub_3_mark=70
avg_mark=(sum([sub_1_mark,sub_2_mark,sub_3_mark])/3)
total_subject=3
#print(f"The average mark of {name} of age {age} on {total_subject} subjects is {avg_mark}")
print(f"Student: {name} \nAge: {age} \nAverage Marks: {avg_mark:.2f}")

print("\n#Hard")
monthly_income=50000
food=3000
rent=5000
dress=3000
emi=15000
total_expence=food+rent+dress+emi
savings=monthly_income-total_expence
print(f"Monthly Income: {monthly_income} \n Expences: \n Food: {food} \n Rent: {rent} \n Dress: {dress} \n EMI: {emi} \n Total Expence: {total_expence} \nSavings: {savings}")
