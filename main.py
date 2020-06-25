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
# print('\n', cook_book.keys())
print('\n', cook_book['Омлет'])

def make_buy_list(incoming_list, guest_number):

    meals_check_list = list(cook_book.keys())

    for meal in incoming_list:
        if meal not in meals_check_list:
            incoming_list.remove(meal)
            print(f'\nБлюдо {meal} отсутствует в книге рецептов')
    buy_dict = {}

    for meal in incoming_list:
        ingredients = cook_book[meal]

        for ingredient in ingredients:
            if ingredient['ingredient_name'] not in buy_dict.keys():

                ing_key = ingredient['ingredient_name']
                buy_dict[ing_key] = {'quantity': ingredient['quantity'], 'measure': ingredient['measure']}


            else:
                # print(buy_dict[ingredient['ingredient_name']]['quantity']) #уже имеющееся кол-во ингридиента
                # print(ingredient['quantity'])                              #кол-во которое нужно добавить

                buy_dict[ingredient['ingredient_name']]['quantity'] += ingredient['quantity']
                
    for ingredient in buy_dict.keys():
        # print(ingredient)
        # print(buy_dict[ingredient])
        # print(buy_dict[ingredient]['quantity'])
        buy_dict[ingredient]['quantity'] *= guest_number

    print('\n', buy_dict)
    return buy_dict


make_buy_list(['Омлет', 'Запеченный картофель', 'Салат', 'Омлет', 'Фахитос', 'Шаурма'], 5)
# make_buy_list(['Омлет', 'Омлет', 'Омлет', 'Омлет', 'Омлет', 'Омлет', 'Омлет', 'Омлет'], 1)



