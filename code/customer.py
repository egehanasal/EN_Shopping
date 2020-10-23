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

    # Method that upgrades the membership by checking how many products that the customer bought.
    def upgrade_membership(self):
        if self.membership == "bronze" and self.product_counter == 4:
            self.membership = "silver"
        elif self.membership == "silver" and self.product_counter == 9:
            self.membership = "gold"

    # Method that increases the product counter.
    def increase_product_counter(self):
        for i in range(len(Basket.basket)):
            self.product_counter += 1

    # Returns the number of customers.
    @classmethod
    def num_of_customers(cls):
        return len(cls.customers)

    # Method that sets discount by checking the membership of the customer.
    def set_discount(self):
        discount = 0
        if self.membership == "bronze":
            discount = 0
        elif self.membership == "silver":
            discount = 10
        elif self.membership == "gold":
            discount = 20
        return discount

    # Method that fixes the 'flus' to 20 after it reached to 30.
    def fix_flus(self):
        if self.flus == 30:
            self.flus = 20
            self.is_fixed = True

    # Method that increases the 'flus' if it is not fixed.
    def increase_flus(self):
        self.fix_flus()
        if not self.is_fixed:
            self.flus += 5

    # Method that adds the product to the basket.
    def add_to_basket(self, product_name):
        is_valid = False
        for i in range(len(Product.products)):
            if Product.products[i].name == product_name:
                Basket.basket.append(Product.products[i])
                Basket.total_price += int(Product.products[i].price)
                break

    # Method that delete the products from the products list after they are sold.
    def delete_products(self):
        temporary_list = list()
        print(Product.products)
        print(Product.products[0].name)
        for p in Product.products:
            if p not in Basket.basket:
                temporary_list.append(p)
        for p in Basket.basket:
            if p.stock > 1:
                p.stock -= 1
                temporary_list.append(p)
        Product.products = temporary_list

    # Method that clears the basket and sets its price to 0.
    def empty_basket(self):
        Basket.basket.clear()
        Basket.total_price = 0

    # Method that adds the customer to the shopped customers list if customer bought any product from the store.
    def add_to_shopped_customers(self):
        if self not in Customer.shopped_customers:
            Customer.shopped_customers.append(self)

    # Method that allows the customer to buy products.
    # This method also does the additional operations after the purchase process.
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
                self.delete_products()
                self.empty_basket()

            else:
                print("Total price of the products are higher than customer's balance.")
        else:
            print("No product in basket.")

    def __str__(self):
        return "Customer name: " + self.name + "\nMembership: " + self.membership + "\n"

    __repr__ = __str__


