import urllib.request
import json
import pprint

#https://stackoverflow.com/questions/29824111/get-a-users-steam-inventory
def getInventory(steamid):
    data = urllib.request.urlopen('http://steamcommunity.com/inventory/'+steamid+'/753/6')
    json_data = json.loads(data.read())
    descriptions = json_data['descriptions']
    amounts = json_data['assets']
    for key in descriptions:
        print(key['market_hash_name'])
    print ('Done!')
    #return

getInventory('76561198089894938');
