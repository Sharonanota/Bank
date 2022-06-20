
    
from datetime import datetime
class Student:
    def __init__ (self,fullname,age,country,school,yearofbirth,initials):
        self.fullname = fullname
        self.age = age
        self.country = country
        self.school=school
        self.yearofbirth = yearofbirth
        self.initials = initials
    
    def greet(self):
        return f"hello{self.fullname},welcome to {self.school}, how is {self.country} "
    
    def student(self):
        return f"Hello{self.fullname} you were born in {self.yearofbirth}your initials are {self.initials}"
    
class initial:
    def __init__(self,initials):
        self.initials=initials
        return f"{self.fullname[0:3]}"
    
    def year(self):
        years=2022-self.age
        return f"{self.year}" 
    
    
class Account:
    def __init__(self,accounts_name,accnts_number):
    
        self.accounts_name=accounts_name
        self.accnts_number=accnts_number
        self.transaction=100
        self.deposits=[]
        self.withdrawals=[]
        self.balance=0
        self.statement=[]
        self.loan=0
        # self.deposit_statement=""
        # self.withdraw_statement=""
    def deposit(self,amount):
               #  for self.deposit_statement in self.deposit:
        if amount <=0: 
           return f"deposit must be positive amount{amount}"
        else:
            self.balance+=amount
            now = datetime.now()
            money_transaction={
             "amount":amount,
             "time":now,
             "Narration": "You have deposited"

         }
            self.statement.append(money_transaction)
            self.deposits.append(f"you have deposited {amount}")
            return f"Hello {self.accounts_name} you have deposited {amount} so your balance is {self.balance} and your statement is {self.statement}"  
    
    
    
    def withdrw(self,amount):

        if  amount>self.balance:
             return f"your balance is {self.balance}you can't witdraw{amount}"
          
        elif amount+self.transaction>self.balance:
            return f"no sufficient funds" 
            
        elif amount <=0:
           return f"withdraw should be greater than zero"
        
        else:
            self.balance -= amount+ self.transaction
            now = datetime.now()
            money_transactions={
             "amount":amount,
             "time":now,
             "Narration": "You have withdrawn"

         }
            self.withdrawals.append(amount)
            self.statement.append(money_transactions)
            
            self.withdrawals.append(f"you have withdrawn {amount}")
           
            return f"hello {self.accounts_name},you have withdrawn {amount} at and your new balance is {self.balance} and your statement{self.statement}"
        
    def deposit_statement(self):
        for m in self.deposits:
            print  (m)  
            
    def withdrw_statement (self):
        for n in self.withdrawals:
            print(n)  
            
 #Modify the withdrawal method to include a transaction fee of 100 per transaction.
 #Add a method to show the current balance.
    def current_balance(self):
        balance=self.balance
        print(balance)
        
    def full_statement(self):
        for money_transaction in self.statement:
            amount=money_transaction["amount"]
            Narration=money_transaction["Narration"]
            time=money_transaction["time"]
            date=time.strftime("%x/%X")
            print(f"{date}: {Narration} {amount}")
    

    def loan(self,amount):
    
        item =len(self.deposits)
        items=sum(self.deposits)
        limit=items*(1/3)
        amount+=(amount)*0.03
        
        if amount<=100:
            return f"sorry we can't give you loan go away"
            
        elif self.loan>0:
            return f"Dear customer sorry you have 0{self.loan}" 
        
        elif item<10:
            return f"your deposit must be atleast 10"  
        
        elif amount>=limit:
            return f"Dear customer you can't borrow {amount} is higher than limit of {self.balance}"
        else:
            self.loan+=amount
            return f"Dear customer {self.accounts_name} your loan of ksh {amount} has been granted successfully"
        
    def loan_repay(self,amount):
        if amount<self.loan:
            paying = self.loan-amount
            return f"Dear customer you have paid {amount} and your loan is {paying}"
        else:
          over_pay = amount-self.loan
          self.balance+=over_pay
          return f"You successfully completed paying your loan and the over pap is {over_pay} and your new balance is {self.balance}"
    def transfer(self,amount,account):
        fee=amount*0.05
        Total=fee+amount
        if amount<0:
            return f"Dear customer {self.accounts_name}your amount is too low"
        elif Total>self.balance:
            return f"Dear customer {self.accounts_name} your balance is {self.balance} and you need atleast {Total}"
        else:
            self.balance-=Total
            return f"Dear customer you have sent {amount} to {account} and your new balance is {self.balance}"
        
        

            
            
        
               
             
           

    
            
 
               
        
        
    
            
     
          
            
        
          
    
        