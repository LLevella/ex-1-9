
def get_shop_list_by_dishes(dishes, person_count, cook_book):
  shop_list = {}
  for dish in dishes:
    for ingridient in cook_book[dish]:
      new_shop_list_item = dict(ingridient)

      new_shop_list_item['quantity'] *= person_count
      if new_shop_list_item['ingridient_name'] not in shop_list:
        shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
      else:
        shop_list[new_shop_list_item['ingridient_name']]['quantity'] += new_shop_list_item['quantity']
  return shop_list

def print_shop_list(shop_list):
  for shop_list_item in shop_list.values():
    print('{} {} {}'.format(shop_list_item['ingridient_name'], shop_list_item['quantity'],
                            shop_list_item['measure']))

def create_shop_list(cook_book):
  person_count = int(input('Введите количество человек: '))
  dishes = input('Введите блюда в расчете на одного человека (через запятую): ') \
    .lower().split(', ')
  shop_list = get_shop_list_by_dishes(dishes, person_count, cook_book)
  print_shop_list(shop_list)


def create_dict_from_list(one_of_ings):
    d_ing = {}
    d_ing['ingridient_name'] = one_of_ings[0].lower()
    d_ing['quantity'] = int(one_of_ings[1])
    d_ing['measure'] = one_of_ings[2].lower()
    return d_ing

def create_ing_list(f, n_ing):
    ingridients = []
    for i in range(n_ing):
        one_of_ingridients = f.readline().strip().split(' | ')
        ingridients.append(create_dict_from_list(one_of_ingridients))
        # create_dict_from_list(one_of_ingridients)
    return ingridients

def input_data(cook_book):
    with open('input.txt', 'r') as fin:
        for fline in fin:
            name = fline.strip().lower()
            n_ing = int(fin.readline().strip())
            cook_book[name] = create_ing_list(fin, n_ing)
            fin.readline()
     return cook_book



def main():
  cook_book = {
  'яйчница': [
    {'ingridient_name': 'яйца', 'quantity': 2, 'measure': 'шт.'},
    {'ingridient_name': 'помидоры', 'quantity': 100, 'measure': 'гр.'}
    ],
  'стейк': [
    {'ingridient_name': 'говядина', 'quantity': 300, 'measure': 'гр.'},
    {'ingridient_name': 'специи', 'quantity': 5, 'measure': 'гр.'},
    {'ingridient_name': 'масло', 'quantity': 10, 'measure': 'мл.'}
    ],
  'салат': [
    {'ingridient_name': 'помидоры', 'quantity': 100, 'measure': 'гр.'},
    {'ingridient_name': 'огурцы', 'quantity': 100, 'measure': 'гр.'},
    {'ingridient_name': 'масло', 'quantity': 100, 'measure': 'мл.'},
    {'ingridient_name': 'лук', 'quantity': 1, 'measure': 'шт.'}
    ]
  }
    cook_book = input_data(cook_book)
    print(cook_book)
    create_shop_list(cook_book)



main()
