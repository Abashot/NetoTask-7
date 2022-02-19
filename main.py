from pprint import pprint

def cookbook_dict(source):
    with open(source, 'r', encoding='utf-8') as f:
        cook_book = {}        
        
        for line in f:
            dish = line.strip()
            count = int(f.readline().strip())
            ingredients = []
            for i in range(count):
                ingredients_list = f.readline().strip().split(' | ')
                items = dict.fromkeys(['ingredient_name', 'quantity', 'measure'])
                for item in ingredients_list:
                    items['ingredient_name'] = ingredients_list[0]
                    items['quantity'] = ingredients_list[1]
                    items['measure'] = ingredients_list[2]
                ingredients.append(items)
                dish_dict = {dish: ingredients}
                cook_book.update(dish_dict)
            f.readline()
            
    return cook_book

def get_shop_list_by_dishes(dishes, person_count):
  cook_book = cookbook_dict('cookbook.txt')
  shopping_list = {}
  
  for dish in dishes: 
    for recipe in cook_book.keys():
      if recipe == dish:
        for ingredient in cook_book[recipe]:
          if ingredient['ingredient_name'] not in shopping_list.keys():
            shopping_list.update({ingredient['ingredient_name']: {'measure' : ingredient['measure'],\
                'quantity' : int(ingredient['quantity']) * person_count}})
          else:
            shopping_list[ingredient['ingredient_name']]['quantity'] += int(ingredient['quantity']) * person_count
  
  return shopping_list

pprint(cookbook_dict('cookbook.txt'))
print()
pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))