/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var rotate = function(nums, k) {
    
    const n = nums.length

    k = k % n

    function swap(start, end) {

        while (start < end) { 
            [nums[start], nums[end]] = [nums[end], nums[start]];  // Swap elements
            start++;
            end--;
        }

    }

    swap(0, n - 1)
    swap(0, k - 1)
    swap(k, n - 1)


};