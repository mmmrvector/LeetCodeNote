class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        min_path = [[ 10** 8 for i in range(len(triangle[j])) ] for j in range(len(triangle))]

        min_path[0][0] = triangle[0][0]
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                if j == 0:
                    min_path[i][j] = min_path[i - 1][j] + triangle[i][j]
                else:
                    if len(min_path[i - 1]) > j:
                        min_path[i][j] = min(min_path[i - 1][j] + triangle[i][j], min_path[i - 1][j - 1] + triangle[i][j])
                    else:
                        min_path[i][j] = min_path[i - 1][j - 1] + triangle[i][j]
        return min(min_path[len(triangle) - 1])
s = Solution()
print(s.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))