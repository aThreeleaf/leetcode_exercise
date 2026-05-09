"""
给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。请你返回所有和为 0 且不重复的三元组。

注意：答案中不可以包含重复的三元组。
"""


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # 排序，以便去重和查找
        nums.sort()
        list1 = []
        # 存储数组长度
        length = len(nums)
        # 遍历数组
        for i in range(length - 2):
            # 如果第一个数>0则后面的数也大于0，和不可能为0
            if nums[i] > 0:
                break
            # 如果当前数和前一个数相等，则跳过
            # i>0确保当前数不是第一个数
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1  # 左指针指向当前数后面的数
            right = length - 1  # 右指针指向数组末尾
            target = -nums[i]
            # 循环判断
            while left < right:
                # 存储求和结果
                sum1 = nums[left] + nums[right]
                # 如果和等于target,则将结果添加到结果列表中
                if sum1 == target:
                    list1.append([nums[i], nums[left], nums[right]])
                    # 循环判断第二个数的下一个值是否和当前值相等
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # 循环判断第三个数的前一个值是否和当前值相等
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    # 移动指针,必须同时移动，如果只移动一边，都会导致和变大或者和变小
                    left += 1
                    right -= 1
                # 如果和大于target，说明第三个数大了，则将右指针左移
                elif sum1 > target:
                    right -= 1
                # 如果和小于0，说明第二个数小了，则将左指针右移
                elif sum1 < target:
                    left += 1

        # 返回结果
        return list1


if __name__ == '__main__':
    # nums = [-1, 0, 1, 2, -1, -4]
    # nums = [0,1,1]
    # nums = [0, 0, 0]
    # nums = [-100, -70, -60, 110, 120, 130, 160]
    nums = [-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4]
    print(Solution().threeSum(nums))
