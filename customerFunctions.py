#this class is to build my own customer class with some attrubutes

class Customers:
    
    def __init__(self,surname,lastname,customer_id, adress,age, sex):
        # this method initializes a customer with the neccessary attributes
        self.name = surname + " " + lastname
        self.adress = adress
        self.age = age  
        self.sex = sex
        self.customer_id = customer_id

        self.numberOfPurchases = 0
        self.totalRevenue = 0

    def getStats(self):
        print(self.name, self.adress, self.sex, self.numberOfPurchases, self.totalRevenue)
        return(list[self.name, self.adress, self.sex, self.numberOfPurchases, self.totalRevenue])
    
    def addPurchase(self, revenue):
        self.totalRevenue = self.totalRevenue + revenue
        self.numberOfPurchases = self.numberOfPurchases + 1

    
        

