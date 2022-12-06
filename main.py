import customerFunctions
import random
import pandas as pd
import generateFakeOrders
import numpy
import productCatalog

numberFake_orders = 50
orders = generateFakeOrders.GenerateOrders.generateOrders(numberFake_orders)

catalog = productCatalog.Catalog()

catalog.displayCatalog()

ordersDf = pd.DataFrame(orders, columns=['cusID','prodID','tstamp'])
print(ordersDf)
# next steps - join df catalog with orders and create a new one that has revenue in it etc and total number of orders..
print(ordersDf[ordersDf.prodID == 1])