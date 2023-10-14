import requests
import json
import helper
url = 'http://prices.runescape.wiki/api/v1/osrs/latest'
headers = {
    'User-Agent': 'Potion decanting checker - Written by Rugg @ Discord Rugg#4267'
}
params = {}
response = requests.get(url, headers=headers, params=params)
responseJson = json.loads(response.content)

url = 'http://prices.runescape.wiki/api/v1/osrs/1h'
response = requests.get(url, headers=headers, params=params)
volumeJson = json.loads(response.content)


mapping = helper.get_mapping()
itemIds = helper.get_name_to_id_mapping(mapping)


items = {
    "Extended super antifire": {
        4: "Extended super antifire(4)",
        3: "Extended super antifire(3)",
        2: "Extended super antifire(2)",
        1: "Extended super antifire(1)",
    },
    "Divine super combat potion": {
        4: "Super combat potion(4)",
        3: "Super combat potion(3)",
        2: "Super combat potion(2)",
        1: "Super combat potion(1)",
    },
    "Anti-venom+": {
        4: "Anti-venom+(4)",
        3: "Anti-venom+(3)",
        2: "Anti-venom+(2)",
        1: "Anti-venom+(1)",
    },
    "Super antifire potion": {
        4: "Super antifire potion(4)",
        3: "Super antifire potion(3)",
        2: "Super antifire potion(2)",
        1: "Super antifire potion(1)",
    },
    "Super combat potion": {
        4: "Super combat potion(4)",
        3: "Super combat potion(3)",
        2: "Super combat potion(2)",
        1: "Super combat potion(1)",
    },
    "Anti-venom": {
        4: "Anti-venom(4)",
        3: "Anti-venom(3)",
        2: "Anti-venom(2)",
        1: "Anti-venom(1)",
    },
    "Extended antifire": {
        4: "Extended antifire(4)",
        3: "Extended antifire(3)",
        2: "Extended antifire(2)",
        1: "Extended antifire(1)",
    },
    "Saradomin brew": {
        4: "Saradomin brew(4)",
        3: "Saradomin brew(3)",
        2: "Saradomin brew(2)",
        1: "Saradomin brew(1)",
    },
    "Battlemage potion": {
        4: "Battlemage potion(4)",
        3: "Battlemage potion(3)",
        2: "Battlemage potion(2)",
        1: "Battlemage potion(1)",
    },
    "Bastion potion": {
        4: "Bastion potion(4)",
        3: "Bastion potion(3)",
        2: "Bastion potion(2)",
        1: "Bastion potion(1)",
    },
    "Antidote++": {
        4: "Antidote++(4)",
        3: "Antidote++(3)",
        2: "Antidote++(2)",
        1: "Antidote++(1)",
    },
    "Divine magic potion": {
        4: "Divine magic potion(4)",
        3: "Divine magic potion(3)",
        2: "Divine magic potion(2)",
        1: "Divine magic potion(1)",
    },
    "Zamorak brew": {
        4: "Zamorak brew(4)",
        3: "Zamorak brew(3)",
        2: "Zamorak brew(2)",
        1: "Zamorak brew(1)",
    },
    "Stamina potion": {
        4: "Stamina potion(4)",
        3: "Stamina potion(3)",
        2: "Stamina potion(2)",
        1: "Stamina potion(1)",
    },
    "Magic potion": {
        4: "Magic potion(4)",
        3: "Magic potion(3)",
        2: "Magic potion(2)",
        1: "Magic potion(1)",
    },
    "Divine ranging potion": {
        4: "Divine ranging potion(4)",
        3: "Divine ranging potion(3)",
        2: "Divine ranging potion(2)",
        1: "Divine ranging potion(1)"
    },
    "Ranging potion": {
        4: "Ranging potion(4)",
        3: "Ranging potion(3)",
        2: "Ranging potion(2)",
        1: "Ranging potion(1)",
    },
    "Divine super strength potion": {
        4: "Divine super strength potion(4)",
        3: "Divine super strength potion(3)",
        2: "Divine super strength potion(2)",
        1: "Divine super strength potion(1)"
    },
    "Divine super defence potion": {
        4: "Divine super defence potion(4)",
        3: "Divine super defence potion(3)",
        2: "Divine super defence potion(2)",
        1: "Divine super defence potion(1)",
    },
    "Divine super attack potion": {
        4: "Divine super attack potion(4)",
        3: "Divine super attack potion(3)",
        2: "Divine super attack potion(2)",
        1: "Divine super attack potion(1)",
    },
    "Antifire potion": {
        4: "Antifire potion(4)",
        3: "Antifire potion(3)",
        2: "Antifire potion(2)",
        1: "Antifire potion(1)",
    },
    "Antidote+": {
        4: "Antidote+(4)",
        3: "Antidote+(3)",
        2: "Antidote+(2)",
        1: "Antidote+(1)",
    },
    "Super defence": {
        4: "Super defence(4)",
        3: "Super defence(3)",
        2: "Super defence(2)",
        1: "Super defence(1)",
    },
    "Sanfew serum": {
        4: "Sanfew serum(4)",
        3: "Sanfew serum(3)",
        2: "Sanfew serum(2)",
        1: "Sanfew serum(1)",
    },
    "Super restore": {
        4: "Super restore(4)",
        3: "Super restore(3)",
        2: "Super restore(2)",
        1: "Super restore(1)",
    },
    "Super strength": {
        4: "Super strength(4)",
        3: "Super strength(3)",
        2: "Super strength(2)",
        1: "Super strength(1)",
    },
    "Super energy": {
        4: "Super energy(4)",
        3: "Super energy(3)",
        2: "Super energy(2)",
        1: "Super energy(1)",
    },
    "Super attack": {
        4: "Super attack(4)",
        3: "Super attack(3)",
        2: "Super attack(2)",
        1: "Super attack(1)",
    },
    "Prayer potion": {
        4: "Prayer potion(4)",
        3: "Prayer potion(3)",
        2: "Prayer potion(2)",
        1: "Prayer potion(1)",
    },
    "Energy potion": {
        4: "Energy potion(4)",
        3: "Energy potion(3)",
        2: "Energy potion(2)",
        1: "Energy potion(1)",
    },
    "Restore potion": {
        4: "Restore potion(4)",
        3: "Restore potion(3)",
        2: "Restore potion(2)",
        1: "Restore potion(1)",
    },
    "Menaphite remedy": {
        4: "Menaphite remedy(4)",
        3: "Menaphite remedy(3)",
        2: "Menaphite remedy(2)",
        1: "Menaphite remedy(1)",
    },
    "Ancient brew": {
        4: "Ancient brew(4)",
        3: "Ancient brew(3)",
        2: "Ancient brew(2)",
        1: "Ancient brew(1)",
    },
    "Forgotten brew": {
        4: "Forgotten brew(4)",
        3: "Forgotten brew(3)",
        2: "Forgotten brew(2)",
        1: "Forgotten brew(1)",
    },

}

