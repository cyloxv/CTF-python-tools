'''
若知道栏数，则使用decode解密，若不知道，则使用crack_cipher遍历所有可能性
'''
def generate_w(string, n): 
    '''将字符排列成w型'''
    array = [['.']*len(string) for i in range(n)] #生成初始矩阵
    row = 0
    upflag = False
    for col in range(len(string)): #在矩阵上按w型画出string
        array[row][col] = string[col]
        if row == n-1:
            upflag = True
        if row == 0:
            upflag = False
        if upflag:
            row -= 1
        else:
            row += 1
    return array

def encode(string, n):
    '''加密'''
    array = generate_w(string, n)
    msg = []
    for row in range(n): #将每行的字符连起来
        for col in range(len(string)):
            if array[row][col] != '.':
                msg.append(array[row][col])
    return array, msg

def decode(string, n):
    '''解密'''
    array = generate_w(string, n)
    sub = 0
    for row in range(n): #将w型字符按行的顺序依次替换为string
        for col in range(len(string)):
            if array[row][col] != '.':
                array[row][col] = string[sub]
                sub += 1
    msg = []
    for col in range(len(string)): #以列的顺序依次连接各字符
        for row in range(n):
            if array[row][col] != '.':
                msg.append(array[row][col])
    return array, msg

def crack_cipher(string):
    '''破解密码'''
    for n in range(2,len(string)): #遍历所有可能的栏数
        print(str(n)+'栏：'+''.join(decode(string, n)[1]))

if __name__ == "__main__":
    string = "ccehgyaefnpeoobe{lcirg}epriec_ora_g"
    n = 5 #栏数

    #若不知道栏数，则遍历所有可能
    # crack_cipher(string)

    #若知道栏数
    array,msg = decode(string, n)
    # array,msg = encode(string, n)
    for i in array: print(i)
    print(''.join(msg))
