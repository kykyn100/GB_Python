# -*- coding: utf-8 -*-
from itertools import count
import re
with open("2.txt") as f:
    data = f.read()
    print(f'В файле написано следующее:\n\n{data}\n')
    f.seek(0)
    lines = f.readlines()
    line_cnt = len(lines)
    print(f'Файл соделжит {line_cnt} строк.')
    cnt = count(1)
    for i in lines:
        word_cnt = len((re.sub('\W+',' ', i )).split())
        print(f'Строка {next(cnt)} содержит {word_cnt} слов.')

