from operation import *
from write import *


print("\n")
print("---------------------------------------------------------------")
print("\t \t Welcome to C1")
print("---------------------------------------------------------------")
print("\t \t Address: BSL Contact: 9819770701")
print("---------------------------------------------------------------")
print("\n")


continueLoop = True
while continueLoop == True:

    print("\n")
    print("Press 1 to buy from manufacturer")
    print("Press 2 to sell to customer")
    print("Press 3 to exit")
    print("\n")
    print("---------------------------------------------------------------")
    userinput=0
    try:
        userinput = int(input("Press 1,2 or 3 :"))
        print("\n")
        option = False
    except:
        print("Please enter valid input 1,2,3 only")



    if userinput == 1:
        name, phone, today_date_and_time,user_purchased_laptops,VAT,final_total,total_with_vat = purchase_laptops()
        write_buy(name, phone, today_date_and_time,user_purchased_laptops,VAT,final_total,total_with_vat)

            
    elif userinput==2:
        name,phone,today_date_and_time,user_purchased_laptops,shipping_cost,grand_total_price = sold_laptops()
        write_sell(name,phone,today_date_and_time,user_purchased_laptops,shipping_cost,grand_total_price)

        
    elif userinput==3:
        continueLoop = False
        print("Thank you  for Visiting")
    else:
        print("Please Enter correct option")
