# 给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # 创建一个空字典
        my_dict = {}
        for i in strs:  # 遍历字符串
            key = ''.join(sorted(i))  # 对字符串进行排序并且将排序后的结果作为键
            if key not in my_dict:
                my_dict[key] = []  # 如果键不存在，则创建一个空列表
            my_dict[key].append(i)  # 将字符串添加到对应的键对应的列表中
        return list(my_dict.values())


if __name__ == '__main__':
    # 创建一个Solution对象
    s = Solution()
    res = s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    print(res)
