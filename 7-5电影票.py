while True:
    age = input('请输入您的年龄: ')
    age = int(age)
    if age < 3:
        cost = 10
    elif 3 <= age <12:
        cost = 10
    else:
        cost = 15
    print('你的票价为' + str(cost) + '元')
