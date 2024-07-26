
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        if len(nums)==2:
            return [0,1]

        original_indexed = {i:nums[i] for i in range(len(nums))}
        #print(nums)
        sorted_indexed = {k: v for k, v in sorted(original_indexed.items(), key=lambda item: item[1])}
        nums = [x for x in sorted_indexed.items()]
        #print(sorted_indexed, nums)
        i=0
        j=len(nums)-1
        
        while i < j:
            sum = nums[i][1] + nums[j][1]
            if sum==target:
                return (nums[i][0],nums[j][0])
            if sum < target:
                i += 1
            if sum > target:
                j -= 1


def two_num(nums, target) ->list[int]:

    if len(nums)==2:
        return [0,1]

    for i in range(len(nums)-1, 0, -1):
        first_num = nums[i]
        to_find = target - first_num
        try:
            second_index = nums.index(to_find)
            if i==second_index:
                continue
            return [second_index, i]
        except:
            continue



obj = Solution()
target = 0
nums = [0,2,3,0]
print(obj.twoSum(nums, target))
print(two_num(nums.copy(), target))
