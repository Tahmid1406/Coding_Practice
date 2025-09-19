class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        s = set(nums)

        max_len = 0

        for v in s:
            start = v 
            end = v

            while end+1 in s:
                end+=1
            
            seq_len = end - start+1
            max_len = max(max_len, seq_len)
        
        return max_len