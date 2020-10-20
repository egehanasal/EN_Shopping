from product import Product
from manager import Manager
from customer import Customer
from basket import Basket
import tkinter as tk
from tkinter import *


HEIGHT = 700
WIDTH = 800

root = tk.Tk()
root.title("EN Shopping")

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

m = Manager()
c = Customer("ege", "asal", 300)


# Swaps to the given frame.
def swap(frame):
    frame.tkraise()


# Swaps to the entrance.
def swap_back():
    frame_1.tkraise()
    frame_2.tkraise()
    frame_3.tkraise()


# Method that runs when "add" button for entering the name of the product is clicked.
def add_name():
    global product_name
    product_name = entry_1.get()
    if check_entry(product_name) and not product_name.isdigit():
        entry_1.delete(0, END)
        swap(frame_6)
    else:
        raise_error()
        entry_1.delete(0, END)


# Returns true if the entry box is not empty and not starting with space.
def check_entry(entry):
    if entry != "" and len(entry) > 0:
        if entry[0] != " ":
            return True
    return False


# Method that creates a new window when user enters an invalid input.
def raise_error():
    error_window = tk.Toplevel()
    error_window.geometry("150x75")
    error_label = tk.Label(error_window, text="Invalid Input", bg="red", fg="white")
    error_label.place(relx=0, rely=0, relheight=1, relwidth=1)


# Method that creates a new window if the product that customer wants to buy is sold out.
def sold_out():
    error_window = tk.Toplevel()
    error_window.geometry("150x75")
    error_label = tk.Label(error_window, text="Sold Out", bg="red", fg="white")
    error_label.place(relx=0, rely=0, relheight=1, relwidth=1)


# Method that runs when "add" button for entering the price of the product is clicked.
def add_price(product_name):
    global price
    price = entry_2.get()
    if check_entry(price) and price.isdigit():
        if not is_same(product_name, price):
            add_product(product_name, price)
        entry_2.delete(0, END)
        swap(frame_1)
    else:
        raise_error()
        entry_2.delete(0, END)


# Returns true if the product name is same with another product in product list while their prices are different.
def is_same(product_name, price):
    for product in Product.products:
        if product.name == product_name and product.price == price:
            product.stock += 1
            return True
    return False


# Creates the product and adds it to the product list.
def add_product(product_name, price):
    if len(Product.products) > 0:
        for i in range(len(Product.products)):
            if product_name == Product.products[i].name and price != Product.products[i].price:
                raise_error()
                return
    m.add_product(product_name, price)
    new_button = tk.Button(frame_4, text=product_name, bg="pink", command=lambda: show_info(text_on_button))
    text_on_button = new_button['text']
    new_button.place(relx=0.35, rely=0.15 + (Product.counter / 10), relheight=0.1, relwidth=0.1)


# Method that displays the info (stock and price) of the product.
def show_info(product_name):
    global place
    place = disp_label(product_name)
    global frames_on_products
    frames_on_products = list()
    frame_new = tk.Frame(frame_4, bg="#73c4fa")
    frame_new.place(relx=0.45, rely=0.15+(place/10), relheight=0.1, relwidth=0.2)
    frames_on_products.append(frame_new)
    for i in range(len(Product.products)):
        if product_name == Product.products[i].name:
            info_label = tk.Label(frame_new, bg="#73c4fa", fg="white", text="Stock: " + str(Product.products[i].stock)
                                                  + "\nPrice: " + str(Product.products[i].price))
            info_label.place(relx=0, rely=0, relheight=1, relwidth=0.5)

            if Product.products[i].stock > 0:
                add_to_basket_button = tk.Button(frame_new, bg="#73c4fa", fg="white", text="Add to\n Basket",
                                             command=lambda: add_to_basket(product_name))
                add_to_basket_button.place(relx=0.5, rely=0, relheight=1, relwidth=0.5)


# Method that finds where to put the info of the product button to screen.
def disp_label(product_name):
    for i in range(len(Product.products)):
        if product_name == Product.products[i].name:
            return Product.products[i].counter
    return False


# Method that adds the given product to the basket.
def add_to_basket(product_name):
    is_exist = False
    for p in Product.products:
        if p.name == product_name:
            is_exist = True
            break
    if is_exist:
        c.add_to_basket(product_name)
    else:
        sold_out()


# Method that shows the basket.
def show_basket():
    swap(frame_7)
    global frames_on_basket
    frames_on_basket = list()
    if len(Basket.basket) > 0:
        for i in range(len(Basket.basket)):
            frame_b = tk.Frame(frame_7, bg="pink")
            frame_b.place(relx=0.45, rely=0.15 + (i/10), relheight=0.1, relwidth=0.1)
            frames_on_basket.append(frame_b)
            basket_product_label = tk.Label(frame_b, text=Basket.basket[i].name, bg="pink")
            basket_product_label.place(relx=0, rely=0, relheight=1, relwidth=1)


# Method that allows the customer to buy the products that are added to the basket.
def buy_basket():
    c.buy_products()
    print(Basket.basket)
    for i in range(len(frames_on_basket)):
        frames_on_basket[i].destroy()


# Frame 1: Exists on the entrance of the program, at the top.
frame_1 = tk.Frame(root, bg="#718b28")
frame_1.place(relx=0, rely=0, relheight=0.4, relwidth=1)

