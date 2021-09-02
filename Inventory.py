# inventory system project

from datetime import datetime
import random
import sys

all_products = [
[1,"Chocos",20,500],
[2,"Cake",450,500],
[3,"Parle G Biscuits",10,500],
[4,"Oreo Biscuits",25,500],
[5,"Bourbon Biscuits",18,500],
[6,"Butter Bite",25,500],
[7,"Munch",10,500],
[8,"Dairy Milk",40,500],
[9,"Kitkat",20,500],
[10,"5 star",10,500],
[11,"Aloo Bhujiya",38,500],
[12,"Moong daal namkeen",40,500],
[13,"Punjabi tadka",20,500],
[14,"Mixture Namkeen",35,500],
[15,"Khatta Meetha Namkeen",40,500],
[16,"Dove Soap",50,500],
[17,"Lux Soap",36,500],
[18,"Dettol Soap",28,500],
[19,"Cinthol Soap",45,500],
[20,"Pears Soap",55,500],
[21,"Eclairs toffee",70,500],
[22,"Kaccha aam toffee",65,500],
[23,"Coffee Bite toffee",68,500],
[24,"Pulse toffee",85,500],
[25,"Kismi Toffee",46,500],
[26,"Rin Detergent powder",60,500],
[27,"Tide detergent powder",48,500],
[28,"Surf exel detergent powder",50,500],
[29,"Colgate Toothpaste",57,500],
[30,"CloseUp Toothpaste", 66,500],
[31,"Sensodyne Toothpaste",55,500],
[32,"Maggi noodles",48,500],
[33,"Top Ramon Noodles",45,500],
[34,"Yippee Noodles",46,500],
[35,"Kissan Ketchup",115,500],
[36,"Tomato Sauce",65,500],
[37,"Chili Sauce",65,500],
[38,"Soya Sauce",65,500],
[39,"Amul Ghee",450,500],
[40,"Dawat Basmati Rice",193,500],
[41,"Arhar Daal 1kg pkt",95,500],
[42,"Ashirwad Aata 5kg pkt",120,500],
[43,"Schezwan Chutney",119,500],
[44,"Fogg Body Perfume",180,500],
[45,"Park Avenue Deodorant",210,500],
[46,"Almond Drop Hair Oil",132,500],
[47,"Dettol Handwash",90,500],
[48,"Kurkure Masala",20,500],
[49,"Uncle Chips",20,500],
[50,"Tea Marvel Gold 500mg",140,500]



]


def banner():
    print("*************")
    print("\tGrofers Super Market")
    print("\t*************")
    print("\t1.Show All Products")
    print("\t2.Buy Product")
    print("\t3.Add Products")
    print("\t4.Exit")
    print("\t**************")


def display_all():
    print("Product_Id\tProdcut_Name\t\tPrice\tAvailable_Quantity")
    for item in all_products:
        print("{0}\t{1}\t\t\t{2}\t\t\t\t{3}".format(item[0], item[1], item[2], item[3]))


def order_summary(product, name):
    print("*****************")
    print("\t\tGrofers Super Market")
    print("*****************")
    print("Order Summary\tDate:{}".format(str(datetime.now())))
    print("Customer Name: {}".format(name))
    print("Product Name: {}".format(item[1]))
    print("Price for single item: {}".format(item[-2]))
    print("*****************")


def generate_bill(product, name):
    print("*****************")
    print("\t\tGrofers Super Market")
    print("*****************")
    print("Bill:{} \tDate:{}".format(int(random.random() * 100000), str(datetime.now())))
    print("Customer Name: {}".format(name))
    print("Product Name: {}".format(item[1]))
    print("Price: {}".format(item[-2]))
    print("*****************")
    print("\t\tTotal Bill Amount: {}".format(item[-2]))


while (True):
    banner()
    choice = int(input(""))
    if choice == 1:
        display_all()
    elif choice == 2:
        display_all()
        prod_id = int(input("Enter the Product ID: "))
        prod_quant=int(input("Enter the quantity of product"))
        for item in all_products:
            if item[0] == prod_id:
                name = input("Customer Name: ")
                order_summary(item, name)
                cnf = input("Confirm the Order(Y/N)")
                if cnf == 'Y':
                    print("-----------------------------")
                    print("Billing Amount: ",prod_quant*int(item[2]))
                    print()
                    print()
                    print()
                    print("!!!Thanks For shopping with Us!!!")
                    print("-----------------------------")
                    sys.exit(0)
                else:
                    print("Continue Exploring the shop")
    elif choice == 3:
        username = input("Enter Admin UserID: ")
        password = input("Enter the Password: ")
        if username == "Admin" and password == "password":
            prod = []
            prod.append(len(all_products) + 1)
            prod.append(input("Enter the Product Name: "))
            prod.append(int(input("Available: ")))
            prod.append(int(input("Price: ")))
            all_products.append(prod)
        else:
            print("Incorrect username and password")
    else:
        print("GoodBye!!")
        break