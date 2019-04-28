import urllib.request
import json
import pprint
import openpyxl
from openpyxl import Workbook


#https://stackoverflow.com/questions/29824111/get-a-users-steam-inventory
def getInventory(steamid):
    data = urllib.request.urlopen('http://steamcommunity.com/inventory/'+steamid+'/753/6')
    json_data = json.loads(data.read())
    descriptions = json_data['descriptions']
    assets = json_data['assets']
    
        #print(item['market_hash_name'])
    writeToExcel(assets, descriptions)
    print ('Done!')
    #return

def writeToExcel(assets, descriptions):
    wb = Workbook() 
    ws = wb.active

    r = 1
    col_name = 1
    col_ID = 3
    col_game = 2
    ws.cell(row=r, column=col_game, value='Game')
    ws.cell(row=r, column=col_name, value='Name')
    r = r+1
    for item in descriptions: #item is a dict of one description
        tags = item['tags']
        if(len(tags) == 4):
            is_card = False
            game_tag = tags[1]
            class_tag = tags[3]
            if class_tag['localized_tag_name'] == 'Trading Card':
                is_card = True
            if is_card:
                game_name = game_tag['localized_tag_name']
                ws.cell(row=r, column=col_game, value=game_name)
                ws.cell(row=r, column=col_name, value=item['name'])
                r = r+1


    wb.save('file.xlsx')

getInventory('76561198089894938');
