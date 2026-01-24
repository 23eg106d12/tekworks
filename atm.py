class Bank:
    acbal=10000
    def withdraw(self):
        amt=int(input("Enter your withdraw amount :"))
        if amt%100==0:
            if amt<=20000:
                if amt<=self.acbal:
                    self.acbal=self.acbal-amt
                    print("Available bal : ",self.acbal)
                    five = amt // 500
                    amt -= five * 500
                    two = amt // 200
                    amt -= two * 200
                    one = amt // 100

                    print("Currency notes dispensed:")
                    print(f"500: {five}, 200: {two}, 100: {one}")
                else:
                    print("insuffient fund")
            else:
                print("withdraw limit is 20k only")
        else:
            print("Please enter multiples of 100 only")
    def deposite(self):
        
        amt=int(input("Enter your deposite amount:  "))
        if amt%100==0:
            self.acbal=self.acbal+amt
        else:
            print("Please enter multiples of 100 only")
        print("Avalaible bal :",self.acbal)
    def viewOptions(self):
        transactions=0
        while True:
            print("1. deposite")
            print("2. withdraw")
            print("3. bal Enquiry")
            print("0. EXIT")
            option=int(input("Choose your option: "))
            if option==1:
                obj.deposite()
                transactions+=1
            elif option==2:
                obj.withdraw()
                transactions+=1
            elif option==3:
                print("Bal Enquiry")
                transactions+=1
            elif option==0:
                print("Thank you, visit again")
                break
            else:
                print("Invalid option")
                continue

            if transactions==3:
                print("Transactions Limit reached")
                break
            else:
                print("Would you like to continue :")
                print("1.yes")
                print("2.no")
                con=int(input(""))
                if con==1:
                    pass
                elif con==2:
                    print("Thank you, visit again")
                    break

obj=Bank()
obj.viewOptions()
  