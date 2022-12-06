import pandas as pd
from IPython import display

class Catalog:
    def __init__(self):
        self.productCatalog = pd.DataFrame(
            {"prodID" : [1,2,3],
            "Beschreibung": ["Seil", "Exen", "Hosen"],
            "Kosten": [100,50,80]},
            index= [1,2,3]   
        )
    def displayCatalog(self):
        print(self.productCatalog)



