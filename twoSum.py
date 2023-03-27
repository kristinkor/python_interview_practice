from typing import List
def twoSum(nums: List[int], target: int) -> List[int]:
    elements = dict()   
    
    for index, value in enumerate(nums):
        res = target- value
    
        if res in elements:
            return [elements[res], index]
    
    
        elements[value] = index

    return []  

def Test():
    print("test start...")   
    arr = [1,3,6,8,5,3,5,67,9,0,46,8,345,44]
    print(twoSum(arr,389))
    print("test end")    

if __name__ =="__main__":
    Test()     