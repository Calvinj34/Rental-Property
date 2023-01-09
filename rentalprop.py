class ROI:
    def __init__(self) -> None:
        self.sum= None
        self.expense= None
        self.income = None
        self.tmd = None

    def getincome(self):
       rental_income = int(input("what is your monthly rent charge going to be? "))
       laundry= int(input("what is your monthly laundry charge? "))
       storage =int(input("what is your monthly storage charge? "))
       misc = int(input("what is your monthly misc charge? "))
       mi= (rental_income+laundry+storage+misc)
       self.income= mi
       print(f'you will make ${self.income} a month from this')
       
    

    
    def expenses(self):
        taxes = int(input("how much are taxes? "))
        insurance= int(input("what is your Insurance charge? "))
        utilities =int(input("how much are utilities? "))
        mortgage = int(input("what is the mortgage cost? "))
        repairs = int(input("what is the cost of repairs and capx you budgeted? "))
        propmang = int(input("what is the cost for your property manager? "))
        self.expense = (taxes+insurance+utilities+ mortgage+ repairs+ propmang)
        print(f'you will pay ${self.expense} a month from this')
       
    def cashflow(self):
        self.tmd = (self.expense-self.income)
       

    def annualcash(self):
        downpayment = int(input("how much are you putting down? "))
        cc= int(input("how much are the closing cost? "))
        rehab= int(input("what is your rehab budget? "))
        ti = (downpayment) +(cc) +(rehab)
        
        self.cashflow()
        cash = (self.tmd/ti)*100
        print(f' your ROI on this property is {round(cash,2)} %. ')
        

        
    def run(self):
        info = input("do you want to find the ROI? or enter Q to quit")
        while info != 'Q':
            if info:
                self.getincome()
                self.expenses()
                self.annualcash()
                break

r= ROI()
r.run()
    