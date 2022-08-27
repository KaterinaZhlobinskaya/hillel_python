class Product:
    def __init__(self, name, color, price, amount, discount):
        self.name = name
        self.color = color
        self.price = price
        self.amount = amount
        self.discount = discount

    def get_product_description(self):
        return f"{self.name} {self.color}: IT'S COAST - {self.price} |AMOUNT: {self.amount}|  ->  -{self.discount*100}% "

    def show_description(self):
        print(f"Description: {self.get_product_description()}  --> = NEW PRICE: {self.get_price()}")

    def get_price(self):
        new_price = self.price - self.price*self.discount if self.discount else self.price
        return f"{new_price}"

class Phone(Product):
    def __init__(self, name, color, price, amount, discount, lte=False):
        # Product.__init__(self, name, color, price, amount, discount)
        super().__init__(name, color, price, amount, discount)
        self.lte = lte

    def get_product_description(self):
        additional = ", LTE" if self.lte else ""
        message = super().get_product_description()
        message += additional 

        return message

    # def show_description(self):
    #     # if self.lte is True:
    #     #     additional = "LTE"
    #     # else:
    #     #     additional = ""
    #     additional = "LTE" if self.lte else ""
    #     print(f"Description: {self.name}/{self.color}: {self.price} | {self.amount}, {additional}")


class Laptop(Product):
    def __init__(self, name, color, price, amount, discount, motherboard_type, material):
        super().__init__(name, color, price, amount, discount)
        self.motherboard_type = motherboard_type
        self.material = material
    
    def get_product_description(self):
        message = super().get_product_description() 
        message += self.show_details()
        
        return message 

    def show_details(self):
        haracteristics = f" some details:  {self.motherboard_type},  {self.material}"        
        return f"{haracteristics}" 


iphone7 = Phone(name="iPhone 7", color="red", price=700.0, amount=1, discount=0.25)
iphone13 = Phone(name="iPhone 13", color="black", price=2000.0, amount=2, lte=True, discount=0.05)
lenovo = Laptop(name="Lenovo", color="grey", price=3000.0, amount=4, discount=0, motherboard_type="  Mini-ITX", material="plastic")
dell = Laptop(name="Dell", color="metalic", price=2760.0, amount=7, discount=0.15, motherboard_type="  Micro-ATX", material="metal")
iphone13.show_description()
iphone7.show_description()
lenovo.show_description()
dell.show_description()