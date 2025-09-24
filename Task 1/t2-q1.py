def matrix_multiplication():
    if cols_A != rows_B:
        print("Error: matrix multiplication is not possible")
    
    result = []
    for i in range(rows_A):
        row = []  
        for j in range(cols_B):
            row.append(0)  
        result.append(row)  


    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(rows_B):
                result[i][j] += A[i][k] * B[k][j]
    
    return result


rows_A,cols_A = map(int, input("Enter rows and columns of first matrix: ").split())

rows_B,cols_B = map(int, input("Enter rows and columns of second matrix: ").split())

print("Enter elements of first matrix row by row")
A=[]
for i in range(rows_A):
    row = list(map(int, input().split()))
    if len(row) != cols_A:
        print("Error: wrong number of elements in a row")
    A.append(row)

print("first matrix is:")
for row in A:
    print(row)

print("Enter elements of second matrix row by row")
B=[]
for i in range(rows_B):
    row = list(map(int, input().split()))
    if len(row) != cols_B:
        print("Error: wrong number of elements in a row")
    B.append(row)

print("second matrix is:")
for row in B:
    print(row)

res=matrix_multiplication()
for row in res:
    print(row)