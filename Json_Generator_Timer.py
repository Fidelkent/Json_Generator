import time
import json

with open('json_files/timer.json', 'r') as file:
    data = json.load(file)

is_start = False


def start_cyclic_timer(minutes):
    total_seconds = minutes * 60
    is_start = True

    while is_start:
        for sec in range(total_seconds, 0, -1):
            m = sec // 60
            s = sec % 60
            time_str = f"{m:02d}:{s:02d}"
            print(time_str)
            data[0]['real_time'] = time_str
            data[0]['is_start'] = is_start
            with open('json_files/timer.json', 'w', encoding='utf-8') as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
            time.sleep(1)


try:
    while True:
        start_cyclic_timer(10)



except KeyboardInterrupt:
    is_start = False
    data[0]['is_start'] = is_start
    with open('json_files/timer.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

    print("Program interrupted by user.")
