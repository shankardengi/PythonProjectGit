def accept_matrix_input(x,y):
    matrix_input=[]
    for i in range(0,x):
        temp_list =[]
        for j in range(0,y):
                temp_list.append(int(input("Enter matrix elemts  at {} row {} column :".format(i,j))))
        matrix_input.append(temp_list)
    return matrix_input

def display_matrix(matrix):
    print("matrix size is {}X{}".format(len(matrix),len(matrix[1])))
    for row in range(0,len(matrix)):
        print(matrix[row])

def add_matrix(matrix_a,matrix_b):
    result=[]
    for row in range(0,len(matrix_a)):
        temp = []
        for col in range(0,len(matrix_a[row])):
            temp.append((matrix_a[row][col]+matrix_b[row][col]))
        result.append(temp)
    return result



if __name__ =="__main__":
    x,y = input("Enter size of matrix:").split(",")
    x = int(x)
    y = int(y)
    matrix_a=accept_matrix_input(x,y)
    matrix_b=accept_matrix_input(x,y)
    print(len(matrix_a))
    print(len(matrix_a[1]))
    display_matrix(matrix_a)
    display_matrix(matrix_b)
    result = add_matrix(matrix_a,matrix_b)
    print("sum of two matrix is:")
    display_matrix(result)

