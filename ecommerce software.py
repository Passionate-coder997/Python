#Creating Classes
class Customer:
    def __init__(self, name,phone,email):
        self.name=name
        self.phone=phone
        self.email=email
        self.purchases=[]

    def purchase(self,inventory,product):
        inventory_dictionary=inventory.inventory
        if product in inventory_dictionary:
            if inventory_dictionary[product]>0:
                self.purchases.append(product)
                inventory_dictionary[product] -= 1
            else:
                print('The product is currently out of stock')
        else:
            print("We don't have that product")
    def print_purchase(self):
        for item in self.purchases:
            print(item.name)

class Product:
    def __init__(self,name,price):
        self.name=name
        self.price=price

class Inventory:
    def __init__(self):
        self.inventory={}
    def add_Product(self,product,qty):
        if product not in self.inventory:
            self.inventory[product] = qty
        else:
            self.inventory[product] += qty
    def print_inventory(self):
        for key,value in self.inventory.items():
            print(key.name + ": "+ str(value))
        


#Creating Object
customer=Customer('john', +919824285474, 'john.miller@gmail.com')
shirts=Product('shirts', 2455)
#pants=Product('pants', 400)

inventory=Inventory()
inventory.add_Product(shirts, 300)
inventory.print_inventory()
customer.purchase(inventory, shirts)
customer.print_purchase()
inventory.print_inventory()