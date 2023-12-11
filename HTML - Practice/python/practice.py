shopping = True;
total=0;
items=0;

while(shopping):
    print("1. Coffee 5$")
    print("2. Cups 20$")
    print("3. Throw money 500$")
    print("4. Let me out of here")
    match int(input("Enter number for item")):
        case 1:
            total+=5
            items+=1
        case 2:
            total+=20
            items+=1
        case 3:
            total+=500
            items+=1
        case 4:
            shopping=False

print(f"Price{total}")

if(total>=500):
    print(f"Discount 15 percent applied, total is now:{total-(total*.15)}")
elif(total>=200):
    print(f"Discount 5 percent applied, total is now:{total-(total*.05)}")
else:
    print(f"No discount applied, total is now:{total}")

print(f"Total items:{items}")