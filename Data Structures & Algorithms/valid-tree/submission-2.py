class Solution:

    def dfs(self, curr, prev, visited, adj):
        if curr in visited: return False
        visited.add(curr)

        for neigh in adj[curr]:
            if neigh == prev: continue
            if not self.dfs(neigh, curr, visited, adj): return False
        return True

    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
    
        visited = set()
        return self.dfs(0, -1, visited, adj) and len(visited) == n