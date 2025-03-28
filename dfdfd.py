class Product:
    def __init__(self, name = "None", price = 0):
        self.name = name
        self.price = price
    def info(self):
        print(f"name - {self.name}\nціна - {self.price} грн")

class Customer:
    def __init__(self, name = "Степан Гіга", cart = []):
        self.name = name
        self.cart = cart
    def add_to_cart(self, obj: Product):
        self.cart.append(obj)
    def show_cart(self):
        total_price = 0
        print(f"покупець - {self.name}")
        for i in self.cart:
            print("Додано до кошика:", i.name, i.price)
            total_price += i.price
        print("загальна вартість:", total_price)
f=Product("Murder in the family", 540)
f1=Product("Have you seen me?", 550)
f2=Product("Cat", 530)
f3=Product("Bird", 560)
f.info()
f1.info()
f2.info()
f3.info()
ff=Customer()
ff.add_to_cart(f)
ff.add_to_cart(f1)
ff.add_to_cart(f2)
ff.add_to_cart(f3)
ff.show_cart()
