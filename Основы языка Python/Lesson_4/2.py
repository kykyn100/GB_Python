example_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

#
#
# def checker(checked_list):
#     for i in range(len(checked_list) - 1):
#         if checked_list[i] < checked_list[i + 1]:
#             yield checked_list[i + 1]
#
# processed_list = checker(example_list)
# print(next(processed_list))
#
# Сначала написал так, чтобы разобраться и сократить в одну строку.

processed_list = [example_list[i + 1]
                  for i in range(len(example_list) - 1)
                  if example_list[i] < example_list[i + 1]]
print(processed_list)
