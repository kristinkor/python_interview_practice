def decode(s,decode):
    """
    :type s: str
    :rtype: int
    """
    mapping = {}
    res = ""
    for item in decode:
        if item.startswith("[newline]"):
            char, code = "\\n", item.split()[1]
        else:
            char, code = item.split()
        mapping[code] = char

   
    i = 0
    while i < len(s):
        for code in mapping:
            if s[i:i+len(code)] == code:
                if mapping[code] == "\\n":
                    res += "\n"
                else:
                    res += mapping[code]
                i += len(code)
                break
        else:
            # If no code is found, skip ahead one bit
            i += 1
    return res      

            

def Test():
    print("test start...")   
    s = "dddccdbba"
    print(decode("111110000001100100111111100101110001111110", ["a	100100", "b	100101", "p 111110", "c	110001", "d	100000"]))
    print("test end")    

if __name__ =="__main__":
    Test()     