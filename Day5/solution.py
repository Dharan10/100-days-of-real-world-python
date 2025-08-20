def easy():
    print("#Easy")
    name=input("Enter your Name:")
    print("Hi {}!".format(name))

def medium():
    print("#Medium")
    item=input("Enter item name:")
    quantity=int(input("Enter item quantity:"))
    price=int(input("Enter item price:"))
    print("{}kg of {} cost {}".format(quantity,item,price))

def hard():
    print("#Hard")
    name=input("Enter name:")
    mark=[]
    for i in range(3):
        mark.append(int(input("Enter mark:")))
    tot=sum(mark)
    avg=sum(mark)/len(mark)
    print(f"Name: {name}\nMarks {mark} \nTot:{tot}\nAverage:{avg}")