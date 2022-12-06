#!\usr\bin\env python 3
# -*- coding: utf-8 -*-

def search_null(s):
    strsp = ([int(x) for x in s.split(' ')])
    a = 1
    b = 0
    for i in range(len(strsp)): 
        if i == 0:
            if strsp[i] == 0:
                b +=1
                a = 1
            else:
                strsp[i] = a
        else:
            if strsp[i] == 0:
                a = 1
                if b == 0:
                    b += 1
                    for x in range(i,0,-1):
                            strsp[x-1] = strsp[x]+1
                else:
                    for x in range(i,1,-1):
                        if strsp[x] < strsp[x-1]:
                            strsp[x-1] = strsp[x]+1
                        else:
                            continue
            else:
                strsp[i] = a
                a += 1
    return(" ".join(map(str, strsp)))

    
print(search_null(input()))
