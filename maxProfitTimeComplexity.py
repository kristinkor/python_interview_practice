

def maxProfit(prices):
    lowerPrice = prices[0]
    profit = 0
    i = 1

    while(i < len(prices)):
        cost = prices[i] - lowerPrice
        if (profit < cost):
            profit = cost
        if(lowerPrice > prices[i]):
            lowerPrice = prices[i]
            
        i+=1    
    return profit 

def Test():
    print("test start...")   
    arr = [345,1,3,6,8,5,3,5,67,9,46,8,44]
    print(maxProfit(arr))
    print("test end")    

if __name__ =="__main__":
    Test() 