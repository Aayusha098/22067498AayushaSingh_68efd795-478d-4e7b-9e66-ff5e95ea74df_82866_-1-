from read import readtxtfile
from datetime import datetime

def purchase_laptops():
    print("Thank you for buying")
    print("-----------------------------------------------------------")
    print("We will need your name and number to print bill")
    print("-----------------------------------------------------------")
    print("\n")
    name = input("Enter your name")
    phone = input("Enter your phone")
    print("S.N. \t Name \t  Brand \t unit Price \t Quantity \t Processor \t Graphic Card \t")
    a=1
    file = open("Laptop.txt","r")
    for line in file:
        print(a,"\t "+line.replace(",","\t"))
        a+=1
    print("-----------------------------------------------------------")
    file.close()
    print("\n")

    valid_id = int(input("please provide the ID of the Laptop you want to buy: "))
    print("\n")

    # Valid ID

    while valid_id <= 0 or valid_id > len(readtxtfile()):
        
        print("Please provide a valid Laptop ID !!!")
        
        print("\n")
        
        valid_id = int(input("Please provide the ID of the Laptop you want to buy:"))
    user_quantity = int(input("Please provide the number of quantity of the laptop you want to buy: "))
    print("\n")

    # valid quantity
    mydictonary = readtxtfile()
    get_quantity = mydictonary[valid_id][3]
    while user_quantity <= 0 or user_quantity > int(get_quantity):
        print("Dear Admin the quantity you looking is not available in our shop, Please look again in the Laptop screen")
        print("\n")

        user_quantity = int(input("Please provide the number of quantity of the laptop you want to buy: "))
    print("\n")

    # update the text file

    mydictonary[valid_id][3] = int(mydictonary[valid_id][3])+int(user_quantity)

    file = open("Laptop.txt", "w")

    for values in mydictonary.values():
        file.write(str(values[0])+","+str(values[1])+","+str(values[2])+","+str(values[3])+","+str(values[4])+","+str(values[5]))
        file.write("\n")
    file.close()

    # purchasing from manufacture

    product_name = mydictonary[valid_id][0]
    brand_name = mydictonary[valid_id][1]
    quantity_selected_by_user = user_quantity
   # unit_price = mydictonary[valid_id][2]
    selected_item_price = mydictonary[valid_id][2].replace("$",'')
    total_price = int(selected_item_price)*int(quantity_selected_by_user)
    #final_total = total_price + VAT
    #VAT = VAT + 0.13 * total_price
    #grand_total = final_total + VAT

    user_purchased_laptops = []
    user_purchased_laptops.append([product_name,brand_name, quantity_selected_by_user, selected_item_price, total_price])
    VAT = 0
    total_with_vat = 0
    final_total = 0
    final_total = final_total + total_price


    purchase_loop = True
    while purchase_loop ==  True:
        purchase = input("Do you want to purchase more laptops?(y/n:)")
        if purchase == "y" or purchase == "Y":

            # Valid ID

            while valid_id <= 0 or valid_id > len(readtxtfile()):

                print("Please provide a valid Laptop ID !!!")
                print("\n")

            valid_id = int(input("Please provide the ID of the Laptop you want to buy:"))
            user_quantity = int(input("Please provide the number of quantity of the laptop you want to buy: "))
            print("\n")

            # valid quantity
            mydictonary = readtxtfile()
            get_quantity = mydictonary[valid_id][3]
            while user_quantity <= 0 or user_quantity > int(get_quantity):
                print("Dear Admin the quantity you looking is not available in our shop, Please look again in the Laptop screen")
                print("\n")

                user_quantity = int(input("Please provide the number of quantity of the laptop you want to buy: "))
            print("\n")

            # update the text file

            mydictonary[valid_id][3] = int(mydictonary[valid_id][3])+int(user_quantity)

            file = open("Laptop.txt", "w")

            for values in mydictonary.values():
                file.write(str(values[0])+","+str(values[1])+","+str(values[2])+","+str(values[3])+","+str(values[4])+","+str(values[5]))
                file.write("\n")
            file.close()

            # purchasing from manufacture

            product_name = mydictonary[valid_id][0]
            brand_name = mydictonary[valid_id][1]
            quantity_selected_by_user = user_quantity
            #unit_price = mydictonary[valid_id][2]
            selected_item_price = mydictonary[valid_id][2].replace("$",'')
            total_price = int(selected_item_price)*int(quantity_selected_by_user)
            final_total = final_total + total_price
            VAT = 0 
            VAT = VAT + 0.13 * final_total
            total_with_vat = VAT + final_total

            user_purchased_laptops.append([product_name,brand_name, quantity_selected_by_user, selected_item_price, total_price])
        else:
            break
    VAT = 0.13 * final_total
    total_with_vat = VAT + final_total
            #purchase_loop = False





    #total = 0
    #VAT = 0.13*(total_price)
    #for i in user_purchased_laptops:
        #total += int(i[3])
    #grand_total = total_price + VAT
    today_date_and_time = datetime.now()
    print("\n")
    print("\t \t \t \t Aayusha's laptop Shop Bill ")
    print("\n")
    print("\t \t Kamalpokhari, Kathmandu / Phone No: 9817787870 ")
    print("\n")
    print("------------------------------------------------------------------------------------------------------------")
    print("laptop Details are:")
    print("------------------------------------------------------------------------------------------------------------")
    print("name of the customers:"+str(name))
    print("Contact number: "+str(phone))
    print("Date and time of purchase: "+str(today_date_and_time))
    print("------------------------------------------------------------------------------------------------------------")
    print("\n")
    print("Purchased Details are:")
    print("------------------------------------------------------------------------------------------------------------")
    print("Items Name \t Brand \t\t Total Quantity \t Unit Price \tTotal")
    for i in user_purchased_laptops:
        print(i[0],"\t",i[1],"\t",i[2],"\t\t\t",i[3],"\t","$",i[4])
    print("------------------------------------------------------------------------------------------------------------")
    
    print("VAT Amount:", VAT)
    print("Grand Total: $"+str(total_with_vat))
    print("Note: VAT Amount is added to grand total")

    return name, phone, today_date_and_time,user_purchased_laptops,VAT,final_total,total_with_vat
   











