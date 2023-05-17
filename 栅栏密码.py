'''
遍历所有可能的栏数，并得到加/解密结果
'''
s = 'fa{3c00241528527b69lg32b154eb63ec33d6}'
s = ''
factors = [fac for fac in range(2, len(s)) if len(s)%fac == 0] #取得密文长度的所有因数
for fac in factors:
    flag = ''
    for i in range(fac): #按一定的步长取几组字符，并连接起来，这里组数就等于步长数
        flag += s[i::fac]
    print(str(fac)+'栏：'+flag)