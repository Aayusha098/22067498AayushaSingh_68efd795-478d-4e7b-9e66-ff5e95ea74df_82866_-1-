def readtxtfile():
    file = open("laptop.txt","r")
    laptopid =1
    mydictonary={}


    for line in file:
        line = line.replace("\n","")
        mydictonary[laptopid]=line.split(",")

        mydictonary.update({laptopid:line.split(",")})
        laptopid+=1

    file.close()
    return mydictonary