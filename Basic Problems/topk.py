class Solution:
    def topK(self, nums, k):
        freq_dict = {}
        for num in nums:
            freq_dict[num] = freq_dict.get(num, 0) + 1
        
        freq_list = [(num, freq_dict[num]) for num in freq_dict]

        freq_list.sort(key = lambda x: (-x[1], -x[0]))

        return [freq_list[i][0] for i in range(k)]