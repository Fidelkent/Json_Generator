import json
import time
import random
from sql_connect import rows

print(rows[0]['game'])
print(rows[1]['game'])
print(rows[2]['game'])
print(rows[3]['game'])

with open('json_files/JsonData.json', 'r') as file:
    data = json.load(file)

print("Программа запущена. Json обновляется каждую 1 секунду")

game = ["NBA", "FIFA", "CS", "Dota"]
title = ["Яблоки VS Апельсины", "Бананы VS Чебуреки", "Курицы VS Кошки", 'Дети VS Тараканы']


def index_counter(value):
    index = 0
    while True:
        yield value[index]
        index = (index + 1) % len(value)

game_generator = index_counter(game)
title_generator = index_counter(title)


# index = 0
try:
    while True:
        # c.execute("SELECT * FROM json_data")
        # data_db = c.fetchall()
        # index = (index + 1) % len(game)
        game_value = next(game_generator)
        title_value = next(title_generator)
        idid = random.randint(1000, 10000)
        round_num = random.randint(50, 131)
        points = random.randint(1000, 1500)
        fouls = random.randint(500, 1000)
        tournament_id = random.randint(10, 100)
        one_point_goal = random.randint(115, 345)
        two_point_goal = random.randint(115, 345)


        data['info']['id'] = idid
        data['info']['round_number'] = round_num
        data['info']['matchround_id'] = points
        data['info']['game'] = game_value
        data['info']['title'] = title_value
        data['info']['tournament_id'] = tournament_id
        data['teams'][0]['statistic']['matchround']['point'] = points
        data['teams'][0]['statistic']['matchround']['team_foal'] = fouls
        data['teams'][0]['statistic']['matchround']['one_point_goal'] = one_point_goal
        data['teams'][0]['statistic']['matchround']['two_point_goal'] = two_point_goal


        with open('json_files/JsonData.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

        time.sleep(1)

except KeyboardInterrupt:
    print("Program interrupted by user.")
    # conn.close()

    # Этот текст для проверки работы программы с githubv./1
