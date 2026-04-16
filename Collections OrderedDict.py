from collections import OrderedDict

n = int(input())
item_list = OrderedDict()

for _ in range(n):
    data = input().rsplit(' ', 1)
    item_name = data[0]
    net_price = int(data[1])
    item_list[item_name] = item_list.get(item_name, 0) + net_price

for item, price in item_list.items():
    print(item, price)
