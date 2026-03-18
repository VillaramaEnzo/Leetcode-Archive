/**
 * @param {string} s
 * @return {number}
 */
var maximumLength = function(s) {
  const n = s.length;
    let maxLength = -1;

    // Iterate over possible lengths of substrings, from longest to shortest
    for (let len = n; len >= 1; len--) {
        const freqMap = new Map();
        let foundValid = false;

        // Count the frequency of substrings of length `len`
        for (let i = 0; i <= n - len; i++) {
            const sub = s.slice(i, i + len);

            // Check if the substring is special (all characters are the same)
            if (sub[0].repeat(len) === sub) {
                freqMap.set(sub, (freqMap.get(sub) || 0) + 1);

                // If a valid substring is found, stop early for this length
                if (freqMap.get(sub) >= 3) {
                    maxLength = len;
                    foundValid = true;
                    break;
                }
            }
        }

        if (foundValid) break; // Stop checking shorter lengths
    }

    return maxLength;
};