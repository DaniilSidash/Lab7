# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import sys

#  Использовать словарь, содержащий следующие ключи: название пункта назначения рейса;
# номер рейса; тип самолета. Написать программу, выполняющую следующие действия: ввод
# с клавиатуры данных в список, состоящий из словарей заданной структуры; записи должны
# быть размещены в алфавитном порядке по названиям пунктов назначения; вывод на экран
# пунктов назначения и номеров рейсов, обслуживаемых самолетом, тип которого введен с
# клавиатуры; если таких рейсов нет, выдать на дисплей соответствующее сообщение

if __name__ == '__main__':
    airplanes = []

    while True:
        command = input(">>> ").lower()

        if command == 'exit':
            break

        elif command == 'add':
            name = input("Пункт назначения рейса? ")
            type = input("Тип самолета? ")
            num = int(input("Номер рейса?"))

            airplane = {
                'name': name,
                'type': type,
                'num': num,
            }

            airplanes.append(airplane)
            if len(airplane) > 1:
                airplanes.sort(key=lambda item: item.get('type', ''))

        elif command == 'list':
            line = '+-{}-+-{}-+-{}-+-{}-+'.format(
                '-' * 4,
                '-' * 30,
                '-' * 20,
                '-' * 20
            )
            print(line)
            print(
                ' | {:^4} | {:^30} | {:^20} | {:^20} |'.format(
                    "№",
                    "Пункт назначения рейса",
                    "Тип самолета",
                    "Номер рейса"
                )
            )
            print(line)

            for idx, airplane in enumerate(airplanes, 1):
                print(
                    '| {:>4} | {:<30} | {:<20} | {:>20} |'.format(
                        idx,
                        airplane.get('name', ''),
                        airplane.get('type', ''),
                        airplane.get('num', 0)
                    )
                )

            print(line)

        elif command.startswith('select '):
            parts = command.split(' ', maxsplit=1)
            count = 0

            for airplane in airplanes:
                if parts[1] == airplane.get('type').lower():
                    count += 1
                    print(
                        '{:>4}: {} {}'.format(count, product.get('coast', ' '), product.get('name', ' '))
                    )
                if count == 0:
                    print("Рейс с таким названием не найден")

        elif command.startswith('load '):
            parts = command.split(' ', maxsplit=1)
            with open(parts[1], 'r') as f:
                airplanes = json.load(f)

        elif command.startswith('save '):
            parts = command.split(' ', maxsplit=1)
            with open(parts[1], 'w') as f:
                json.dump(airplanes, f)

        elif command == 'help':
            # Вывести справку о работе с программой.
            print("Список команд:\n")
            print("add - добавить рейсы;")
            print("list - вывести список рейсов;")
            print("select <самолет> - запросить информацию о рейсе")
            print("load <имя файла> - загрузить данные из файла;")
            print("save <имя файла> - сохранить данные в файл;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)