import requests
import json
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

with open('./items.txt', 'r') as myfile:
    data = myfile.read()
itemIds = json.loads(data)

items = {
    "Extended super antifire": {
        4: "Extended super antifire(4)",
        3: "Extended super antifire(3)",
        2: "Extended super antifire(2)",
        1: "Extended super antifire(1)"
    },
    "Divine super combat potion": {
        4: "Super combat potion(4)",
        3: "Super combat potion(3)",
        2: "Super combat potion(2)",
        1: "Super combat potion(1)"
    },
    "Anti-venom+": {
        4: "Anti-venom+(4)",
        3: "Anti-venom+(3)",
        2: "Anti-venom+(2)",
        1: "Anti-venom+(1)"
    },
    "Super antifire potion": {
        4: "Super antifire potion(4)",
        3: "Super antifire potion(3)",
        2: "Super antifire potion(2)",
        1: "Super antifire potion(1)"
    },
    "Super combat potion": {
        4: "Super combat potion(4)",
        3: "Super combat potion(3)",
        2: "Super combat potion(2)",
        1: "Super combat potion(1)"
    },
    "Anti-venom": {
        4: "Anti-venom(4)",
        3: "Anti-venom(3)",
        2: "Anti-venom(2)",
        1: "Anti-venom(1)"
    },
    "Extended antifire": {
        4: "Extended antifire(4)",
        3: "Extended antifire(3)",
        2: "Extended antifire(2)",
        1: "Extended antifire(1)"
    },
    "Saradomin brew": {
        4: "Saradomin brew(4)",
        3: "Saradomin brew(3)",
        2: "Saradomin brew(2)",
        1: "Saradomin brew(1)"
    },
    "Battlemage potion": {
        4: "Battlemage potion(4)",
        3: "Battlemage potion(3)",
        2: "Battlemage potion(2)",
        1: "Battlemage potion(1)"
    },
    "Bastion potion": {
        4: "Bastion potion(4)",
        3: "Bastion potion(3)",
        2: "Bastion potion(2)",
        1: "Bastion potion(1)"
    },
    "Antidote++": {
        4: "Antidote++(4)",
        3: "Antidote++(3)",
        2: "Antidote++(2)",
        1: "Antidote++(1)"
    },
    "Divine magic potion": {
        4: "Divine magic potion(4)",
        3: "Divine magic potion(3)",
        2: "Divine magic potion(2)",
        1: "Divine magic potion(1)"
    },
    "Zamorak brew": {
        4: "Zamorak brew(4)",
        3: "Zamorak brew(3)",
        2: "Zamorak brew(2)",
        1: "Zamorak brew(1)"
    },
    "Stamina potion": {
        4: "Stamina potion(4)",
        3: "Stamina potion(3)",
        2: "Stamina potion(2)",
        1: "Stamina potion(1)"
    },
    "Magic potion": {
        4: "Magic potion(4)",
        3: "Magic potion(3)",
        2: "Magic potion(2)",
        1: "Magic potion(1)"
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
        1: "Ranging potion(1)"
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
        1: "Divine super defence potion(1)"
    },
    "Divine super attack potion": {
        4: "Divine super attack potion(4)",
        3: "Divine super attack potion(3)",
        2: "Divine super attack potion(2)",
        1: "Divine super attack potion(1)"
    },
    "Antifire potion": {
        4: "Antifire potion(4)",
        3: "Antifire potion(3)",
        2: "Antifire potion(2)",
        1: "Antifire potion(1)"
    },
    "Antidote+": {
        4: "Antidote+(4)",
        3: "Antidote+(3)",
        2: "Antidote+(2)",
        1: "Antidote+(1)"
    },
    "Super defence": {
        4: "Super defence(4)",
        3: "Super defence(3)",
        2: "Super defence(2)",
        1: "Super defence(1)"
    },
    "Sanfew serum": {
        4: "Sanfew serum(4)",
        3: "Sanfew serum(3)",
        2: "Sanfew serum(2)",
        1: "Sanfew serum(1)"
    },
    "Super restore": {
        4: "Super restore(4)",
        3: "Super restore(3)",
        2: "Super restore(2)",
        1: "Super restore(1)"
    },
    "Super strength": {
        4: "Super strength(4)",
        3: "Super strength(3)",
        2: "Super strength(2)",
        1: "Super strength(1)"
    },
    "Super energy": {
        4: "Super energy(4)",
        3: "Super energy(3)",
        2: "Super energy(2)",
        1: "Super energy(1)"
    },
    "Super attack": {
        4: "Super attack(4)",
        3: "Super attack(3)",
        2: "Super attack(2)",
        1: "Super attack(1)"
    },
    "Prayer potion": {
        4: "Prayer potion(4)",
        3: "Prayer potion(3)",
        2: "Prayer potion(2)",
        1: "Prayer potion(1)"
    },
    "Energy potion": {
        4: "Energy potion(4)",
        3: "Energy potion(3)",
        2: "Energy potion(2)",
        1: "Energy potion(1)"
    },
    "Restore potion": {
        4: "Restore potion(4)",
        3: "Restore potion(3)",
        2: "Restore potion(2)",
        1: "Restore potion(1)"
    },
}

for i in items:
    volumeData = None
    if(str(itemIds[items[i][4]]) in volumeJson['data']):
            volumeData = volumeJson['data'][str(itemIds[items[i][4]])]
    if(volumeData is None or 'lowPriceVolume' not in volumeData or volumeData['lowPriceVolume'] < 2000 or volumeData['highPriceVolume'] < 2000):
        continue
    fourHigh = responseJson['data'][str(itemIds[items[i][4]])]['high']
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