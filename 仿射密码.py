#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encode E(x) = ax + b (mod m)
# decode D(x) = a^{-1} (x - b) (mod m)
def affine(a, b):
    pwd_dic = {}
    for i in range(26):
        pwd_dic[chr(((a*i+b)%26)+97)] = chr(i+97)
    return pwd_dic

if __name__ == '__main__':
    pwd_dic = {}
    pwd = raw_input('Please input miwen : ')
    plain = []
    b = input('Please input b : ')
    for a in range(26):
		if((((ord('f') - 97)*a + b) % 26) == (ord(pwd[0]) - 97)): #5 is the number of f in Alphabet,a is 0;16 is the number of pwd[0] in Alphabet,a is 0
			pwd_dic = affine(a, b)
			print a,b
			for i in pwd:
				plain.append(pwd_dic[i])
				print "You Flag is: " + "".join(plain)
			break
