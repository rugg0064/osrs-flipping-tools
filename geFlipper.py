import requests
import statistics
import multiprocessing
from scipy.stats import linregress

headers = {
    'User-Agent': 'Item Volatility Investment Algorithm - Rugg - Discord Rugg#4267'
}

class ItemPrice:
    def __init__(self, data):
        self.data = data
        self.timestamp = 0
        self.highPrice = 0
        self.lowPrice = 0
        self.highPriceVolume = 0
        self.lowPriceVolume = 0
        self.setData(data)

    def setData(self, data):
        self.timestamp = data['timestamp']
        self.highPrice = data['avgHighPrice'] or 0
        self.lowPrice = data['avgLowPrice'] or 0
        self.highPriceVolume = data['highPriceVolume']
        self.lowPriceVolume = data['lowPriceVolume']

    def averagePrice(self):
        totalVolume = self.highPriceVolume + self.lowPriceVolume
        highFraction = self.highPriceVolume / totalVolume
        lowFraction = self.lowPriceVolume / totalVolume
        return (self.highPrice * highFraction) + (self.lowPrice * lowFraction)

class OSRSItemInfo:
    def __init__(self, data):
        self.examine = ""
        self.id = 0
        self.members = False
        self.lowalch = 0
        self.limit = 0
        self.value = 0
        self.highalch = 0
        self.icon = ""
        self.name = ""
        self.setData(data)
    
    def setData(self, item):
        self.examine = item["examine"]
        self.id = item["id"]
        self.members = item["members"]
        self.lowalch = item["lowalch"] if 'lowalch' in item else 0
        self.limit = item["limit"] if 'limit' in item else 0
        self.value = item["value"]
        self.highalch = item["highalch"] if 'highalch' in item else 0
        self.icon = item["icon"]
        self.name = item["name"]

# Provides a map that goes from itemID -> item mapping
def getOsrsMapping():
    response = requests.get(
        "https://prices.runescape.wiki/api/v1/osrs/mapping", 
        headers = headers)
    if response.status_code == 200:
        data = response.json()
        objectMap = {}
        for item in data:
            osrsItem = OSRSItemInfo(item)
            objectMap[item['id']] = osrsItem
        return objectMap
    else:
        raise Exception("Failed to retrieve data from OSRS Wiki API")
    
global instantResults
instantResults = None

def getInstantResults():
    global instantResults
    if instantResults is None:
        response = requests.get(
            "https://prices.runescape.wiki/api/v1/osrs/latest", 
            headers = headers,
        )
        instantResults = response.json()['data']
    return instantResults

def getAllItemInstantPrice():
    data = getInstantResults()
    returnDict = {}
    for id, item in data.items():
        if((item['high'] is not None) and (item['low'] is not None)):
            returnDict[int(id)] = (item['high'] + item['low']) / 2
    return returnDict

def getAllItem1hrPriceVolumes():
    def getTotalVolume(data):
        return data['highPriceVolume'] + data['lowPriceVolume']
    def getWeightedPrice(data):
        totalVolume = getTotalVolume(data)
        highFraction = data['highPriceVolume'] / totalVolume
        lowFraction = data['lowPriceVolume'] / totalVolume
        return ((data['avgHighPrice'] or 0) * highFraction) + ((data['avgLowPrice'] or 0) * lowFraction)

    response = requests.get(
        "https://prices.runescape.wiki/api/v1/osrs/1h", 
        headers = headers,
    )
    data = response.json()['data']
    return {int(k): {'price':getWeightedPrice(x), 'volume':getTotalVolume(x)} for k, x in data.items() }

def get24Hour5MinutePrices(itemID):
    response = requests.get(
        "https://prices.runescape.wiki/api/v1/osrs/timeseries", 
        headers = headers,
        params = {
            'timestep': '5m',
            'id': str(itemID)
        }
    )
    data = response.json()
    return [ItemPrice(x) for x in data['data'][-288:]]
    
def linRegGetSlope(tuples):
    slope, intercept, r_value, p_value, std_err  = linregress(tuples)
    return slope

# Slope is in gp/hr
def get24HourItemSlope(itemID):
    prices = get24Hour5MinutePrices(itemID)
    linRegData = [ (price.timestamp, price.averagePrice()) for price in prices ]
    return linRegGetSlope(linRegData) * 60 * 60

def getItemStdev(itemID):
    prices = get24Hour5MinutePrices(itemID)
    averagePrices = [x.averagePrice() for x in prices]
    if(len(averagePrices) < 10):
        return None
    stdev = statistics.stdev(averagePrices)
    return stdev

def getAllStdevs(itemIDs):
    standardDeviations = []
    pool = multiprocessing.Pool(processes=8)
    try:
        results = pool.map(getItemStdev, itemIDs)
        pool.close()
        pool.join()
        return {k: v for k, v in zip(itemIDs, results)}
    except KeyboardInterrupt:
        pool.terminate()

notableItems = [7936, 554, 556, 562, 12934, 21820, 6685, 2434, 2503]

def filterItem(id):
    return (abs(get24HourItemSlope(id)) < 10) and (getItemStdev(id) > 50)

def main():
    mapping = getOsrsMapping()
    volumePrices = getAllItem1hrPriceVolumes()
    filteredItems = [k for k, v in volumePrices.items() if (500 <= v['price'] <= 150_000) and v['volume'] > 1000]
    for item in filteredItems:
        if(filterItem(item)):
            print(mapping[item].name)


    #print(volumePrices)

    #result = getAllStdevs(notableItems)
    #[print(mapping[id].name, std) for id, std in result.items()]

if __name__ == '__main__':
    main()