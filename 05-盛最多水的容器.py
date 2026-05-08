"""
给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。

找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

返回容器可以储存的最大水量。

说明：你不能倾斜容器。
"""


class Solution:
    def maxArea(self, height: list[int]) -> int:
        # left指向最左边,right指向最右边
        left, right = 0, len(height) - 1
        # 记录最大容量
        max_area = 0
        # 只要left<right就循环判断
        while left < right:
            # 如果左边更高
            if height[left] > height[right]:
                area = (right - left) * height[right]  # 计算容量，用短的那边作为高
                # 更新最大容量
                max_area = max(max_area, area)
                # 让短的那边往左靠
                right -= 1
            #  如果右边更高或相等
            else:
                area = (right - left) * height[left]
                # 更新最大容量
                max_area = max(max_area, area)
                # 让短的那边往右靠
                left += 1
        # 返回最大容量
        return max_area


if __name__ == '__main__':
    # height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    # height = [1, 1]
    height = [5, 1, 5]
    print(Solution().maxArea(height))
