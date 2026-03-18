class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        max_deque = deque()  # To maintain maximum values
        min_deque = deque()  # To maintain minimum values
        total_count = 0

        for right in range(n):
        # Maintain decreasing order in max_deque
            while max_deque and nums[max_deque[-1]] <= nums[right]:
                max_deque.pop()
            max_deque.append(right)

        # Maintain increasing order in min_deque
            while min_deque and nums[min_deque[-1]] >= nums[right]:
                min_deque.pop()
            min_deque.append(right)

        # Ensure the condition |max - min| <= 2
            while nums[max_deque[0]] - nums[min_deque[0]] > 2:
                left += 1
            # Remove invalid indices
                if max_deque[0] < left:
                    max_deque.popleft()
                if min_deque[0] < left:
                    min_deque.popleft()

        # Add the number of valid subarrays ending at 'right'
            total_count += (right - left + 1)

        return total_count