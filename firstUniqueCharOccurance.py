def firstUniqChar( s):
    """
    :type s: str
    :rtype: int
    """
   
    for i in range(0,len(s)-1):
        temp = s[i]
        
        for j in range(i+1, len(s)):
            if(temp == s[j]):
              
                s= s.replace(s[i], '$')
                s = s.replace(s[j], '$')
                
            
    index = -1      
    for i in range(0,len(s)): 
        if(s[i]!= "$"):
            index = i
            break
    return index         

def Test():
    print("test start...")   
    arr = "starStarstarl"
    print(firstUniqChar(arr))
    print("test end")    

if __name__ =="__main__":
    Test()     