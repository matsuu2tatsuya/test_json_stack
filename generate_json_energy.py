import json
import numpy as np

if __name__ == '__main__':
    json_data = {
        "type": "energy",
        "result": []
    }
    for i in range(7, 26):
        if i < 9:
            i = f"0{str(i)}"
        w_count = np.random.normal(
            loc=2700,  # 平均
            scale=1000,  # 標準偏差
            size=2,  # 出力配列のサイズ(タプルも可)
        )
        count = round(int(w_count[0]))
        if 3000 > count > 2500:
            feeling_type = "perfect"
            burn_energy = round(int(w_count[1]))
            energy_balance = count - burn_energy
        elif 3500 > count > 1800:
            feeling_type = "happy"
            burn_energy = round(int(w_count[1]))
            energy_balance = count - burn_energy
        elif 4200 > count > 1500:
            feeling_type = "lazy"
            burn_energy = round(int(w_count[1]))
            energy_balance = count - burn_energy
        else:
            feeling_type = "slump"
            burn_energy = round(int(w_count[1]))
            energy_balance = count - burn_energy
        data = {
            "date": f"2021-02-{str(i)}",
            "feeling": feeling_type,
            "count": count,
            "intake_energy": count,
            "energy_balance": energy_balance,
            "burn_energy": burn_energy
        }
        json_data['result'].append(data)
    f = open(f'wepo_energy_test.json', 'w')
    json.dump(json_data, f, ensure_ascii=False, indent=4, separators=(',', ':'))
