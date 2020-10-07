def multiply():
    m = int(input('Enter the number of rows in the first matrix: '))
    n = int(input('Enter the number of columns in the first matrix: '))

    a = []
    for i in range(m):
        one_d_array = []
        for j in range(n):
            s = int(input('Enter ' + str(i) + ", " + str(j) + ' element of 1st matrix: '))
            one_d_array.append(s)
        a.append(one_d_array)

    p = int(input('Enter the number of rows in the first matrix: '))
    q = int(input('Enter the number of columns in the first matrix: '))

    b = []
    for i in range(p):
        one_d_array = []
        for j in range(q):
            s = int(input('Enter ' + str(i) + ", " + str(j) + ' element of 2nd matrix: '))
            one_d_array.append(s)
        b.append(one_d_array)

    if n != p:
        return "Matrix Multiplication is not possible!"
    
    c = []
    for i in range(m):
        c.append([0] * p)
    
    for i in range(m):
        for j in range(p):
            for k in range(n):
                c[i][j] += a[i][k] * b[k][j]
    
    return c

if __name__=='__main__':
    result = multiply()
    print(result)