apple=int(input("Apple Sold:"))
banana=int(input("Banana Sold:"))
orange=int(input("Orange Sold:"))

total_fruit_sold=apple+banana+orange
apple_percent=apple/total_fruit_sold*100
banana_percent=banana/total_fruit_sold*100
orange_percent=orange/total_fruit_sold*100
print(f"Total Fruit Sold: {total_fruit_sold:.2f}\n Apple percentage:{apple_percent:.2f}\n Banana percentage:{banana_percent:.2f}\n Orange percentage:{orange_percent:.2f}")