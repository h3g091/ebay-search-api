import orders

class GenerateOrders():
    def generateOrders(numberOfOrders):
        allOrders = list()
        for i in range(numberOfOrders):
            new_order = orders.Orders()
            allOrders.append(new_order.getOrderAttributes())
        
        return(allOrders)




