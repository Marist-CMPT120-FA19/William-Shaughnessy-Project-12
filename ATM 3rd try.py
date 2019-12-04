class Account:

    def __init__(self,id,pin,checking,savings):
        self.ID = id
        self.PIN = pin
        self.checking = checking
        self.savings = savings

    def get_ID(self):
        return self.ID

    def get_PIN(self):
        return self.PIN
   
    def get_Save(self):
        return self.savings

    def get_Check(self):
        return self.checking

    def withdraw(self,amount,type): 
        if(type==1):
            if(self.savings<amount):
              print("Insuficcent funds")
        else:
              self.savings -= amount
        if(type==2):
            if(self.checking<amount):
                print("Insuficcent funds")
        else:
                self.checking -= amount
        return True

    def deposit(self,amount,type):
        if(type==1):
            self.savings += amount
        elif(type==2):
            self.checking += amount
        return True

def main():
    account = []
    n=0

    with open("accounts.txt") as file: 
        for line in file: 
            acct = line.split(" ") 
            account.append(Account(acct[0],acct[1],float(acct[2]),float(acct[3].replace('\n', " "))))
            n += 1 

    id = input("please enter ID number: ")
    pin = input("please enter PIN: ")
    i=0

    while i<n:
        if(account[i].get_ID()==id):
            if(account[i].get_PIN()==pin):
                option = int(input('Enter (1) for withdraw (2) for deposit (3) for transfer (4) for balance: '))
                if(option==1):
                    type = int(input('Select account to withdraw from 1.Savings 2.Checking: '))
                    amount = float(input("Enter amount to withdraw: "))
                    if(account[i].withdraw(amount,type)):
                        if(type==1):
                            print(amount,'Funds withdrawn. Closing balance: ',account[i].get_Save())
                        elif(type==2):
                            print(amount,'Funds withdrawn. Closing balance: ',account[i].get_Check())
                    else:
                        print('insufficient funds')
                elif(option==2):
                    type = int(input('Select account to deposit into (1) Savings (2) Checking: '))
                    amount = float(input("Enter amount to deposit: "))
                    if(account[i].deposit(amount,type)):
                        if(type==1):
                            print(amount,'Funds deposited. Closing balance: ',account[i].get_Save())
                        elif(type==2):
                            print(amount,'Funds deposited. Closing balance: ',account[i].get_Check())
                elif(option==3):
                        trans = int(input('Enter (1) transfer from savings to checking (2) transfer from checking to savings: '))
                        amount = float(input('Enter amount to transfer: '))
                        if(trans==1):
                            account[i].withdraw(amount,1)
                            account[i].deposit(amount,2)
                            print('Successful transfer from savings to checking. Closing balance: ', account[i].get_Check())
                elif(trans==2):
                            account[i].withdraw(amount,2)
                            account[i].deposit(amount,1)
                            print('Successful transfer from checking to savings. Closing balance: ', account[i].get_Save())
                else:
                    type = int(input('Select type (1) Savings (2) Checking: '))
                    if(type==1):
                        print('Your savings balance:',account[i].get_Save())
                    elif(type==2):
                        print('Your checking balance:',account[i].get_Check())
                break
        i += 1

    if(i==n): 
        print('invalid login')
    else:
        file = open('accountinfo.txt','w')
        j=0
        while j<n:
            file.write(account[j].get_ID()+' '+account[j].get_PIN()+' '+str(account[j].get_Check())+' '+str(account[j].get_Save())+' ')
            j += 1
    file.close() 
    print('Thank youHave a nice day.')

main()
