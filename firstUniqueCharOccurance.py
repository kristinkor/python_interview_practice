def firstUniqChar( s):
    """
    :type s: str
    :rtype: int
    """
    char_index = {}

    for char in s:
        if char not in char_index:
            char_index[char] = 1
        else:
            char_index[char] +=1
            


    for i in range(0,len(s)):
        if char_index[s[i]] == 1:
            return i
            
    return -1      
         

def Test():
    print("test start...")   
    s = "dddccdbba"
    print(firstUniqChar(s))
    print("test end")    

if __name__ =="__main__":
    Test()     