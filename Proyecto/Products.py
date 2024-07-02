
class Product:
    def __init__(self, name,quantity, price, stock, type, sell=0, ):
        self.name = name
        self.price = float(price)*1.16
        self.stock = stock
        self.type = type
        self.sell = sell
    def show_attributes(self):
        print("\n")
        print(f"\t\tProduct Name: {self.name}")
        print(f"\t\tPrice: ${self.price}")
        print(f"\t\tSell: {self.sell}")
        print(f"\t\tStock: {self.stock}")
        print(f"\t\tType: {self.type}")
    def add_sell(self):
        self.sell += 1
        self.stock -= 1
    def dicc(self):
        return {"\n"
                "name":self.name, 
                "price":self.price, 
                "stock":self.stock,
                "sell":self.sell, 
                "type":self.type
            }