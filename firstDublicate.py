'''
Created on 17 апр. 2018 г.

@author: eq
'''
#a = [8, 4, 6, 2, 6, 4, 7, 9, 5, 8]

def firstDuplicate(a):
    result = a.__iter__()
    next(result)
    for i in range(len(a)):
        try:
            if a.count(a[i]) > 1:
                if a[i] == next(result) :
                    return a[i]
            else:
                continue
        except Exception:
            continue
    return -1 
