def read_matrix(row,col):
    temp_matrix = []
    for i in range(row):
        temp_row = []
        for j in range(col):
            temp_row.append(int(input("Enter Element at row {} col {}".format(i,j))))
        temp_matrix.append(temp_row)
    return temp_matrix

def matrix_display(mat):
    for i in range(len(mat)):
        print(mat[i])


if __name__ == "__main__":
    result_matrix =[]
    mat1_row,mat1_col = input("Enter order matrix 1:").split(",")
    mat_a = read_matrix(int(mat1_row),int(mat1_col))
    mat2_row,mat2_col = input("Enter order matrix 2:").split(",")
    mat_b = read_matrix(int(mat2_row),int(mat2_col))
    print("Matrix A elements are")
    matrix_display(mat_a)
    print("Matrix B elements are")
    matrix_display(mat_b)
    if mat1_col == mat2_row:
        for i in range(int(mat1_row)):
            mat_res = []
            print("printing i:",i)
            for j in range(int(mat2_col)):
                print("printing j:",j)
                sum = 0
                for k in range(int(mat2_row)):
                    print("printing k:",k)
                    sum += mat_a[i][k] * mat_b[k][j]
                mat_res.append(sum)
            result_matrix.append(mat_res)
        print("result of matrix",len(mat_res))
        matrix_display(result_matrix)
    else:
        print("Invalid Matrix")



