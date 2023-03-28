def sortSentence(s):
    """
    :type s: str
    :rtype: str
    """
    words = s.split()
    i = 1
    new_s=""
    thisdict ={}
    for word in words:
        for i in word:
            if(i.isdigit()):
                word = word.replace(i,"")
                thisdict[i] = word
            
    for key in sorted(thisdict):
        new_s += (thisdict[key]) + " "
    new_s = new_s[:-1]
    return new_s 


def Test():
    print("test start...")   
    s = "Myself2 Me1 I4 and3"
    print(sortSentence(s))
    print("test end")    

if __name__ =="__main__":
    Test()      