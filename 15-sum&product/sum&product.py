def get_matrix(rows, cols):
    mat = []

    for i in range(rows):
        row = input(f"Enter the elements of row {i+1} separated by space: ")
        row = row.split(" ")
        if len(row) != cols:
            print("Error: Invalid number of elements in row.")
            return None
        row = [int(x) for x in row]
        mat.append(row)

    return mat

def matSumProt():
    rows1 = int(input("Enter the number of rows in the first matrix: "))
    cols1 = int(input("Enter the number of columns in the first matrix: "))
    rows2 = int(input("Enter the number of rows in the second matrix: "))
    cols2 = int(input("Enter the number of columns in the second matrix: "))
    
    if cols1 != rows2:
        print("Error: The matrices are not compatible for addition and multiplication.")
        return None

    print("Enter the elements of the first matrix:")
    mat1 = get_matrix(rows1, cols1)
    print("Enter the elements of the second matrix:")
    mat2 = get_matrix(rows2, cols2)

    if mat1 is None or mat2 is None:
        return None

    sum_mat = [[0 for j in range(cols1)] for i in range(rows1)]
    prod_mat = [[0 for j in range(cols2)] for i in range(rows1)]

    for i in range(rows1):
        for j in range(cols1):
            sum_mat[i][j] = mat1[i][j] + mat2[i][j]
            for k in range(cols2):
                prod_mat[i][k] += mat1[i][j] * mat2[j][k]

    return (sum_mat, prod_mat)


result = matSumProt()
if result is not None:
    print("The sum of the matrices is:")
    for row in result[0]:
        print(row)
    print("The product of the matrices is:")
    for row in result[1]:
        print(row)
