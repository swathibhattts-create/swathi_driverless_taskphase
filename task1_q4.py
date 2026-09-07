def matrix_multiply(A,B):
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])
    if cols_A != rows_B:
        print("Error: Number of columns in A must be equal to number of rows in B.")
        return None
    result = [[0 for j in range(cols_B)] for i  in range(rows_A)]
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]
    return result
input_A=input('enter the matrix A') 
A = [list(map(int,r.split())) for r in input_A.split(',')]
input_B=input('enter the matrix B')
B=[list(map(int,r.split())) for r in input_B.split(',')]

print(matrix_multiply(A,B))


    
        
    