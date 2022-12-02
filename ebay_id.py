
ebay_id = "HeikoLan-searchan-SBX-da27d63e4-e57a2caf"

from ensurepip import version
#from msilib.schema import AppId
from urllib import response
import pandas as pd 
import os
# dotenv is used to create hidden files .env files - here a .env file contains api_key
from dotenv import load_dotenv

from ebaysdk.finding import Connection as Finding
from ebaysdk.exception import ConnectionError
print('all neccessary module loaded')

print(os.getcwd())

# hide id in a .env file
APPLICATION_ID = os.environ.get('API_KEY')
APPLICATION_ID= 'HeikoLan-searchan-SBX-da27d63e4-e57a2caf'
print(APPLICATION_ID)

# set deprication for showing
pd.set_option('display.max_rows', 500)


# function to get the payload
def get_results(payload):
    try:
        api = Finding(siteid="EBAY-DE", appid = APPLICATION_ID, config_file = None)
        response= api.execute('findItemsAdvanced', payload)
        return response.dict()

    except ConnectionError as e:
            print(e)
            print(e.response)



# define payload for search

payload = {
    #search for Samsung
    'keywords':'Samsung',
    'categoryId':['80053'],
    'itemFilter':[
        {'name': 'LocatedIn', 'value': 'EU'},
    ],
    'sortOrder' : 'StartTimeNewest',    
}


# get results

results = get_results(payload)