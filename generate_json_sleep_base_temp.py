import json
import numpy as np

if __name__ == '__main__':
    json_data = {
        "type": "sleep_temp",
        "result": []
    }
    for i in range(7, 26):
        if i < 9:
            i = f"0{str(i)}"
        w_count = np.random.normal(
            loc=6,  # 平均
            scale=2,  # 標準偏差
            size=1,  # 出力配列のサイズ(タプルも可)
        )
        count = round(float(w_count[0]), 1)
        if 8 > count > 6.5:
            feeling_type = "perfect"
            base_temp = round(float(np.random.normal(loc=36.7, scale=0.3, size=1)[0]), 1)
        elif 10 > count > 5.5:
            feeling_type = "happy"
            base_temp = round(float(np.random.normal(loc=36.7, scale=0.3, size=1)[0]), 1)
        elif 12 > count > 5:
            feeling_type = "lazy"
            base_temp = round(float(np.random.normal(loc=36.7, scale=0.3, size=1)[0]), 1)
        else:
            feeling_type = "slump"
            base_temp = round(float(np.random.normal(loc=36.7, scale=0.3, size=1)[0]), 1)
        if base_temp > 37.0:
            feeling_type = "lazy"
        elif base_temp > 37.5:
            feeling_type = "slump"
        data = {
            "date": f"2021年02月{str(i)}日00時00分",
            "feeling": feeling_type,
            "count": count,
            "base_temperature": base_temp,
        }
        json_data['result'].append(data)
    f = open(f'wepo_sleep_baseTemp_test.json', 'w')
    json.dump(json_data, f, ensure_ascii=False, indent=4, separators=(',', ':'))
