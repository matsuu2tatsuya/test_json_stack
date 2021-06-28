import json
import numpy as np

if __name__ == '__main__':
    json_data = {
        "type": "walking",
        "user_id": "001",
        "result": []
    }
    for i in range(7, 26):
        if i < 9:
            i = f"0{str(i)}"
        w_count = np.random.normal(
            loc=8202,  # 平均
            scale=4000,  # 標準偏差
            size=1,  # 出力配列のサイズ(タプルも可)
        )
        count = round(int(w_count[0]))
        if count > 11000:
            feeling_type = "perfect"
            distance_meter = round(count * 0.7)
            time_hour = round((count * 0.55) / 3600, 1)
            speed_kilometer = round(distance_meter / time_hour / 1000, 1)
        elif count > 8202:
            feeling_type = "happy"
            distance_meter = round(count * 0.7)
            time_hour = round((count * 0.6) / 3600, 1)
            speed_kilometer = round(distance_meter / time_hour / 1000, 1)
        elif count > 5000:
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
            "date": f"2021-02-{str(i)}",
            "feeling": feeling_type,
            "count": count,
            "distance_meter": distance_meter,
            "time_hour": time_hour,
            "speed_kilometer": speed_kilometer
        }
        json_data['result'].append(data)
    f = open(f'wepo_walking_test.json', 'w')
    json.dump(json_data, f, ensure_ascii=False, indent=4, separators=(',', ':'))
