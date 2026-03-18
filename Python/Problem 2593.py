class Solution:
    def findScore(self, nums: List[int]) -> int:
        sorted_nums = sorted((val, idx) for idx, val in enumerate(nums))
    
        marked = set()  
        score = 0

   
        for value, index in sorted_nums:
            if index in marked:
                continue  
        
            score += value

            marked.add(index)
            if index > 0:
                marked.add(index - 1)
            if index < len(nums) - 1:
                marked.add(index + 1)

        return score