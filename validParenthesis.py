 
def validateParenthesis(s):
    openlist = {"(":[],
        "{":[],
        "[":[]
    }
    closelist = {")":[],
        "}":[],
        "]":[]
    }
    for i in range(0,len(s)):
        if(s[i] in openlist):
            openlist[s[i]].append(i)
            #openlist.update({s[i]:[i]})
        elif(s[i] in closelist):
            closelist[s[i]].append(i)

    res = True
    
    if len(openlist['(']) == len(closelist[')']) and len(openlist['{']) == len(closelist['}']) and len(openlist['[']) == len(closelist[']']):
        
        if compareTwo(openlist['('], closelist[')']) and compareTwo(openlist['{'], closelist['}']) and compareTwo(openlist['['], closelist[']']):
            return True
    else:
        return False    
    print(openlist)
    print(closelist)

def compareTwo(arr1,arr2):
    for i in range(0, len(arr1)):
        if arr1[i] > arr2[i]:
            return False
    return True

def Test():
    print("test start...")  

    print(validateParenthesis("sdgsfg{{gvdfgd}sgsfg()[]d"))

    
    print("test end")    

if __name__ =="__main__":
    Test()            