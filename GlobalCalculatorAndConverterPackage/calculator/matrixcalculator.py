def addition(mat1, mat2):
    temp = []
    temp1= []
    for i in range(len(mat1)):  
        for j in range(len(mat1[0])):
            sum = mat1[i][j] + mat2[i][j]
            temp1.append(sum)
        temp.append(temp1)
        temp1=[]
    return temp

def subtraction(mat1, mat2):
    temp = []
    temp1= []
    for i in range(len(mat1)):  
        for j in range(len(mat1[0])):
            dif = mat1[i][j] - mat2[i][j]
            temp1.append(dif)
        temp.append(temp1)
        temp1=[]
    return temp

def multiplication(mat1, mat2):
    mul = []
    for i in range(len(mat1)): 
        x=[] 
        for j in range(len(mat2[0])):
            tmp=0
            for k in range(len(mat2)):
                tmp += mat1[i][k] * mat2[k][j]
            x.append(tmp)
        mul.append(x)
    print(mul)
    return mul
