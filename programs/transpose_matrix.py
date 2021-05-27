import pdb
import copy
def read_matrix():
    a,b = input("Enter dimension of matrix:").split(",")
    matrix = []
    for i in range(int(a)):
        temp_lis=[]
        for j in range(int(b)):
            temp_lis.append(input("Enter element at {}:row {}:col :".format(i,j)))
        matrix.append(temp_lis)
    return matrix
def disp_matrix(matrix):
    for i in range(len(matrix)):
        print(matrix[i])
def transpose_matrix(matrix):
    #pdb.set_trace()
    trans_matrix = copy.deepcopy(matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i == j:
                continue
            else:
               trans_matrix[j][i]=matrix[i][j]

    return trans_matrix
if __name__=="__main__":
    matrix = read_matrix()
    disp_matrix(matrix)
    trans_matrix = transpose_matrix(matrix)
    print("transpose of matrix is ")
    disp_matrix(trans_matrix)



