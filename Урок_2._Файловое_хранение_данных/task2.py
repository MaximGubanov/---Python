import json


def write_json(dict_data):
    try:
        orders_data = json.load(open('orders.json'))
    except:
        orders_data = dict()
        orders_data['orders'] = []

    orders_data['orders'].append(dict_data)

    with open('orders.json', 'w') as file:
        json.dump(orders_data, file, indent=4)


def write_order_to_json(item, quantity, price, bayer, date):

    dict_file = dict(item=item, quantity=quantity, price=price, bayer=bayer, date=date)
    write_json(dict_file)


write_order_to_json('Футболка', 3, 540, 'Иванов', '2021-12-27')
write_order_to_json('Кроссовки', 4, 999, 'Сидоров', '2021-11-21')
write_order_to_json('Куртка', 1, 3399, 'Петров', '2021-11-11')


with open('orders.json', 'r', encoding='utf-8') as file_json:
    print(file_json.read())



