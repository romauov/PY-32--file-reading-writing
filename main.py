# создаём словарь с блюдами
# открываем файл
# читаем строку с названием блюда,
# если строка пустая - break
# помещаем в словарь запись с ключом (название блюда) и значением (список ингридиентов)
# читаем строку с количеством ингридиентов
# запускаем цикл по количеству ингридиентов
#     читаем сроку, разбиваем её по " | " на:\
#         1 название ингридиента
#         2 количество ингридиента
#         3 размерность ингридиента
#     разбитую строку преобразуем в словарь с ключами 'ingredient_name', 'quantity', 'measure'
#     полученный словарь заносим список ингридиентов
# читаем пустую строку


cook_book = {}

with open('recipes.txt', encoding = 'utf8') as f:
     while True:
        meal_name = f.readline().rstrip()
        ingredient_number = f.readline().rstrip()

        if not meal_name or not ingredient_number:
            break
        cook_book[meal_name] = []
        for ingredient in range(int(ingredient_number)):
            ing = f.readline().rstrip()
            split_ing = ing.split(' | ')
            ing_dict = {}
            ing_dict['ingredient_name'] = split_ing[0]
            ing_dict['quantity'] = int(split_ing[1])
            ing_dict['measure'] = split_ing[2]
            cook_book[meal_name].append(ing_dict)
        f.readline()

print(cook_book)
print(cook_book.keys())
print(cook_book['Фахитос'])


