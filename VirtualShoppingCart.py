name=input("Hello User! Please enter your name:").strip().title()
print(f'''Hello {name}! How was your day? Hope it was good. Time to order, innit? \nHere i got a cart for you.''')


def getQuantity():
       while True:
        try:
             quantity = int(input("Enter the quantity of the item: "))
             if quantity<=0:
                 print("Quantity must be positive")
             else:
                 return quantity
        except ValueError:
            print("Invalid choice!")

def addItems():
    global items
    items=[]
    counter=0
    while True:
        if counter==0:
         choice=input("Wanna add items: (Yes/No) ").strip().upper()
        else:
            choice=input("You sure you wanna add items: Yes/No").strip().upper() 
        if choice=="YES":
           print('''                            PRICING
                            Bread: 20 bucks
                            Butter: 15 bucks
                            Milk: 30 bucks''')
           i=input("Choose from Bread, Butter and Milk: ").strip().title()
           item=["Bread","Milk","Butter"]
           if i in item:
            items.append(i)
            counter=0
           else:
              print("Enter Valid Choice!")
              counter=counter+1
              continue        

        elif choice=="NO":
                return items
                
        else:
             print("Invalid choice")
   
def quant(items):
 items=set(items)
 global b
 b=[]
 T=0
 sum=0
 items=list(items)
 for i in range(len(items)):
    print("You have selected...",items[i])
    q=getQuantity()
    b.append(q)
    if items[i]=="Butter":
      T =q * 15
      sum=sum+T
    elif items[i]=="Bread":
        T =q * 20
        sum=sum+T
    else:
        T =q * 30
        sum=sum+T
 return sum
def summary(sum):
    for i in range(len( items)):
        print("You have ordered:", b[i],"units",items[i])
    print("Your total cost is:",sum,"\nPleasure business with you! \nHave a good day!!!")
summary(quant(addItems()))
 