label = tk.Label(frame_1, text="EN Shopping", bg="#718b28", fg="white", font="fairwater")
label.place(relx=0.2, rely=0, relheight=0.2, relwidth=0.6)

search_entry = tk.Entry(frame_1, bg="grey", fg="black")
search_entry.place(relx=0.25, rely=0.2, relheight=0.15, relwidth=0.45)

search_button = tk.Button(frame_1, text="search", bg="#0097fb", fg="black")
search_button.place(relx=0.7, rely=0.2, relheight=0.15, relwidth=0.07)

button_account = tk.Button(frame_1, text="My Account", bg="#c2f239")
button_account.place(relx=0.1, rely=0.45, relheight=0.3, relwidth=0.2)

button_products = tk.Button(frame_1, text="Products", bg="#b3dd3b", command=lambda: swap(frame_4))
button_products.place(relx=0.35, rely=0.45, relheight=0.3, relwidth=0.3)

button_basket = tk.Button(frame_1, text="Basket", bg="#99bd34", command=lambda: show_basket())
button_basket.place(relx=0.70, rely=0.45, relheight=0.3, relwidth=0.2)

button_add_product = tk.Button(frame_1, text="Add Product", bg="yellow", fg="black", command=lambda: swap(frame_5))
button_add_product.place(relx=0.35, rely=0.8, relheight=0.18, relwidth=0.3)

enter_product_label = tk.Label(frame_1, text="Enter product name", bg="white", fg="black")


# Frame 2: Exists on the entrance of the program, in the middle of the screen.
frame_2 = tk.Frame(root, bg="#0f9960")
frame_2.place(relx=0, rely=0.4, relheight=0.3, relwidth=1)

label_2 = tk.Label(frame_2, text="Latest Products!", bg="#0f606b", fg="white", font="fairwater")
label_2.place(relx=0.2, rely=0, relheight=0.3, relwidth=0.6)


# Frame 3: Exists on the entrance of the program, at the bottom.
frame_3 = tk.Frame(root, bg="#74106b")
frame_3.place(relx=0, rely=0.7, relheight=0.3, relwidth=1)

label_3 = tk.Label(frame_3, text="Most saled product!", bg="#74106b", fg="white", font="fairwater")
label_3.place(relx=0.2, rely=0, relheight=0.3, relwidth=0.6)


# Frame 4: Appears on the screen after the PRODUCTS button is clicked.
frame_4 = tk.Frame(root, bg="#ff9f77")
frame_4.place(relx=0, rely=0, relheight=1, relwidth=1)

label_products = tk.Label(frame_4, text="Products", bg="#ff9f77", fg="blue", font=("Helvetica", 20))
label_products.place(relx=0.4, rely=0.05, relheight=0.05, relwidth=0.2)

button_back = tk.Button(frame_4, text="<<Back<<", bg="#1d2333",fg="#0068ad",
                        command=lambda: swap_back())
button_back.place(relx=0, rely=0, relheight=0.1, relwidth=0.1)


# Frame 5: Occurs on the screen after Add Product button is clicked, contains add_product_name.
frame_5 = tk.Frame(root)
frame_5.place(relx=0.35, rely=0.32, relheight=0.075, relwidth=0.3)

global entry_1
entry_1 = tk.Entry(frame_5, text="Enter products name", bg="grey")
entry_1.place(relx=0, rely=0, relheight=1, relwidth=0.7)

back_to_main_button = tk.Button(frame_5, text="Back", command=lambda: swap_back())
back_to_main_button.place(relx=0.7, rely=0, relheight=1, relwidth=0.15)

add_name_button = tk.Button(frame_5, text="add", bg="purple", fg="black", command=lambda: add_name())
add_name_button.place(relx=0.85, rely=0, relheight=1, relwidth=0.15)


# Frame 6: Occurs on the screen after Add Product button is clicked, contains add_product_price.
frame_6 = tk.Frame(root)
frame_6.place(relx=0.35, rely=0.32, relheight=0.075, relwidth=0.3)


# Frame 7: Occurs on the screen after Basket button is clicked.
frame_7 = tk.Frame(root, bg="#c5251c")
frame_7.place(relx=0, rely=0, relheight=1, relwidth=1)

button_back_from_basket = tk.Button(frame_7, text="<<Back<<", bg="#1d2333",fg="#0068ad", command=lambda: swap_back())
button_back_from_basket.place(relx=0, rely=0, relheight=0.1, relwidth=0.1)

buy_basket_button = tk.Button(frame_7, text=" Buy\nBasket", bg="yellow", command=lambda: buy_basket())
buy_basket_button.place(relx=0.9, rely=0, relheight=0.1, relwidth=0.1)


global entry_2
entry_2 = tk.Entry(frame_6, text="Enter products price", bg="grey")
entry_2.place(relx=0, rely=0, relheight=1, relwidth=0.7)

back_to_main_button = tk.Button(frame_6, text="Back", command=lambda: swap(frame_1))
back_to_main_button.place(relx=0.7, rely=0, relheight=1, relwidth=0.15)

add_price_button = tk.Button(frame_6, text="add", bg="blue", fg="black", command=lambda: add_price(product_name))
add_price_button.place(relx=0.85, rely=0, relheight=1, relwidth=0.15)


# Mainloop
frame_1.tkraise()
frame_2.tkraise()
frame_3.tkraise()

root.mainloop()


