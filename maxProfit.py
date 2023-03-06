#Given an array prices representing stock prices for each day, 
#find the maximum profit that can be obtained by buying and selling the stock once. 
#If no profit can be made, return 0.


def maxProfit(prices):

    firstDay = 0
    lastDay = len(prices)-1
    sum = 0
    arrOfSums=[] 


    if len(prices) > 1:
        while firstDay < lastDay: 
            while lastDay > firstDay:
                if prices[lastDay] >= prices[firstDay]:
                    sum = prices[lastDay] - prices[firstDay]
                    arrOfSums.append(sum)  
                firstDay +=1 
                
            firstDay = 0    
            lastDay -= 1   
        if (len(arrOfSums)) != 0:            
            maxProfit = max(arrOfSums)              
            if maxProfit < 0:
                return 0   
            else:
                print(arrOfSums)
                return max(arrOfSums) 
        else:
            return 0        
    else: 
        return 0        


def Test():
    print("test start...")   
    arr = [1,3,6,8,5,3,5,67,9,0,46,8]
    print(maxProfit(arr))
    print("test end")    

if __name__ =="__main__":
    Test() 