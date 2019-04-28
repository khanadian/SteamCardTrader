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
        name_found = False
        card_found = False
        is_card = False
        game_name = ""
        for tag in tags:
            if not(card_found and name_found):
                if tag['category'] == 'Game':
                    name_found = True;
                    game_name = tag['localized_tag_name']
                elif tag['category'] == 'item_class':
                    card_found = True
                    if tag['localized_tag_name'] == 'Trading Card':
                        is_card = True
        if is_card == True:
            ws.cell(row=r, column=col_game, value=game_name)
            ws.cell(row=r, column=col_name, value=item['name'])
            r = r+1


    
    
    
    wb.save('file.xlsx')

getInventory('76561198089894938');
