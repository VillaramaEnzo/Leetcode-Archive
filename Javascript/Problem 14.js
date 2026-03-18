/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function(strs) {
    if (strs.length === 0) return ""; // Edge case: Empty array
    if (strs.length === 1) return strs[0]; // Single string

    // Start with the first string as the potential prefix
    let prefix = strs[0];

    for (let i = 1; i < strs.length; i++) {
        // Reduce the prefix until it matches the beginning of the current string
        while (!strs[i].startsWith(prefix)) {
            prefix = prefix.slice(0, -1);
            if (prefix === "") return ""; // No common prefix exists
        }
    }

    return prefix;
};