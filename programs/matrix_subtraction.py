import  pdb
def read_matrix(m,n):
    temp_matrix = []
    for i in range(0,m):
        temp_matrix_row = []
        for j in range(0,n):
            temp_matrix_row.append(int(input("Enter Element at position row {} col {}:".format(i,j))))
        temp_matrix.append(temp_matrix_row)
    return temp_matrix

def validate_matrix(matrix_a,matrix_b):
    #pdb.set_trace()
    a_row = len(matrix_a)
    b_row = len(matrix_b)
    a_col =set()
    b_col =set()
    if a_row == b_row:
        for row in range(a_row):
            a_col.add(len(matrix_a[row]))
        for row in range(b_row):
            b_col.add(len(matrix_b[row]))
        if len(a_col) > 0 and len(b_col) > 0 and a_col == b_col:
            return True
        else:
            return False
    else:
        print("Invalid Combination")
        return  False



def sub_matrix(matrix_a,matrix_b):
    result_matrix =[]
    if(validate_matrix(matrix_a,matrix_b)):
        for row in range(len(matrix_a)):
            temp_matrix = []
            for col in range(len(matrix_a[row])):
                temp_matrix.append(matrix_a[row][col]-matrix_b[row][col])
            result_matrix.append(temp_matrix)
        return  result_matrix
def disp_matrix(matrix):
    for i in range(len(matrix)):
        print(matrix[i])

# def disp_matrix(matrix):
#     print("matrix size is {}X{}".format(len(matrix),len(matrix[1])))
#     for row in range(0,len(matrix)):
#         print(matrix[row])


if __name__=="__main__":
    m,n=input("Enter dimension of matrix:").split(",")
    m = int(m)
    n = int(n)
    print("Enter Matrix A Elements:")
    matrix_a=read_matrix(m,n)
    print("Enter Matrix B Elements:")
    matrix_b=read_matrix(m,n)
    result_matrix = sub_matrix(matrix_a,matrix_b)
    print("Result of matrix:")
    disp_matrix(result_matrix)




