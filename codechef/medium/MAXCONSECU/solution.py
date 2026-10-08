def findMaxConsecutiveOnes(nums): 
    c,d=1,1 
    for i in range(1,len(nums)):
        if nums[i]==nums[i-1]:
            c+=1
            d=max(d,c)
        else:
            c=1 
    return (d)
   # write code here...