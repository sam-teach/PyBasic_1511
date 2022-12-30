# '''
# словарь = {ключ : значение} - ключ является неизменяемым объектом
# человек = имя - Андрей
#         фамилия - Смит
#         возраст - 189
#         телефон - 01248795452
# '''
# # man=dict()
# # man={}
# man = {'name': 'Andrew',
#        'surname': 'Smith',
#        'age': 189,
#        'phone': 'trinolyatrulyalya'}
#
# print(man['name'])
# print(man)
# for element in man:
#     print(element, end=' ')
# print()
# print(man.keys())
# print(man.items())
# print(man.values())
# man['phone'] = '+38050123456789'
# print(man)
# man.update({'login': 'Andy'})
# print(man)
#
# study_class = {
#     'Petrov': {
#         'name': 'qwe',
#         'age': 12
#     },
#     'Ivanov': {
#         'name': 'rew',
#         'age': 54
#     },
# }
# print(study_class['Petrov']['name'])

'''
product = {
name : ''
description : ''
price : 0
}
'''
products = {
    1: {
        'name': 'meat',
        'description': 'Crocodile meat',
        'price': 412
    },
    2: {
        'name': 'juice',
        'description': 'Crocodile juice',
        'price': 612
    },
    3: {
        'name': 'leg',
        'description': 'Crocodile leg',
        'price': 112.8
    },
    4: {
        'name': 'egg',
        'description': 'Chicken egg',
        'price': 30.5
    },
}
for id in products:
    print(products[id]['name'], end=' ')
print()
cart = []
cart.append(products[2])
cart.append(products[4])
print('Your choice is ', end='')
for product in cart:
    print(product['name'], end=' ')
print()
print('Your price is ', end='')
print(sum(product['price'] for product in cart))
