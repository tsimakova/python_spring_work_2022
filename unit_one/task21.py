# todo: Задан словарь, его значения необходимо внести по соответвющим тегам и атрибутам вместо вопросов (?)
# заполненный шаблон записать в файл index.html

page = {"title": "Тег BODY",
        "charset": "utf-8",
        "alert": "Документ загружен",
        "p": "Ut wisis enim ad minim veniam,  suscipit lobortis nisl ut aliquip ex ea commodo consequat."}

template = """ 
<!DOCTYPE HTML>
<html>
 <head>
  <title> ? </title>
  <meta charset=?>
 </head>
 <body onload="alert(?)">

  <p>?</p>
 </body>
</html>
"""

old_f = open('D:\python_homework\index_old.html', 'r', encoding = 'utf-8')

new_f = open('D:\python_homework\index.html', 'w', encoding = 'utf-8')

contents = old_f.readlines()


contents[3] = str(contents[3])[:9] + page['title'] + str(contents[3])[12:]
contents[4] = str(contents[4])[:16] + page['charset'] + str(contents[4])[17:]
contents[6] = str(contents[6])[:21] + page['alert'] + str(contents[6])[22:]
contents[8] = str(contents[8])[:5] + page['p'] + str(contents[8])[6:]

#print(contents)


for element in contents:
        new_f.write(element)
new_f.close()
old_f.close()