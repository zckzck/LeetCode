# 题目：给定一个数组，求两数之和是目标值的索引。
# 例如 nums = [2,7,11,13] target = 9
# 输出 [0,1]

"""
    思路，使用字典，遍历数组，判断字典中是否有该值，
    如果没有将目标值减去该值作为键，索引值作为值，
    如果存在字典中，返回键的值和当前索引。
"""

nums = [2,5,6,7,11,15]
target = 9
def func(nums,target):
    if len(nums) <= 1:
        return False
    buff_dict = {}
    for i in range(len(nums)):
        if nums[i] in buff_dict:
            return [buff_dict[nums[i]], i]
        else:
            buff_dict[target - nums[i]] = i
print(func(nums,target))