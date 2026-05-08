class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        # left指向已处理元素的末尾
        left = 0  # 初始为0
        # 遍历数组
        for right in range(len(nums)):
            # 遇到非0元素就交换
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                # 更新已处理元素的末尾
                left += 1
        # 打印结果
        print(nums)


if __name__ == '__main__':
    s = Solution()
    s.moveZeroes([0, 1, 0, 3, 12])
    s.moveZeroes([0])
