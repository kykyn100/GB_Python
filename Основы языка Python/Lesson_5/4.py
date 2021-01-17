# -*- coding: utf-8 -*-


def converter(data, glossary):
    new_data = data.split()
    if new_data[0] in glossary.keys():
        new_data[0] = glossary[new_data[0]]
        return " ".join(new_data)

num_dict = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'
}


with open("4.txt") as f_old, open("4_new.txt", "w") as f_new:
    for line in f_old.readlines():
        f_new.writelines(converter(line, num_dict) + '\n')