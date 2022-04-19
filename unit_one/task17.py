#todo: Создайте функцию compute_bill, считающаю итоговую сумму товаров в чеке.
'''
Функция должна принимать 1 параметр - словарь, в котором указано количество едениц товара.
Цены хранятся в словаре:
prices = {
  "banana": 4,
  "apple": 2,
  "orange": 1.5,
  "pear": 3
}

'''

def compute_bill(goods_dict):  # count total cost from bill in dictionary format
    prices = {"apple": 1.5, "banana": 1, "orange": 2, "pear": 3}
    cost = []
    for item in goods_dict:
        if item in prices:
            cost.append(goods_dict[item]*prices[item])
    else:
        cost.append(0)
    return(sum(cost))


goods = {"banana": 1, "apple": 2, "orange": 1, "pear": 0, "peach": 2}

goods_cost = compute_bill(goods)
print(goods_cost)