#this class generates random orders to fill up my df
import random
import productCatalog
import datetime



numberOfItemsInCatalog = len(productCatalog.Catalog().productCatalog)

class Orders:
    
    def __init__(self):
        self.customer_id = "cus_"+  str(random.randint(0,10))
        #self.purchasedProduct = productCatalog.Catalog().productCatalog.iloc[random.randint(0,numberOfItemsInCatalog-1)]
        self.purchasedProduct = random.randint(0,numberOfItemsInCatalog-1)
        self.timeStamp = datetime.datetime.now()
    
    def getOrderAttributes(self):
        return ([self.customer_id, self.purchasedProduct,self.timeStamp])



