# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.



def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    romans = {
        "IV": 4,
        "IX": 9,
        "XL": 40,
        "XC": 90,
        "CD": 400,
        "CM": 900,
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    sum=0
    
    i=0

    while i < len(s):
        if( i+1 <len(s)):
            
            if (s[i] + s[i+1]) in romans:
                
                sum += romans[(s[i] + s[i+1])]
                i+=2

                
            else:
                sum += romans[s[i]]
                i+=1
        else:       
            sum += romans[s[i]]
            i+=1
            
    return sum 


def Test():
    print("test start...")  

    print(romanToInt("III"))
    print(romanToInt("LVIII"))
    print(romanToInt("MCMXCIV"))
    
    print("test end")    

if __name__ =="__main__":
    Test()    
