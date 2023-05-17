from urllib import parse

import os,sys
string =input()

def str_reverse1(ss):
    return ss[::-1]
restr = str_reverse1(string)

# hex2dec
# 十六进制 to 十进制
def hex2dec(string_num):
    return int(string_num.upper(), 16)


print("反向", str_reverse1(string))
print("url解码", parse.unquote(string))
if string.isnumeric():
    print("asc2解码10进制", chr(int(string)))
print("asc2解码16进制", chr(hex2dec(string)))