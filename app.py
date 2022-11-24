from ticket_macine import  medicine_calc
from ticket_macine import  perfum_calc
from ticket_macine import  cosmotics_calc
from  utils import time_counter


def app():
    Type_of_product = """ list of products:
    1. perfume
    2. cosmotics
    3. medicine"""
    print(" ******************Welcom to our  drug store**************************")
    toda_list = [123456,14789]
    count = 0
    count_limit = 3
    while count_limit > count:
        Toda = int(input("please enter your id: "))
        if Toda in toda_list:
            print(Type_of_product)
            order = input("please choose your product area from Type_of_product: ")
            while True:
                if order == "cosmotics" or order == "perfume" or order == "medicine":
                    print("your number is")
                    cosmotics_calc(order)
                    perfum_calc(order)
                    medicine_calc(order)
                    print("Please wait and someone will assist you shortly.")
                    permission = input("do you want continue? y/n")
                    if permission == "y" or permission == "Y":
                        order = input("please choose your product area from list: ")
                    else:
                        exit(0)
                else:
                    order = input("please choose your product area from Type_of_product: ")
        else:
            print("please try again")
        count += 1
    else:
        times = int(input("enter your time: "))
        time_counter(times)