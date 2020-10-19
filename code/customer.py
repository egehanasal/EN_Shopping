from product import Product
from finance import Finance
from basket import Basket


class Customer:
    customers = list()
    is_fixed = False
    shopped_customers = list()

    def __init__(self, name, last, balance):
        self.name = name
        self.last_name = last
        self.balance = balance
        self.membership = "bronze"
        # flus: Customer earns 5 flus' (5% discount) every time by buying a product. It will be fixed to 20 if it is 30
        self.flus = 0
        self.customers.append(self)
        self.product_counter = 0

    def upgrade_membership(self):
        if self.membership == "bronze" and self.product_counter == 4:
            self.membership = "silver"
        elif self.membership == "silver" and self.product_counter == 9:
            self.membership = "gold"

    def increase_product_counter(self):
        for i in range(len(Basket.basket)):
            self.product_counter += 1

    @classmethod
    def num_of_customers(cls):
        return len(cls.customers)

    def set_discount(self):
        discount = 0
        if self.membership == "bronze":
            discount = 0
        elif self.membership == "silver":
            discount = 10
        elif self.membership == "gold":
            discount = 20
        return discount

    def fix_flus(self):
        if self.flus == 30:
            self.flus = 20
            self.is_fixed = True

    def increase_flus(self):
        self.fix_flus()
        if not self.is_fixed:
            self.flus += 5

    def add_to_basket(self, product_name):
        is_valid = False
        for i in range(len(Product.products)):
            if Product.products[i].name == product_name:
                Basket.basket.append(Product.products[i])
                Basket.total_price += int(Product.products[i].price)
                is_valid = True
                break
        if not is_valid:
            print("Invalid Product...")

    def delete_from_basket(self, product_name):
        for i in range(len(Basket.basket)):
            if Basket.basket[i].name == product_name:
                Basket.basket.pop(i)

    def empty_basket(self):
        Basket.basket.clear()
        Basket.total_price = 0

    def add_to_shopped_customers(self):
        if self not in Customer.shopped_customers:
            Customer.shopped_customers.append(self)

    def buy_products(self):
        if len(Basket.basket) != 0:
            discount = self.set_discount()
            new_price = (100 - discount) * Basket.total_price / 100
            new_price = (100 - self.flus) * new_price / 100
            if self.balance >= new_price:
                print("Products are sold for: $", new_price)
                self.balance -= new_price
                Finance.budget += new_price
                self.add_to_shopped_customers()
                self.increase_product_counter()
                self.increase_flus()
                self.upgrade_membership()
                self.empty_basket()

            else:
                print("Total price of the products are higher than customer's balance.")
        else:
            print("No product in basket.")

    def __str__(self):
        return "Customer name: " + self.name + "\nMembership: " + self.membership + "\n"

    __repr__ = __str__


