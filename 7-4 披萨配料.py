active = True
while active:
    material = input('请输入要加入配料(如不加入则输出("quit")): ')
    if material == 'quit':
        break
    print('我们会在披萨中加入' + material)