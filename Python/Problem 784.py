class Solution(object):
    def letterCasePermutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        
        results = []

        def backtrack(currentString, index): 

            if index >= len(s):

                results.append(currentString)

                return
            
            if s[index].isalpha():

                backtrack(currentString + s[index].upper(), index + 1)

                backtrack(currentString + s[index].lower(), index + 1)
            
            else: 

                backtrack(currentString + s[index], index + 1)
            
        backtrack("", 0)
        return results
