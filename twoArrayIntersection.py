from typing import List

def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
    thislist = []
    
    for i in nums1: 
        if i in nums2:
            thislist.append(i)
    new_list = list(set(thislist))   
    return   new_list 

def Test():
    print("test start...")   
    a1 = [1,2,3,4,5,4,5]
    a2 = [4,5,6,7,8,1,2]
    print(intersection(a1,a2))
    print("test end")    

if __name__ =="__main__":
    Test()     