def sold_laptops():
    print("Thank you for selling")
    print("-----------------------------------------------------------")
    print("We will need your name and number to print bill")
    print("-----------------------------------------------------------")
    print("\n")
    name = input("Enter your name")
    phone = input("Enter your phone")
    print("S.N. \t Name \t \t Brand \t \t Quantity  \t Price  \t Processor  \t Graphic Card \t")
    a=1
    file = open("Laptop.txt","r")
    for line in file:
        print(a,"\t "+line.replace(",","\t"))
        a+=1
    file.close()
    print("\n")

    valid_id = int(input("please provide the ID of the Laptop you want to sell: "))
    print("\n")

    # Valid ID

    while valid_id <= 0 or valid_id > len(readtxtfile()):
        
        print("Please provide a valid Laptop ID !!!")
        
        print("\n")
        
        valid_id = int(input("Please provide the ID of the Laptop you want to sell:"))

    user_quantity = int(input("Please provide the number of quantity of the laptop you want to sell: "))
    print("\n")

    # Valid Quantity
    mydictonary = readtxtfile()
    get_quantity = mydictonary[valid_id][3]
    while user_quantity <= 0 or user_quantity > int(get_quantity):
        print("Dear Admin the quantity you looking is not available in our shop, Please look again in the Laptop screen")
        print("\n")

        user_quantity = int(input("Please provide the number of quantity of the laptop you want to sell: "))
    print("\n")

    #Update the text file

    mydictonary[valid_id][3] = int(mydictonary[valid_id][3])-int(user_quantity)

    file = open("Laptop.txt", "w")

    for values in mydictonary.values():
        file.write(str(values[0])+","+str(values[1])+","+str(values[2])+","+str(values[3])+","+str(values[4])+","+str(values[5]))
        file.write("\n")
    file.close()


    # getting user purchased items

    product_name = mydictonary[valid_id][0]
    brand_name = mydictonary[valid_id][1]
    quantity_selected_by_user = user_quantity
    unit_price = mydictonary[valid_id][2]
    selected_item_price = mydictonary[valid_id][2].replace("$",'')
    total_price = int(selected_item_price)*int(quantity_selected_by_user)

    user_purchased_laptops = []
    user_purchased_laptops.append([product_name,brand_name, quantity_selected_by_user, selected_item_price, total_price])
    grand_total_price = 0
    grand_total_price = grand_total_price + total_price

    sales_loop = True
    while sales_loop == True:
        continue_sales = input("Do You Want To sell More Laptops? (y/n)").lower()
        if continue_sales == "y":
            # Valid ID

            valid_id = int(input("Please provide the ID of the Laptop you want to sell:"))
            while valid_id <= 0 or valid_id > len(readtxtfile()):
                print("Please provide a valid Laptop ID !!!")
                print("\n")
                valid_id = int(input("Please provide the ID of the Laptop you want to sell:"))

                # user_quantity = int(input("Please provide the number of quantity of the laptop you want to sell: "))
                # print("\n")

            # Valid Quantity
            mydictonary = readtxtfile()
            user_quantity = int(input("Please provide the number of quantity of the laptop you want to sell: "))
        
            get_quantity = mydictonary[valid_id][3]
            while user_quantity <= 0 or user_quantity > int(get_quantity):
                print("Dear Admin the quantity you looking is not available in our shop, Please look again in the Laptop screen")
                print("\n")


            #Update the text file

            mydictonary[valid_id][3] = int(mydictonary[valid_id][3])-int(user_quantity)

            file = open("Laptop.txt", "w")

            for values in mydictonary.values():
                file.write(str(values[0])+","+str(values[1])+","+str(values[2])+","+str(values[3])+","+str(values[4])+","+str(values[5]))
                file.write("\n")
            file.close()


            # getting user purchased items

            product_name = mydictonary[valid_id][0]
            brand_name = mydictonary[valid_id][1]
            quantity_selected_by_user = user_quantity
            unit_price = mydictonary[valid_id][2]
            selected_item_price = mydictonary[valid_id][2].replace("$",'')
            total_price = int(selected_item_price)*int(quantity_selected_by_user)

            user_purchased_laptops.append([product_name,brand_name, quantity_selected_by_user, selected_item_price, total_price])
            grand_total_price = grand_total_price + total_price
        else:
            sales_loop = False



    shipping_cost = input("Dear user do you want your laptop to be shipped?(Y/N)")

    today_date_and_time = datetime.now()
    print("\n")
    print("\t \t \t \t laptop Shop Bill ")
    print("\n")
    print("\t \t Kamalpokhari, Kathmandu / Phone No: 9817787870 ")
    print("\n")
    print("------------------------------------------------------------------------------------------------------------")
    print("laptop Details are:")
    print("------------------------------------------------------------------------------------------------------------")
    print("name of the customers:"+str(name))
    print("Contact number: "+str(phone))
    print("Date and time of purchase: "+str(today_date_and_time))
    print("------------------------------------------------------------------------------------------------------------")
    print("\n")
    print("Purchased Details are:")
    print("------------------------------------------------------------------------------------------------------------")
    print("Items Name \t\t Brand \t\t Total Quantity \t Unit Price \t\t\Total")
    for i in user_purchased_laptops:
        print(i[0],"\t",i[1],"\t",i[2],"\t\t\t",i[3],"\t\t","$",i[4])
    print("------------------------------------------------------------------------------------------------------------")

    if shipping_cost == "Y" or shipping_cost == "y":
        total = 0
        shipping_cost = 500
        for i in user_purchased_laptops:
            total+=int(i[4])
        grand_total_price = total+shipping_cost
        print("Your Shipping Cost is:", shipping_cost)
        print("Grand Total: "+str(grand_total_price))
        print("Note: Shipping cost is added to grand total")         
    else:
        total = 0
        shipping_cost = 0
        for i in user_purchased_laptops:
            total+=int(i[4])
        grand_total_price = total_price + shipping_cost
        print("Grand Total: "+str(grand_total_price)) 
          
        
    return name,phone,today_date_and_time,user_purchased_laptops,shipping_cost,grand_total_price