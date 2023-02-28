# you are given an array of int and int k
#find indicies of the numbers in array that add up to the val k


#solution 1 On
def solution1(arr: list, k: int)->list:
    hashed_dfferences = {}
    for i in range(len(arr)):
        difference = k - arr[i]
        if(difference in hashed_dfferences):
            return [hashed_dfferences[difference],i]    
        hashed_dfferences[arr[i]] = i    
    return[]

def solution2(arr: list, k: int)->list:
    
    for i in range(len(arr)):
        difference = k - arr[i]
        for j in range(i + 1,(len(arr))):
            if arr[j] == difference:
                return [i,j]    
    return[]    


#solution 2 O(n²)
def Test():
    print("test start...")   
    assert(solution1([2,3,4],6)==[0,2])   
    assert(solution1([2,13,14,19,200],27)==[1,2]) 
    assert(solution1([2,2,2,3],4)==[0,1])  
 
    assert(solution2([2,3,4],6)==[0,2])   
    assert(solution2([2,13,14,19,200],27)==[1,2]) 
    assert(solution2([2,2,2,3],4)==[0,1])  
    print("test end")    

if __name__ =="__main__":
    Test()    


