import re
from models import getStoreData

DEFAULT_PAGE_SIZE = 3

def matchSearch(listStoreData, searchString, listStores):
    try:
        for store in listStoreData:
            if(re.match(f'.*({searchString}).*',store['postcode'], flags=re.I)):
                listStores.insert(0, store)
            elif(re.match(f'.*({searchString}).*',store['name'], flags=re.I)):
                listStores.append(store)
    except:
        return listStores

    return listStores

def getRequestArg(request, arg):
    return request.args.get(arg)

def generateResponse(listStores, pagination):
    if len(listStores) < DEFAULT_PAGE_SIZE:
        pagination = len(listStores) 

    return {'stores': listStores[0:int(pagination)], 'offset': pagination }

def findStore(request):
    listStores = []
    searchString = getRequestArg(request, 's')
    pagination = request.args.get('offset',  type=int) or DEFAULT_PAGE_SIZE

    # In future if want to switch to db model then we can change here only
    # Reest logic will remain same
    listStoreData = getStoreData()

    if(not searchString):
        listStores = listStoreData
    else:
        listStores = matchSearch(listStoreData, searchString, listStores)
    
    return generateResponse(listStores, pagination)