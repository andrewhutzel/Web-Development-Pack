import random
import string
#We want to create password generator.
#The password will be 24 chars long, no expectation to cross reference across existing passwords
#Requirements:
#-Password must be 24 chars long
#-Password must contain 1 special charatcers
#-Password must contain 1 upper case character
#Rudimentary password generator completed, edge cases not accounted for. A lot left to be desired.
""" def password_gene():
     
    password = ''
    number =0
    special =0
    lower = 0
    upper = 0
    choice=0
    digits=string.digits
    special_chars= string.punctuation
    lower_chars= string.ascii_lowercase
    upper_chars = string.ascii_uppercase
    user_input = input("Enter the length of characters:")
   

    for x in range(1,int(user_input)+1):
        choice=random.randint(1,4)
        if(choice == 1):
             password+=random.choice(digits)
        elif(choice == 2):
             password+=random.choice(special_chars)
        elif(choice == 3):
             password+=random.choice(lower_chars)
        elif(choice == 4):
             password+=random.choice(upper_chars)
    
    #Check for minmum number of characters
    
    for letter in password:
        if letter in digits:
              number+=1
        elif(letter in special_chars):
             special+=1
        elif(letter in lower_chars):
             lower+=1
        elif(letter in upper_chars):
             upper+=1


    if(number>=2 and special>=5 and lower>=3 and upper>=2):
        return password
    else:
        print("This password didn't work:"+ password)
        return password_gene()

final_pass= password_gene()
print("What we finally got:" +final_pass) """


#def profit_margin():
#     revenue =int(input("What is your revenue?"))
#     cost = int(input("What are your costs?"))
#     total = revenue-cost
#     return total/revenue*100

#print(f"Your profit margin is {profit_margin()}%")

""" class Test:
    def __init__(self,first,last,age):
          self.first=first
          self.age=age
          self.last=last
    car = 14
    def func():
        return "Wee"
    def __str__(self):
         return f"This is our newest memeber, {self.first}"
    def greet(self):
         return f"Hey, you, person: { self.first}"

class Order:
     def __init__(self,username,item,total,premo ,status):
          self.username=username
          self.item=item
          self.total=total
          self.premo=premo
          self.status=status
     def calculate(self):
          if(self.premo):
               return f"Thanks for being premo {self.username},this is your item {self.item} and it costs {self.total} "
          else:
               return f"Welcome {self.username}, this is your item {self.item} and it costs {self.total}"
     def shipping(self):
          if(self.status):
               return f"Your {self.item} is currently on the way!"
          else:
               return f"Your {self.item} is still being processed..."
     def __str__(self):
          return f"Item:{self.item} Value:{self.total}"

purchase = Order("Marcus","Box",299,False,False)
print(purchase.calculate())
print(purchase)
print(purchase.shipping()) """

#Block comment is shift + alt + a
""" date = "11/12/2023"

temp_date= date.split("/")
print(temp_date)
date_final=""
for date in temp_date:
    print(date)
    date_final=date_final+date
print(date_final) """