class Matrix:
    """ Класс Матрица.
        Инициатор принимает список со строками матрицы в виде списков."""

    def __init__(self, matrix: list):
        self.matrix = matrix

    def __str__(self):
        self.view = ''
        for el in self.matrix:
            line = [str(i) for i in el]
            self.view += f"| {' '.join(line)} |\n"
        return self.view

    def __add__(self, other):
        a = self.matrix
        b = other.matrix
        result = []
        for cnt in range(len(a)):
            sum_line = [x + y for x, y in zip(a[cnt], b[cnt])]
            result.append(sum_line)
        return Matrix(result)


data_a = [[1, 2, 3, 4], [4, 3, 2, 1], [2, 1, 4, 3], [3, 4, 1, 2]]
data_b = [[5, 6, 7, 8], [8, 7, 6, 5], [6, 5, 8, 7], [7, 8, 5, 6]]

a = Matrix(data_a)
b = Matrix(data_b)
print(f'Матрица А:\n{a}')
print(f'Матрица Б:\n{b}')
print(f'Результат сложения матриц А и Б:\n{a + b}')
