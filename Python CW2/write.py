#operations module
def write_buy(name, phone, today_date_and_time,user_purchased_laptops,VAT,final_total,total_with_vat):
    # today_date_and_time = datetime.now()
    with open(str(name)+str(phone)+".txt", "w") as file:
        file.write("\n")
        file.write("\t \t \t \t laptop Shop Bill ")
        file.write("\n")
        file.write("\t \t Kamalpokhari, Kathmandu / Phone No: 9817787870 ")
        file.write("\n")
        file.write("------------------------------------------------------------------------------------------------------------\n")
        file.write("laptop Details are:")
        file.write("\n")
        file.write("------------------------------------------------------------------------------------------------------------\n")
        file.write("name of the customers:"+str(name))
        file.write("\n")
        file.write("Contact number: "+str(phone))
        file.write("\n")
        file.write("Date and time of purchase: "+str(today_date_and_time))
        file.write("\n")
        file.write("------------------------------------------------------------------------------------------------------------\n")
        file.write("\n")
        file.write("Purchased Details are:")
        file.write("\n")
        file.write("------------------------------------------------------------------------------------------------------------\n")
        file.write("Items Name \t\t\t Brand \t\t Total Quantity \t\t Unit Price \t Total")
        file.write("\n")
        for i in user_purchased_laptops:
         file.write(str(i[0])+"\t\t\t"+str(i[1])+"\t\t\t"+str(i[2])+"\t\t\t"+"$"+str(i[3])+"\t\t" + "$" + str(i[4])+"\n")
        file.write("------------------------------------------------------------------------------------------------------------\n")
        file.write("\n")
        file.write("VAT Amount :"+ str(VAT))
        file.write("\n")
        file.write("Grand Total: $"+str(total_with_vat))
        file.write("\n")
        file.write("Note: VAT Amount is added to grand total"+"\n")
       





            

def write_sell(name,phone,today_date_and_time,user_purchased_laptops,shipping_cost,grand_total):
    with open(str(name)+str(phone)+".txt", "w") as file:
            file.write("\n")
            file.write("\t \t \t \t Aayusha laptop Shop ")
            file.write("\n")
            file.write("\t \t Kamalpokhari, Kathmandu / Phone No: 9817787870 ")
            file.write("\n")
            file.write("------------------------------------------------------------------------------------------------------------\n")
            file.write("laptop Details are:")
            file.write("\n")
            file.write("------------------------------------------------------------------------------------------------------------\n")
            file.write("name of the customers:"+str(name))
            file.write("\n")
            file.write("Contact number: "+str(phone))
            file.write("\n")
            file.write("Date and time of purchase: "+str(today_date_and_time))
            file.write("\n")
            file.write("------------------------------------------------------------------------------------------------------------")
            file.write("\n")
            file.write("Purchased Details are:")
            file.write("\n")
            file.write("------------------------------------------------------------------------------------------------------------\n")
            file.write("Items Name \t\t Brand \t\t Total Quantity \t\t Unit Price \t\t\tTotal")
            file.write("\n")
            for i in user_purchased_laptops:
                file.write(str(i[0])+"\t" + str(i[1])+"\t\t" + str(i[2]) + "\t\t\t\t" + str(i[3])+ "\t\t" +"$"+str(i[4])+"\n")
                file.write("\n")
            file.write("------------------------------------------------------------------------------------------------------------\n")
            file.write("\n")
            if shipping_cost == 500:
                file.write("Your Shipping Cost is:" +""+ str(shipping_cost)+"\n")
                file.write("\n")
                file.write("Grand Total: $"+str(grand_total))
                file.write("\n")
                file.write("Note: Shipping cost is added to grand total"+"\n")
            else:
                file.write("Grand Total: $"+str(grand_total))
