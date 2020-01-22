sandwich_orders = ['猪肉', '牛肉', '羊肉']
finished_sandwiches = []
while sandwich_orders:
    finished_sandwiches.append(sandwich_orders.pop())
for i in finished_sandwiches:
    print(i + '披萨好了！')