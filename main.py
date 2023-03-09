
def twoSum(nums, target):
    
    break_ = False
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] + nums[j] == target:
                break_check = True
                listt=[i,j] 
                return listt
                break
        if break_:
            break


nums = list(map(int, input().split()))

target = int(input())

print(twoSum(nums,target))
