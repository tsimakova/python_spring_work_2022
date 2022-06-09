# todo: Прасим страницу сайта центробанка
# Зайдите на сайт Центробанка(cbr.ru) через http-client
# Получите индексную страницу.
# Из индексной страницы извлеките данные по: ключевой ставки, курсе валюты USD, EUR
# Выведите полученные данные на консоль


import http.client

conn = http.client.HTTPSConnection("www.cbr.ru")
conn.request("GET", "/")
r1 = conn.getresponse()
print(r1.status, r1.reason)

# Прочитаем страницу целиком
#data1 = r1.read()

# чтение данных по частям
page = []
while chunk := r1.read(200):
    page.append(repr(chunk))

#print(page)
main_ind = [s for s in page if "main-indicator_value" in s]
main_ind_value = (main_ind[2]).split(">")[6].split('%')[0]
print("main indicator value: " + main_ind_value + "%")

some_list = [s for s in page if "col-md-2 col-xs-9 _right mono-num" in s]
#print(some_list)
usd_sell = some_list[0].split(">")[1].split(" ")[0]
print("usd_sell: " + usd_sell)
usd_buy = some_list[0].split(">")[3].split(" ")[0]
print("usd_buy: " + usd_buy)
eur_sell = some_list[1].split(">")[4].split(" ")[0]
print("eur_sell: " + eur_sell)


#print(some_list[0].split(" "))
#new_list = [s for s in page if "num\">" in s]
#print(new_list)

#print(new_list)


