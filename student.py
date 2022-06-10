
    
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
        return f"{self.age}" 
    
    
class Account:
    def __init__(self,accounts_name,accnts_number):
    
        self.accounts_name=accounts_name
        self.accnts_number=accnts_number
        self.transaction=100
        self.deposits=[]
        self.withdrawals=[]
        self.balance=0
        # self.deposit_statement=""
        # self.withdraw_statement=""
    def deposit(self,amount):
    #  for self.deposit_statement in self.deposit:
        if amount <=0:
            
           return f"deposit must be positive amount{amount}"
        else:
         self.balance+=amount
         self.deposits.append(f"you have deposited {amount}")
        return f"Hello {self.accounts_name} you have deposited {amount} so your balance is {self.balance}"  
    
    
    
    def withdrw(self,amount):
    
        if  amount>self.balance:
              return f"your balance is {self.balance},you can't witdraw{amount}"
            
        elif amount <=0:
           return f"withdraw should be greater than zero"
        
        else:
            self.balance -= amount+ self.transaction
            self.withdrawals.append(f"you have withdrawn {amount}")
           
            return f"hello {self.accounts_name},you have withdrawn {amount}.and your new balance is {self.balance}"
        
    def deposit_statement(self):
        for m in self.deposits:
            print  (m)  
            
    def withdrawals_statement (self):
        for n in self.withdrawals:
            print(n)  
            
 #Modify the withdrawal method to include a transaction fee of 100 per transaction.
 #Add a method to show the current balance.
    def current_balance(self):
        balance=self.balance
        print(balance)
 
               
        
        
    
            
     
          
            
        
          
    
        