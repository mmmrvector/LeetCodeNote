

'''
本题采用邻接图及DFS解决。
equations的两个端点可以看做是图中的两个顶点，边的权值即为value值
query相当于查找两个顶点之间的距离，不过距离值为两个顶点之间所有边值的乘积
采用深度优先的方法，从query左端点开始查找，直至找到右端点，需要采用visited数组记录下已经找过的顶点
'''
class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        from collections import defaultdict
        graph = defaultdict(list)
        for i in range(len(equations)):
            graph[equations[i][0]].append((equations[i][1], values[i]))
            graph[equations[i][1]].append((equations[i][0], 1 / values[i]))
        def dfs(cur, target, product, visited):
            if cur in graph:
                if cur == target:
                    return product
                for next, prod in graph[cur]:
                    if next not in visited:
                        visited.add(next)
                        result = dfs(next, target, product * prod, visited)
                        visited.remove(next)
                        if result != -1:
                            return result
            return -1
        res = []
        for i in range(len(queries)):
            res.append(dfs(queries[i][0], queries[i][1], 1, set([queries[i][0]])))
        return res
