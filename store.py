class Store:
    def __init__(self, product):
        self.name = "Cadens Market"
        self.product = [product]

    def add_product(self, new_product):
        self.product.append(new_product)
        return self
    

class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def update_price(self, percent_changed, is_increased):
        if is_increased == True:
            self.price += (percent_changed/100)
        else:
            self.price -= (percent_changed/100)
    
    def print_info(self):
        print(f"{self.name} are ${self.price} and can be found in the {self.category} section")

store = Store("apples")
apples = Product("apples", 1.00, "fruit")
apples.update_price(10, False)
apples.print_info()
store.add_product("oranges").add_product("bananas")

print(store.product)