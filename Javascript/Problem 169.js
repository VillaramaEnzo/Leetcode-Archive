/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
    
    let m = null;
    let count = 0;

    for (let num of nums) {

        if (count === 0) {

            m = num
            
        }

        count += (num === m) ? 1 : -1

    }

    return m

};