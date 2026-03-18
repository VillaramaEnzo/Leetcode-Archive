from collections import defaultdict


class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:

        count = defaultdict(int)
        for num in nums:
            count[num] += 1

        sorted_keys = sorted(count.keys())
        max_beauty = 0
        current_count = 0
        left = 0
        keys = list(sorted_keys)

        for right in range(len(keys)):
      
            current_count += count[keys[right]]


            while keys[right] - keys[left] > 2 * k:
                current_count -= count[keys[left]]
                left += 1

            max_beauty = max(max_beauty, current_count)

        return max_beauty