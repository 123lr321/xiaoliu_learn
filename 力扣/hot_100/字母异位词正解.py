class Solution:
    def groupAnagrams(self, strs):

        # 定义一个字典，用于存储字母异位词分组结果
        anagram_dict = {}

        # 遍历所有单词
        for word in strs:
            # 将单词按照字母顺序排序，并作为键
            sorted_word = ''.join(sorted(word))

            # 如果该键已经在字典中，将当前单词加入到对应的列表中
            if sorted_word in anagram_dict:
                anagram_dict[sorted_word].append(word)
            else:
                # 如果该键不存在，则创建新的列表，并将当前单词加入其中
                anagram_dict[sorted_word] = [word]

        # 返回字典中所有值组成的列表，即为结果
        return list(anagram_dict.values())
