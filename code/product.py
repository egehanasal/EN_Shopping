from finance import Finance


class Product:

    products = list()
    counter = 0

    def __init__(self, name, price):
        self.name = name
        self.price = price
        Product.counter += 1
        self.counter = Product.counter
        self.stock = 1
        if self.check_product(self.name):
            Product.products.append(self)

    @staticmethod
    def check_product(product_name):
        for i in range(len(Product.products)):
            if product_name == Product.products[i].name:
                return False
        return True

    def sell(self):
        Product.products.remove(self)
        Finance.budget += self.price
        Finance.report(self.name, self.price, "income")
        if self.stock > 1:
            self.stock -= 1

