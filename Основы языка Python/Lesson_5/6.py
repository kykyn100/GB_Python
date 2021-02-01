# -*- coding: utf-8 -*-
import re


def cleaner(data):
    hours = 0
    cl_data = re.sub('\W+', ' ', data)
    cl_data = cl_data.split(' ')
    hours = sum([hours + int(num) for num in cl_data if num.isdigit()])
    return {cl_data[0]: hours}


dic = {}
with open("6.txt") as f:
    for line in f.readlines():
        dic.update(cleaner(line))
    print(dic)