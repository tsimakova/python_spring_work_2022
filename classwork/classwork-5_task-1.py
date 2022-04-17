# todo: База данных пользователя.
# Задан массив объектов пользователя
'''
users = [{'login': 'Piter', 'age': 23, 'group': "admin"},
         {'login': 'Ivan',  'age': 10, 'group': "guest"},
         {'login': 'Dasha', 'age': 30, 'group': "master"},
         {'login': 'Fedor', 'age': 13, 'group': "guest"}]

Написать фильтр который будет выводить отсортированные объекты по возрасту(больше введеного)
,первой букве логина, и заданной группе.

#Сперва вводится тип сортировки:
1. По возрасту
2. По первой букве
3. По группе

тип сортировки: 1

#Затем сообщение для ввода
Ввидите критерии поиска: 16

Результат:
#Пользователь: 'Piter' возраст 23 года , группа  "admin"
#Пользователь: 'Dasha' возраст 30 лет , группа  "master"

'''

users = [{'login': 'Piter', 'age': 23, 'group': "admin"},
         {'login': 'Ivan',  'age': 10, 'group': "guest"},
         {'login': 'Dasha', 'age': 30, 'group': "master"},
         {'login': 'Fedor', 'age': 13, 'group': "guest"}]

sort_type = int(input("Enter sorting type (1 - age; 2 - name start; 3 - group): "))

if sort_type == 1:
    elder_users = []
    N = int(input("Enter minimal age: "))
    for item in users:
        if item['age'] > N:
            elder_users.append(item)
    if len(elder_users) == 0:
        print("No users elder age " + str(N))
    else:
        print(elder_users)

elif sort_type == 2:
    selected_logins = []
    S = str(input("Enter login first letter (upper case): "))
    for item in users:
        if str(item['login']).startswith(S):
            selected_logins.append(item)
    if len(selected_logins) == 0:
        print("No user logins starts with " + S)
    else:
        print(selected_logins)

elif sort_type == 3:
    selected_group = []
    G = str(input("Enter group (guest, master or admin): "))
    for item in users:
        if str(item['group']) == G:
            selected_group.append(item)
    if len(selected_group) == 0:
        print("There is no user group " + G)
    else:
        print(selected_group)

else:
    print("Unknown sorting type. Use: 1 - age; 2 - name start; 3 - group")
