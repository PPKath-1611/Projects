class store(object):
    def __init__(self):
        print("\n1. Panipuri - 20 Rs" )
        print("2. Samosa - 10 Rs" )
        print("3. Chhole - 50 Rs" )
        print("4. Bhel - 30 Rs" )
        print("5. Dahipuri - 40 Rs" )
        print("6. EXIT")

    def cust_order(self, name):
        bill = 0
        ch = 0
        p = 0
        s = 0
        d = 0
        c = 0
        b = 0 
        while True:
            order = int(input("\nEnter CHOICE : "))
            if order == 1:
                print("Panipuri - 20 Rs")
                p += 1
                bill += 20
            if order == 2:
                print("2. Samosa - 10 Rs" )
                s += 1
                bill += 10;
            if order == 3:
                print("3. Chhole - 50 Rs" )
                c += 1
                bill += 50
            if order == 4:
                print("3. Bhel - 30 Rs" )
                b += 1
                bill += 30
            if order == 5:
                print("3. Dahipuri - 40 Rs" )
                d += 1
                bill += 30
            if order == 6:
                break

        print('*' * 50)
        print("\n             Hotel Drushti           \n")
        print("*" * 50)
        print("\nCustomer Name : " + name)
        print("\n" + "*" * 50)
        print("\nItems Purchased : \n")
        if p != 0:
            print("\nPanipuri  \t" + str(p) + "p \t" , 20 * p , " Rs")
        if s != 0:
            print("\nSamosa    \t" + str(s) + "p \t" , 10 * s , " Rs")
        if c != 0:
            print("\nChole     \t" + str(c) + "p \t" , 50 * c, " Rs")
        if b != 0:
            print("\nBhel      \t" + str(b) + "p \t", 30 * b, " Rs")
        if d != 0:
            print("\nDahipuri  \t" + str(d) + "p \t", 40 * d, " Rs")
        print("\n" + '*' * 50)
        print("\nTotal Bill of " + name + " : " + str(bill) + " clRs.")
        print("\nThank you & visit again\n")
        print("*" * 50)


name = input("\nCustomer Name please : ")
print("\n Menu Card ")
message = store()
message.cust_order(name)