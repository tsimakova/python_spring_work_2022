#todo: Требуется создать csv-файл «algoritm.csv» со следующими столбцами:
'''
– id - номер по порядку (от 1 до 10);
– текст из списка algoritm

algoritm = [ "C4.5" , "k - means" , "Метод опорных векторов" , "Apriori" ,
"EM" , "PageRank" , "AdaBoost", "kNN" , "Наивный байесовский классификатор" , "CART" ]

Каждое значение из списка должно находится на отдельной строке.
'''

algoritm = ["C4.5", "k - means", "Метод опорных векторов", "Apriori", "EM", "PageRank", "AdaBoost", "kNN", "Наивный байесовский классификатор", "CART" ]

id = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

fd = open("D:\\python_homework\\algoritm.csv", "w", encoding='utf-8')

new = []
for i in range(len(id)):
    fd.write(str(id[i])+ '\t' + str(algoritm[i])+ '\n')

fd.close()