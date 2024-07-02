class Restaurant:
    def __init__(self, restaurant_name, restaurant_products):
        self.restaurant_name = restaurant_name
        self.restaurant_products = restaurant_products

    def show_attributes(self, stadiums):
        for restaurant in stadiums:
            print(f"Restaurant Name: {self.restaurant_name}")
            print(f"Restaurant Description: {self.restaurant_products}")

    def restaurant_products_dicc(self):
        products = []
        for product in self.restaurant_products:
            products.append(product.dicc())
        return products
    
    def dicc(self):
        return {
            'name': self.restaurant_name,
            'products': self.restaurant_products_dicc()
        }

        
