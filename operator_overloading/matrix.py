class Matrix(object):
    def __init__(self, mat):
        self.mat = mat

    def __add__(self, other):
        if len(self.mat) != len(other.mat) or len(self.mat[0]) != len(other.mat[0]):
            raise ValueError("Invalid matrix size")
        result = [[0]*len(self.mat[0])]*len(self.mat)
        for row in range(len(self.mat)):
            for col in range(len(self.mat[0])):
                result[row][col] = self.mat[row][col] + other.mat[row][col]
        return result

    def __sub__(self, other):
        if len(self.mat) != len(other.mat) or len(self.mat[0]) != len(other.mat[0]):
            raise ValueError("Invalid matrix size")
        result = [[0] * len(self.mat[0])] * len(self.mat)
        for row in range(len(self.mat)):
            for col in range(len(self.mat[0])):
                result[row][col] = self.mat[row][col] - other.mat[row][col]
        return result

    def __mul__(self, other):
        if len(self.mat) != len(other.mat[0]):
            raise ValueError("Invalid matrix size")
        results = [[1] * len(self.mat[0])] * len(self.mat)
        for i in range(len(self.mat)):
            for j in range(len(self.mat[0])):
                result = 0
                for k in range(len(self.mat[0])):
                    result = result + self.mat[i][j]*other.mat[j][i]
                results[i][j] = result
        return results

mat1 = [[1,1,1], [1,1,1], [1,1,1]]
mat2 = [[1,1,1], [1,1,1], [1,1,1]]
obj1 = Matrix(mat1)
obj2 = Matrix(mat2)
print(obj1+obj2)
print(obj1-obj2)
print(obj1*obj2)
