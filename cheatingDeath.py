import helper

def filter(data):
    if data['highPriceVolume'] + data['lowPriceVolume'] < 5:
        return False
    if data['avgLowPrice'] is None:
        return False
    if data['avgLowPrice'] < 3_000:
        return False
    if data['avgLowPrice'] > 10_000_000:
        return False
    return True


def main():
    prices = helper.get_1h_prices()
    mapping = helper.get_mapping()
    name_map = helper.get_id_to_name_mapping(mapping)
    filtered = {id: data for id, data in prices.items() if filter(data)}
    item_ids = [k for k in filtered]
    guide_prices = helper.get_guide_prices(item_ids)
    items = [
        {
            "name": name_map[int(item_id)],
            "id":  item_id,
            "multiplier": int(guide_prices[item_id]['price']) / int(prices[item_id]['avgLowPrice'])
        }
        for item_id in item_ids
    ]
    sorted_items = sorted(items, key=lambda item: item['multiplier'], reverse=True)
    for item in sorted_items[:10]:
        print(item['name'], guide_prices[item['id']]['price'], prices[item['id']]['avgLowPrice'], item['multiplier'])

if __name__ == '__main__':
    main()