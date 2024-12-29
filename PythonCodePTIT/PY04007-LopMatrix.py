class Matrix:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.matrix = [[0 for _ in range(col)] for _ in range(row)]

    def input_data(self, data):
        for i in range(self.row):
            self.matrix[i] = list(map(int, data[i].split()))

    def multiply(self):
        transpose_matrix = Matrix(self.col, self.row)
        for i in range(self.row):
            for j in range(self.col):
                transpose_matrix.matrix[j][i] = self.matrix[i][j]

        result = Matrix(self.row, self.row)
        for i in range(self.row):
            for j in range(self.row):
                result.matrix[i][j] = 0
                for k in range(self.col):
                    result.matrix[i][j] += (
                        self.matrix[i][k] * transpose_matrix.matrix[k][j]
                    )
        return result

    def __str__(self):
        res = ""
        for i in range(self.row):
            for j in range(self.col):
                res += str(self.matrix[i][j]) + " "
            res += "\n"
        return res


if __name__ == "__main__":
    t = int(input())
    while t > 0:
        n, m = map(int, input().split())
        data = [input() for _ in range(n)]
        matrix = Matrix(n, m)
        matrix.input_data(data)
        print(matrix.multiply())
        t -= 1
