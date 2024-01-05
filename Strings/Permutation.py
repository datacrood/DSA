def isPermutation(string1, string2) :
    flag = True
    if len(string1) == len(string2):
        for char1 in string1:
            if char1 in string2:
                # index_str2 = string2.find(char1,k)
                pass
                # k+=1
            else:
                flag = False
    return True if flag else False
print(isPermutation("race", "raec"))
