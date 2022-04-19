#todo:Создайте программу, которая будет выводить все возможные комбинации при броске 2 игральных костей
'''

и сумму их значений. У игральной кости стороны пронумерованы от 1 до 6.

Пример вывода:
Сумма 2   комбинация [(1,1)]
Сумма 3   комбинация [(1,2),(2,1)]
Сумма 4   комбинация [(1,3),(3,1),(2,2)]
........................................
Выводы комбинаций оформить в список кортежей.

'''

dice_1 = [1, 2, 3, 4, 5, 6]
dice_2 = list(dice_1)
combination_1 = ()
combination_2 = ()
list_1 = []
list_2 = []


for i in dice_1:
    for j in dice_2:
        combination_1 = ((i), (j))
        combination_2 = ((j), (i))
        list_1.append(tuple(combination_1))
        list_2.append(tuple(combination_2))
values = list_1 + list_2
print(values)
keys = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
#print(values)
new_dict = {}

for v in range(len(values)):
    new_dict = sorted({sum(values[v]), values[v]})
    print(new_dict)
    #for k in keys:
     #   if sum(v) == k:
      #      new_dict.update({k:v})
       #     #print(new_dict)
        #else:
         #   pass

#new_dict = dict(zip(keys, values))

#print(new_dict)


#for i in values:
 #   for k in keys:





#for i in keys:
 #   new_dict[i] = values(sum(i))

#print(keys)

#print(new_dict)

#sum_list = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

#x = dict.fromkeys(sum_list)
#print(x)

#for t in tmp_list:
 #   new_dict.update({sum(t):t})
#print(new_dict)



'''
tmp_sum = []
for t in tmp_list:
    tmp_sum.append(sum(t))
  #  print('Sum ' + str(sum(t)) + ' Combination '+ tuple(t))
final_list = list(dict.fromkeys(tmp_sum))
#print(final_list)
#print(tmp_list)
y = []
for r in range(len(final_list)):
    for n in tmp_list:
    if final_list[r]) == sum(t):
        print(final_list[r] + )
    
'''



#print(dice_1)
#print(dice_1)

