Table_No = int(input("Enter Table No "))
tea_Quantity=int(input("Enter Tea Quantity "))
coffee_Quantity=int(input("Enter Coffee Quantity "))
class Shop:
    def __init__(self):
        self.tea=10
        self.coffee=15
    def tea_discount(self,tea_Quantity):
        self.tea_price=self.tea*tea_Quantity
        self.tea_discount=(self.tea_price*10)/100
    def coffee_discount(self,coffee_Quantity):
        self.coffee_price=self.coffee*coffee_Quantity
        self.coffee_discount=(self.coffee_price*15)/100
        self.total_price=self.tea_price+self.coffee_price
        self.total_discount=self.tea_discount+self.coffee_discount
        self.final_price=self.total_price-self.total_discount
    def display(self):
        print()
        print("--------------------Coffee Shop--------------------")
        print("")
        print("")
        print("Table No                                         ",Table_No)
        print(f"Tea Quantity                                      {tea_Quantity}")
        print(f"Coffee Quantity                                   {coffee_Quantity}")
        print(f"Total Discount                              {self.total_price-self.final_price} INR")
        print("---------------------------------------------------")
        print(f"Bill Amount                                {self.final_price} INR")
        print()
        print("---------------Thank You For Visiting--------------")
ob=Shop()
ob.tea_discount(tea_Quantity)
ob.coffee_discount(coffee_Quantity)
ob.display()

Add_More=input("ADD MORE ITEMS - Y/N - ")

if Add_More == "Y":

    add_tea=int(input("Addon Tea Quantity "))
    add_coffee=int(input("Addon Coffee Quantity "))

    if add_tea > 0 or add_coffee > 0:
        class Shop:
            def __init__(self):
                self.tea=10
                self.coffee=15
            def tea_discount(self,tea_Quantity,add_tea):
                self.tea_price1=self.tea*tea_Quantity
                self.tea_price2=self.tea*add_tea
                self.tea_discount=(self.tea_price1*10)/100
            def coffee_discount(self,coffee_Quantity,add_coffee):
                self.coffee_price1=self.coffee*coffee_Quantity
                self.coffee_price2=self.coffee*add_coffee
                self.coffee_discount=(self.coffee_price1*15)/100
                self.total_price=self.tea_price1+self.coffee_price1+self.tea_price2+self.coffee_price2
                self.total_discount=self.tea_discount+self.coffee_discount
                self.final_price=self.total_price-self.total_discount
            def display(self):
                    print() 
                    print("****************Generating New Bill****************")
                    print()
                    print("--------------------Coffee Shop--------------------")
                    print("")
                    print("")
                    print("Table No                                         ",Table_No)
                    print(f"Tea Quantity                                      {tea_Quantity+add_tea}")
                    print(f"Coffee Quantity                                   {coffee_Quantity+add_coffee}")
                    print(f"Total Discount                              {self.total_price-self.final_price} INR")
                    print("---------------------------------------------------")
                    print(f"Bill Amount                                {self.final_price} INR")
                    print()
                    print("---------------Thank You For Visiting--------------")
                    print()
                    print("PRINTING...")
        ob=Shop()
        ob.tea_discount(tea_Quantity,add_tea)
        ob.coffee_discount(coffee_Quantity,add_coffee)
        ob.display()
    else:
        print()
        print("PRINTING...")
elif (Add_More=="N"):
    print()
    print("PRINTING...")
else:
    print()
    print("PRINTING...")
