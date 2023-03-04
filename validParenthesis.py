 
def validateParenthesis(s):
        parenthesis = {"(":")",
            "{":"}",
            "[":"]"
        }

        stack = []

        if (len(s)%2 != 0):
            return False

        for i in s:
            if i in parenthesis.keys():     
                stack.append(i)
                #openlist.update({s[i]:[i]}) 
            else:
                if stack == []:     
                    return False
                elif (len(stack) > 0): 
                    if ( i != parenthesis[stack.pop()]):
                        return False

                    
        return stack == []  

def Test():
    print("test start...")  

    print(validateParenthesis("()([]){[]}{}"))

    
    print("test end")    

if __name__ =="__main__":
    Test()            