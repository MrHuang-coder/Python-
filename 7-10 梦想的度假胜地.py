responses = {}
polling_active = True

while polling_active:
    name = input("你叫什么名字: ")
    response = input('你梦想的度假胜地在哪里？')

    responses[name] = response

    repeat = input("你想让另一个人回复吗？(yes/ no)")
    if repeat == 'no':
        polling_active = False

print('-------Poll Results-----')
for name, response in responses.items():
    print(name + "梦想的度假胜地是" + response + "。")


