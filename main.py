import customerFunctions
import random
import pandas
from IPython import display
import numpy
A = customerFunctions.Customers("Heiko", "Langer", "1","Street1", "23", "m")

#print(A.name)

all_stats = A.getStats()
print(all_stats)

A.addPurchase(250)

A.addPurchase(random.randint(0,10000))

A.getStats()

import productCatalog 

B = productCatalog.Catalog()

print(B.productCatalog)

