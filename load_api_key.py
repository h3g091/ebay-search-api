#this module is just to load the api key out of my .env file

import datetime

import os
from ebaysdk.finding import Connection 
from ebaysdk.exception import ConnectionError
from dotenv import load_dotenv
load_dotenv()
API_KEY= os.getenv('api_key')


class Ebay_22(object):
    def __init__(self, API_KEY):
        self.api_key = API_KEY
    
    def fetch(self):
        try:
            # the domain is on the sandbox version!! not the production sandbox is just for testing 
            api = Connection(domain = 'svcs.sandbox.ebay.com',appid=self.api_key, config_file=None)
            response = api.execute('findItemsAdvanced', {'keywords': 'legos'})
            print (response.reply)
            # print the results of the response list
            for item in response.reply.searchResult.item:
                print(f"Title: {item.title}, Price: {item.sellingStatus.currentPrice.value}")
                print(f"Condition: {item.condition.conditionDisplayName}")
                print(f"Buy it now available: {item.listingInfo.buyItNowAvailable}")
                print(f"Product ID: {item.productId}")
            
            assert(response.reply.ack == 'Success')
            assert(type(response.reply.timestamp) == datetime.datetime)
            assert(type(response.reply.searchResult.item) == list)

            item = response.reply.searchResult.item[0]
            assert(type(item.listingInfo.endTime) == datetime.datetime)
            assert(type(response.dict()) == dict)

        except ConnectionError as e:
            print(e)
            print(e.response.dict())


    def parse(self):
        pass


#main driver

if __name__ == '__main__':
    e = Ebay_22(API_KEY)
    e.fetch()
    e.parse()


