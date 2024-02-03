#shopping = True;
#total=0;
#items=0;
#while(shopping):
#    print("1. Coffee 5$")
 #   print("2. Cups 20$")
  #  print("3. Throw money 500$")
   # print("4. Let me out of here")
    #match int(input("Enter number for item")):
     #   case 1:
      #      total+=5
       #     items+=1
        #case 2:
         #   total+=20
          #  items+=1
        #case 3:
         #   total+=500
          #  items+=1
        #case 4:
         #   shopping=False

#print(f"Price{total}")

#if(total>=500 and items >=5):
#    print(f"Discount 15 percent applied, total is now:{total-(total*.15)}")
#elif(total>=200):
#    print(f"Discount 5 percent applied, total is now:{total-(total*.05)}")
#else:
#    print(f"No discount applied, total is now:{total}")

#print(f"Total items:{items}")


#listers = ['us','ca','ba']

#scores=[1,554,4,254,168,84]

#I declare two arrays, even_num & myst_num. Myst_num takes only two inputs from the user to test if the array is able to differentiate between odd and even numbers.
#Once we've explicitly declared the input as INT for myst_num, we take the user input.
#Now that the numbers have been appended, we loop through myst_num. For all even numbers found in myst_num we append it to the end of the list for even_num.

#even_num=[1,2,3,4,5,6]
#even_num.append(int(input("Please add a number:")))
#even_num.append(int(input("Please add a number:")))
#print("This is the list:",even_num)
#for i in even_num:
#    if(i%2!=0):
#        even_num.remove(i)
#print("This is the final list:",even_num)
#list_arr=[]
#stop=""
#temp=0
#while True:
#    temp =(int(input("Please enter a number:")))
#    if(temp%2==0):
#        list_arr.append(temp)
#    stop=input("Do you want to continue(y/n)?")
#    if(stop=='y' or stop=='Y'):
#       break
#print("This is the final list:", list_arr)
#even=[]
#odd=[]
#for i in range(1,101):
#    if(i%2==0):
#        even.append(i)
#    else:
#        odd.append(i)
#    print("This is i:",i)
#print("This is even",even)
#print("This is odd",odd)
#Playing around with the numbers, didn't like declaring another array...
#numbers = [1, 2, 3, 4, 5, 6, 7, 8]
#temp=0
#dex=0
# add your code below this line:
#for i in numbers:
#    temp=i*i
#    del numbers[dex]
#    numbers.insert(dex,temp)
#    dex+=1
#print(numbers)

import random

