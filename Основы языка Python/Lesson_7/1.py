class Matrix:
    """ Класс Матрица.
        Инициатор принимает список со строками матрицы в виде списков."""

    def __init__(self, matrix: list):
        self.matrix = matrix

    # def __str__(self):
    #     self.view = ''
    #     for el in self.matrix:
    #         line = [str(i) for i in el]
    #         self.view += f"| {' '.join(line)} |\n"
    #     return self.view

    # def __add__(self, other):
    #     other = Matrix(other)
    #     result = []
    #     numbers = []
    #     for i in range(len(self.matrix)):
    #         for j in range(len(self.matrix[0])):
    #             summa = other[i][j] + self.matrix[i][j]
    #             numbers.append(summa)
    #             if len(numbers) == len(self.matrix):
    #                 result.append(numbers)
    #                 numbers = []
    #     return Matrix(result)



    def __add__(self, other):
        other = other
        for el in self:
            print(el)






data_a = [[1, 2, 3, 4], [4, 3, 2, 1], [2, 1, 4, 3], [3, 4, 1, 2]]
data_b = [[5, 6, 7, 8], [8, 7, 6, 5], [6, 5, 8, 7], [7, 8, 5, 6]]

a = Matrix(data_a)
b = Matrix(data_b)
print(a)
print(type(a))
print(b)
print(type(b))

a + b

