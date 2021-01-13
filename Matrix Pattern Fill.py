# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 01:20:00 2020

@author: Satyam Patidar MCS20026
"""

def next_l():
    global i
    global strVal
    global PAT_LEN
    s = strVal
    l = PAT_LEN
    s2 = ''
    if i+l<=len(s):
        s2 += s[i:i+l]
        i += l
    else:
        s2 += s[i:]
        s2 += s[:i+l-len(s)]
        i = i+l-len(s)
    return list(s2)

def fill_deepest(a):
    for element in a:
        if len(element) == 0:
            element.extend(next_l())
        else:
            fill_deepest(element)
    if len(a)==0:
        a.extend(next_l())
    return a

def outerFillMyMatrixPat(a):
    global i
    i = 0
    a = fill_deepest(a)
    return a
    
print()

strVal = 'abcdefghijk'
PAT_LEN = 3
print('strVal: ', strVal, '\nPAT_LEN:', PAT_LEN)
print()

myMat0 = []
outerFillMyMatrixPat(myMat0)
print('myMat0: ', myMat0)

myMat1 = [[]]
outerFillMyMatrixPat(myMat1)
print('myMat1: ', myMat1)

myMat2 = [[], [], [], []]
outerFillMyMatrixPat(myMat2)
print('myMat2: ', myMat2)

strVal = 'abcdefghijk'
PAT_LEN = 4
print('strVal: ', strVal, '\nPAT_LEN:', PAT_LEN)
print()

myMat0 = []
outerFillMyMatrixPat(myMat0)
print('myMat0: ', myMat0)

myMat1 = [[]]
outerFillMyMatrixPat(myMat1)
print('myMat1: ', myMat1)

myMat2 = [[], [], [], []]
outerFillMyMatrixPat(myMat2)
print('myMat2: ', myMat2)

strVal = 'abcdefghijk'
PAT_LEN = 5
print('strVal: ', strVal, '\nPAT_LEN:', PAT_LEN)
print()

myMat0 = []
outerFillMyMatrixPat(myMat0)
print('myMat0: ', myMat0)

myMat1 = [[]]
outerFillMyMatrixPat(myMat1)
print('myMat1: ', myMat1)

myMat2 = [[], [], [], []]
outerFillMyMatrixPat(myMat2)
print('myMat2: ', myMat2)

strVal = '0123456789'
PAT_LEN = 2
print('strVal: ', strVal, '\nPAT_LEN:', PAT_LEN)
print()

myMat0 = []
outerFillMyMatrixPat(myMat0)
print('myMat0: ', myMat0)

myMat1 = [[]]
outerFillMyMatrixPat(myMat1)
print('myMat1: ', myMat1)

myMat2 = [[], [], [], []]
outerFillMyMatrixPat(myMat2)
print('myMat2: ', myMat2)


myMatrix2 = [[ [], [] ],
                 [ [] ],
                 [ [], [], []],
                 [ [] ],
                 [ [], [], []],
                 []]
outerFillMyMatrixPat(myMatrix2)
print('myMatrix2\n', myMatrix2)

strVal = 'abcdefghijk'
PAT_LEN = 2
print('strVal: ', strVal, '\nPAT_LEN:', PAT_LEN)
print()

myMatrix3 = [[ [], [] ],
                 [ [] ],
                 [ [], [], []],
                 [ [] ],
                 [ [], [], []],
                 []]
outerFillMyMatrixPat(myMatrix3)
print('myMatrix3\n', myMatrix3)

strVal = '123456789'
PAT_LEN = 0

print('strVal: ', strVal, '\nPAT_LEN:', PAT_LEN)
print()
myMatrix4 = [[ [], [[[[[[]]]]]] ] ]
outerFillMyMatrixPat(myMatrix4)
print('myMatrix4\n', myMatrix4)

