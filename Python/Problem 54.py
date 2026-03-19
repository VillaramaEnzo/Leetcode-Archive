class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        ret = []

        while matrix:

            ret += (matrix.pop(0))

            if matrix and matrix[0]:
                ret += [row.pop() for row in matrix]
        
            if matrix:
                ret += (matrix.pop()[::-1])
        
            if matrix and matrix[0]:

                ret += ([row.pop(0) for row in matrix[::-1]])
        
        return ret
    
        

        