


# Solve linear equation using Gaussian elimination.
def gaussian_elimination(n, matrix):
    res = [0 for i in range(n)]

    for row in range(n):
        if matrix[row][row] == 0.0:
            raise ZeroDivisionError("Divide by zero detected")
        
        for column in range(row+1, n):
            ratio = matrix[column][row] / matrix[row][row]

            for i in range(n+1):
                matrix[column][i] = matrix[column][i] - ratio * matrix[row][i]

    res[-1] = matrix[n-1][n] / matrix[n-1][n-1]


    for row in range(n-2, -1, -1):
        res[row] = matrix[row][n]

        for column in range(row+1, n):
            res[row] = res[row] - matrix[row][column]  * res[column]
        res[row] = res[row] / matrix[row][row]
    
    return res



if __name__ == "__main__":
    
    matrix = []

    n = int(input("Enter Number of Unknowns : "))

    # Takes Coefficients and create a mateix of ( n x n+1 ).
    for i in range(n):
        row = []
        for num in input("Enter Matrix Coefficients : ").strip().split():
            row.append(float(num))
        matrix.append(row)

    res = gaussian_elimination(n, matrix)

    print(res)