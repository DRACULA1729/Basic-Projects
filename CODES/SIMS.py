###################################### Simple Inventory Management System ########################################################


class Items:
    def __init__(self,name,price,quantity) :
        self.name=name
        self.price=price
        self.quantity=quantity
    def displayItems(self):
        print(f'''name - {self.name}\n price -{self.price}\nquantity-{self.quantity}''')
        

class Inventory:
    def __init__(self):
        self.items=[]
    def addItems(self,name,price,quantity):
        for item in self.items:
            if item ==item.name:
                print(f'{name} already exist. Please use update_quantity to modify quantity.')
        self.items.append(Items(name,price,quantity))
    def update_quantity(self,name,new_quantity):
       for item in self.items: 
        if item.name==name:
            self.items[name].quantity+= new_quantity
            print(f'Updated {name} :new quantity is {self.items[name].quantity}')
        else:
            print(f"{name} does not exist inn inventory.")
    def displayItems(self):
        for i in self.items:
            print(i)


inventory1=Inventory()

inventory1.addItems('pencil',25,2500)
inventory1.addItems('pen',25,2500)
inventory1.addItems('pencilstand',25,2500)
inventory1.addItems('scale',25,2500)
inventory1.addItems('box',25,2500)
inventory1.addItems('eraser',25,2500)
inventory1.addItems('marker',25,2500)

inventory1.displayItems()