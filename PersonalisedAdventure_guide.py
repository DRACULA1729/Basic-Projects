name=input("Hello User! Please enter your name:").strip().title()
print(f'''Hello {name}! How was your day? Hope it was good. Time to travel, innit?
      Please select any options from the following
      Mountain / Beach''')


def getValidInput(prompt):
    while True:
        try:
            num = int(input(prompt))
            return num
        except ValueError:
            print("Invalid choice!")



def desti():
    t=input("Enter choice:").strip().title()
    if t=='Mountain':
        print('You have chosen Mountain. You are going to the mountains.')
        budget()
    elif t=='Beach':
        print('You have chosen Beach. You are going to the beaches.')
        budget()
    else:
        print("Invalid Choice.")
        return desti()
def budget():
    
    b=getValidInput("Enter your budget:")
    if b>=500:
        print(f'{b} bucks is quite expensive.\nDo not worry i still got your back. \nLets calculate your total cost.')
        budgetEva(b)
    elif b>=200:
        print(f'{b} bucks is good budget.\nDo not worry i still got your back. \nLets calculate your total cost.')
        budgetEva(b)
    elif b<200 and b<=0:
        print(f'{b} bucks is budget friendly.\nDo not worry i still got your back. \nLets calculate your total cost.')
        budgetEva(b)
    else:
        print("Invalid Budget")
        budget()
def budgetEva(x):
    days=int(input(getValidInput("Enter the number of days you will be staying:")))
    print("The total cost will be", days*x,"bucks")


desti()