def getTaxedPrice(listPrice):
    if listPrice < 100:
        return listPrice
    else:
        return min(5_000_000, listPrice - (0.01*listPrice))

mapping = helper.get_mapping()
latestPrices = helper.get_latest_prices()
name_to_id = helper.get_name_to_id_mapping(mapping)
hour_prices = helper.get_1h_prices()

def getMostProfitablePotionDecants():
    profits = []
    for itemGeneralName, subItemDict in items.items():
        for buyDoseCount, buyItemName in subItemDict.items():
                buyItemId = name_to_id[buyItemName]
                for sellDoseCount, sellItemName in subItemDict.items():
                    sellItemId = name_to_id[sellItemName]
                    if not(str(buyItemId) in latestPrices and str(sellItemId) in latestPrices):
                        continue
                    priceBuy = latestPrices[str(buyItemId)]['low']
                    priceSell= latestPrices[str(buyItemId)]['high']
                    buyPricePerDose = priceBuy / buyDoseCount
                    sellPricePerDose = getTaxedPrice(priceSell) / sellDoseCount
                    profitMultiplier = sellPricePerDose / buyPricePerDose
                    
                    if((buyPricePerDose < sellPricePerDose) 
                        and str(buyItemId) in hour_prices 
                        and hour_prices[str(buyItemId)]['highPriceVolume'] > 50
                        and str(sellItemId) in hour_prices
                        and hour_prices[str(sellItemId)]['highPriceVolume'] > 50):
                        profits.append({
                            'name': itemGeneralName,
                            'dose1': buyDoseCount,
                            'dose2' : sellDoseCount,
                            'profitMultiplier': profitMultiplier,
                            'buy': priceBuy,
                            'sell': priceSell,
                            'buyPerDose': buyPricePerDose,
                            'sellPerDose': sellPricePerDose
                        })
                        #print(itemGeneralName, dose1, dose2, profitMultiplier)
    sorted_profits = sorted(profits, key=lambda x: x['profitMultiplier'], reverse=True)
    for item in sorted_profits:
        print(item)

def getMostEfficientPotion(genericPotionName: str):
    if not genericPotionName in items:
        print("Item not found")
        return
    print(f'Most efficient potion for {genericPotionName}')
    prices = []
    for dose, name in items[genericPotionName].items():
        id = name_to_id[name]
        price = latestPrices[str(id)]['high'] 
        pricePerDoseHigh = price / dose
        price_to_add = {
            'dose': dose,
            'price': price,
            'price_per_dose': pricePerDoseHigh,
            'high_price_volume': hour_prices[str(id)]['highPriceVolume'] if str(id) in hour_prices else 0
        }
        prices.append(price_to_add)
    totalVolume = 0
    for price in prices:
        totalVolume += price['high_price_volume']
    sorted_prices = sorted(prices, key=lambda x: x['price_per_dose'], reverse = True)
    for price in sorted_prices:
        print(price)


#getMostEfficientPotion("Menaphite remedy")
getMostProfitablePotionDecants()
'''
for i in items:
    volumeData = None 
    if(str(itemIds[items[i][4]]) in volumeJson['data']):
            volumeData = volumeJson['data'][str(itemIds[items[i][4]])]
    if(volumeData is None or 'lowPriceVolume' not in volumeData or volumeData['lowPriceVolume'] < 2000 or volumeData['highPriceVolume'] < 2000):
        continue
    fourHigh = responseJson['data'][str(itemIds[items[i][4]])]['high']
    fourHigh = getTaxedPrice(fourHigh)
    #fourHigh = (0.01 * fourHigh)
    for j in range(1,4):
        priceLow = responseJson['data'][str(itemIds[items[i][j]])]['high']
        #print(responseJson['data'][str(itemIds[items[i][j]])])
        volumeData = None
        if(str(itemIds[items[i][j]]) in volumeJson['data']):
            volumeData = volumeJson['data'][str(itemIds[items[i][j]])]
        if(volumeData is None or 'lowPriceVolume' not in volumeData or volumeData['lowPriceVolume'] < 10 or volumeData['highPriceVolume'] < 150):
            continue
        fourDoseMultiplier = 4/j
        priceForFourDose = priceLow * fourDoseMultiplier
        #print(priceForFourDose)
        if(priceForFourDose < fourHigh):
            #print(volumeData)
            print("\t{dose} dose of {item} might be worth it: {profit}".format(dose = j, item = i, profit = int(fourHigh-priceForFourDose)))
'''