def firstUniqChar( s):
    """
    :type s: str
    :rtype: int
    """
    
    for i in range(0,len(s)-1):
        
        count = 0
        for j in range(i, len(s)):
            if(s[i] == s[j]):
                count +=1
        if(count == 1):
            return i
            
    return -1      
         

def Test():
    print("test start...")   
    arr = "starstarstarl"
    print(firstUniqChar(arr))
    print("test end")    

if __name__ =="__main__":
    Test()     