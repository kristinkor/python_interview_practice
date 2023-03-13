def decode(s,decode):
    """
    :type s: str
    :rtype: int
    """
    n=6
    result = ""
    temp = ""
    
    for i in range(0, len(s), n):
        
        temp = s[i:i+n]
        
        res = list(filter(lambda x: temp in x, decode))
        
        if(len(res)>0):
            
            if("[newline]" in ' '.join(res)):
                result += "\n"
            else:
                
                result +=str(res[0][0])
        # if temp in decode:
        #     result += decode[0]
    return result        
         

def Test():
    print("test start...")   
    s = "dddccdbba"
    print(decode("111110000001100100111111100101110001111110", ["a 111110", "b 0000011", "[newline] 111111"]))
    print("test end")    

if __name__ =="__main__":
    Test()     