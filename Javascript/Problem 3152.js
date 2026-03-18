/**
 * @param {number[]} nums
 * @param {number[][]} queries
 * @return {boolean[]}
 */
var isArraySpecial = function (nums, queries) {

    const n = nums.length;

    const prefixSum = Array(n).fill(0);
    for (let i = 1; i < n; i++) {
        prefixSum[i] = prefixSum[i - 1] + (nums[i - 1] % 2 !== nums[i] % 2 ? 1 : 0);
    }

    return queries.map(([from, to]) =>
        (prefixSum[to] - prefixSum[from]) === (to - from));
}
