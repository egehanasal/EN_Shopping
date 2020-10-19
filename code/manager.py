from product import Product


class Manager:

    def add_product(self, product_name, product_price):
        product_name = Product(product_name, product_price)
        print("Product has added successfully:", product_name.name)

    def delete_product(self, product_name):
        for i in range(len(Product.products)):
            if product_name == Product.products[i].name:
                print("Product has removed successfully:", product_name)
                Product.products.pop(i)
                # Size of 'products' will be decreased after that operation.
                # Without 'break', we'll have an error because there won't be the 'i'th product in products anymore.
                break


