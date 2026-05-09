class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        # 将数组转为集合,去重并且可以实现O(1)查找
        nums_set = set(nums)
        # 定义最长连续序列的长度
        max_count = 0
        # 遍历集合中的元素
        for num in nums_set:
            # 只有当 num-1不在集合中时,才让num作为起点来找最长子序列,这样可以实现访问过的数不再访问
            if num - 1 not in nums_set:
                # 定义起点,避免修改原始num
                num_new = num
                # 定义当前连续序列的长度,避免直接修改原始长度
                count_new = 1  # 进入此分支说明长度至少为1
                # 从起点往后找,只要num_new+1在集合中就继续找
                while num_new + 1 in nums_set:
                    num_new += 1
                    count_new += 1
                # 到这里说明找完了一条连续序列,那么比较并更新最长连续序列的长度
                max_count = max(max_count, count_new)
        # 返回最长连续序列的长度
        return max_count