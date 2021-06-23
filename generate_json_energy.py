import json
import numpy as np

if __name__ == '__main__':
    json_data = {
        "type": "walking",
        "result": []
    }
    for i in range(7, 26):
        if i < 9:
            i = f"0{str(i)}"
        w_count = np.random.normal(
            loc=2700,  # 平均
            scale=1000,  # 標準偏差
            size=1,  # 出力配列のサイズ(タプルも可)
        )
        count = round(int(w_count[0]))
        if 3000 > count > 2500:
            feeling_type = "perfect"
            distance_meter = round(count * 0.7)
            time_hour = round((count * 0.55) / 3600, 1)
            speed_kilometer = round(distance_meter / time_hour / 1000, 1)
        elif 3500 > count > 1800:
            feeling_type = "happy"
            distance_meter = round(count * 0.7)
            time_hour = round((count * 0.6) / 3600, 1)
            speed_kilometer = round(distance_meter / time_hour / 1000, 1)
        elif 4200 > count > 1500:
            feeling_type = "lazy"
            distance_meter = round(count * 0.7)
            time_hour = round((count * 0.65) / 3600, 1)
            speed_kilometer = round(distance_meter / time_hour / 1000, 1)
        else:
            feeling_type = "slump"
            distance_meter = round(count * 0.7)
            time_hour = round((count * 0.7) / 3600, 1)
            speed_kilometer = round(distance_meter / time_hour / 1000, 1)
        data = {
            "date": f"2021年02月{str(i)}日00時00分",
            "feeling": feeling_type,
            "count": count,
            "distance_meter": distance_meter,
            "time_hour": time_hour,
            "speed_kilometer": speed_kilometer
        }
        json_data['result'].append(data)
    f = open(f'wepo_energy_test.json', 'w')
    json.dump(json_data, f, ensure_ascii=False, indent=4, separators=(',', ':'))
