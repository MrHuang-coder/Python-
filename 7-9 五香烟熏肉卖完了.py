sandwich_orders = ['fish', 'mutton', 'beef', 'pastrami', 'chicken', 'pastrami', 'pastrami']
print('熟食店的五香牛肉都卖完了!')
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print(sandwich_orders)

