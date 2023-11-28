def check_int(string):
    try:
        return type(int(string[0])) == int
    except ValueError:
        return False


with open('recipes.txt', 'r') as file:  # Задача №1
    cook_book = {}
    for item in file:
        item = item.replace('\n', '').split(' | ')
        if item != ['']:
            if check_int(item):
                continue
            if len(item) != 3:
                name = str(item[0])
            else:
                try:
                    cook_book[name].append({'ingredient_name': item[0], 'quantity': int(item[1]), 'measure': item[2]})
                except KeyError:
                    cook_book[name] = [{'ingredient_name': item[0], 'quantity': int(item[1]), 'measure': item[2]}]


def get_shop_list_by_dishes(dishes, person_count):  # Задача №2
    shop_list = {}
    for d in dishes:
        for i in cook_book[d]:
            ingredient_name = i['ingredient_name']
            try:
                shop_list[ingredient_name]['quantity'] += i['quantity'] * person_count
            except KeyError:
                shop_list[ingredient_name] = {'measure': i['measure'], 'quantity': i['quantity'] * person_count}
    return shop_list


print(get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2))


def task_3(txt):  # Задача №3
    txt_list = {}
    for i in txt:
        with open(i, 'r') as f:
            counting = 1
            for t in f:
                try:
                    txt_list[i].append({'line': counting, 'txt': t})
                except KeyError:
                    txt_list[i] = [{'line': counting, 'txt': t}]
                counting += 1
            txt_list[i] += [counting-1]
    sort_txt_list = []
    for txt in txt_list:
        sort_txt_list.append((txt, txt_list[txt][-1]))
    sort_txt_list = sorted(sort_txt_list, key=lambda x: x[::-1])

    final_file = open("final.txt", "w")
    for final in sort_txt_list:
        final_file.write(f'{final[0]}\n')
        for i in txt_list[final[0]]:
            try:
                final_file.write(f"Строка № {i['line']} файла номер {final[0].replace('.txt','')}: {i['txt']}")
            except TypeError:
                continue


task_3(['1.txt', '2.txt', '3.txt'])
