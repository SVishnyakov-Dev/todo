import json
import os
if os.path.exists('tasks.json'):
    with open('tasks.json', 'r') as json_file:
        a = json.load(json_file)

    while True:
        print('Введите команду:')
        b = input()
        if b == 'list':
            for i in a['list']:
                if not i["done"]:
                    print(i["name"], i["id"])
        elif b == 'add':
            print('Введите задачу:')
            k0 = input()
            k1 = len(a["list"]) + 1
            k = {"id": k1, "name": k0, "done": False}
            a["list"].append(k)
            with open('tasks.json', 'w') as json_file:
                json.dump(a, json_file, ensure_ascii=False, indent = 4)
            print("Задача добавлена")
        elif b == "help":
            print("Доступные команды:\n add - добавить задачу\n list - список задач\n done - отметить задачу выполненой\n exit - выход")
        elif b == 'done':
            print("Введите ID задачи:")
            try:
                b1 = int(input())
                try:
                    t = a["list"][b1-1]
                    t["done"] = True
                    with open('tasks.json', 'w') as json_file:
                        json.dump(a, json_file, indent = 4)
                    for i in a["list"]:
                        if not i["done"]:
                            print(i["name"])
                except IndexError:
                    print('Нет задачи')
            except ValueError:
                print('No number')
        elif b == 'exit':
            print('Пока!')
            break
        else:
            print("Команда еще не создана")
else:
    print('Json file отсутствует')
