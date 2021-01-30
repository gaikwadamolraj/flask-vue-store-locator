import json
listStoreData = []
with open('static/storeData.json', 'r') as f:
       listStoreData = json.loads(f.read())
print('Data loaded!!!!')
def getStoreData():
    return listStoreData
    