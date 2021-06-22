import json
import random

if __name__ == '__main__':
    json_data = {
        "type": "walking",
        "result": []
    }
    for i in range(7, 26):
        if i < 9:
            i = f"0{str(i)}"
        count = random.randint(1500, 8000)
        if count > 6000:
            feeling_type = "perfect"
            distance_meter = random.randint(3000, 10000)
            time_hour = round(random.uniform(1, 3), 1)
            speed_kilometer = round(random.uniform(5, 7), 1)
        elif count > 4000:
            feeling_type = "happy"
            distance_meter = random.randint(2000, 5000)
            time_hour = round(random.uniform(1, 2.3), 1)
            speed_kilometer = round(random.uniform(4.5, 6), 1)
        elif count > 2500:
            feeling_type = "lazy"
            distance_meter = random.randint(1000, 4000)
            time_hour = round(random.uniform(0.3, 2.2), 1)
            speed_kilometer = round(random.uniform(3.5, 5), 1)
        else:
            feeling_type = "slump"
            distance_meter = random.randint(300, 3000)
            time_hour = round(random.uniform(0, 1.5), 1)
            speed_kilometer = round(random.uniform(3.3, 4), 1)
        data = {
            "date": f"2021年02月{str(i)}日00時00分",
            "feeling": feeling_type,
            "count": count,
            "distance_meter": distance_meter,
            "time_hour": time_hour,
            "speed_kilometer": speed_kilometer
        }
        json_data['result'].append(data)
    f = open(f'wepo_walking_test.json', 'w')
    json.dump(json_data, f, ensure_ascii=False, indent=4, separators=(',', ':'))
