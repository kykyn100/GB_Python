from functools import reduce

def gen(data):
    line = ([str(z) for z in i] for i in (el for el in data_a))
    # line_n = [i for i in ' '.join(next(line))]
    yield ' '.join(next(line))

data_a = [[1, 2, 3, 4], [4, 3, 2, 1], [2, 1, 4, 3], [3, 4, 1, 2]]


# # el = (line for line in data_a)
#
# # matrix_line = ([str(z) for z in i] for i in (el for el in data_a))
# test = (el for el in data_a)
# # matrix_line = (i for i in (el for el in data_a))
# matrix_line = [str(i) for i in next(test)]
# # matrix = reduce(lambda x, y: x, y, next(matrix_line))
# lol = []
# i = 0
#
# # for i in next(test):
# #     print(i, type(i))
#
# # for i in next(matrix_line):
# #     print(i, type(i))
# # for i in next(matrix_line):
# #     print(i, type(i))
#
# for i in matrix_line:
#     print(i, type(i))


final = ''


data = str(j for j in (el for el in data_a))

print(next(data))
