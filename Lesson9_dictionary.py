'''
словарь = {ключ : значение} - ключ является неизменяемым объектом
человек = имя - Андрей
        фамилия - Смит
        возраст - 189
        телефон - 01248795452
'''
# man=dict()
# man={}
man = {'name': 'Andrew',
       'surname': 'Smith',
       'age': 189,
       'phone': 'trinolyatrulyalya'}

print(man['name'])
print(man)
for element in man:
    print(element, end=' ')
print()
print(man.keys())
print(man.items())
print(man.values())
man['phone'] = '+38050123456789'
print(man)
man.update({'login': 'Andy'})
print(man)

study_class = {
    'Petrov': {
        'name': 'qwe',
        'age': 12
    },
    'Ivanov': {
        'name': 'rew',
        'age': 54
    },
}
print(study_class['Petrov']['name'])