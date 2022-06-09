#todo: Создайте объект сериализации любым методом для соседа, запишите его в файл,
# педайте его ему для считывания. Соседу необходимо десириализовать полученый объект.


#todo: Заданы два списка. Необходимо их сериализовать в один файл.

import pickle


list_one = [True, 'If the implementation is hard to explain, it\'s a bad idea.', {'age': 27}]
list_two = [False, 'Sparse is better than dense.', {'age': 90}]


with open('test_data/test.pickle','wb') as f:
    pickle.dump(list_one, f)
    pickle.dump(list_two, f)

f.close()