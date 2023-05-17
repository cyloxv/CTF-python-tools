string =input()
def hex2dec(string_num):
    return int(string_num.upper(), 16)

def str_url(sss):
    flag = ''
    for i in range(0, len(sss), 2):
        s = sss[i] + sss[i + 1]
        flag += chr(hex2dec(s))
    return flag

def str_reverse1(ss):
    return ss[::-1]
restring = str_reverse1(string)

print("asc2解码16进制", str_url(string))
print("asc2解码16进制--反向", str_url(restring))