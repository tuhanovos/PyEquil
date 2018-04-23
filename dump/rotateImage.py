def rotateImage(a):
    a2 = zip(*a)
    result = []
    for i in a2:
    	result.append(list(i)[::-1])


    return result

a = [[10,9,6,3,7], 
 [6,10,2,9,7], 
 [7,6,3,8,2], 
 [8,9,7,9,9], 
 [6,8,6,8,2]]

print(rotateImage(a))