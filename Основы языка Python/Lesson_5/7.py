# -*- coding: utf-8 -*-
import json


def firm_prof(data):
    firm_name = data[0]
    money = list(map(int, data[2:]))
    return {firm_name: money[0] - money[1]}


def ave_prof(data):
    new_data = {}
    ave = 0
    cnt = 0
    for el in data:
        new_data.update(el)
        for i, j in el.items():
            if j > 0:
                cnt += 1
                ave += j
    return [new_data, {"average_profit": int(ave / cnt)}]


with open("7.txt") as f, open("7.json", "w") as json_f:
    stage_data = list(map(firm_prof, [line.split() for line in f.readlines()]))
    final_data = ave_prof(stage_data)
    json.dump(final_data, json_f)
