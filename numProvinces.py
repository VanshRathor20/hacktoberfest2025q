class Solution:
    def numProvinces(self, adj, V):
        visited = [False] * V
        
        def dfs(city):
            visited[city] = True
            for neighbor in range(V):
                if adj[city][neighbor] == 1 and not visited[neighbor]:
                    dfs(neighbor)
        
        count = 0
        for city in range(V):
            if not visited[city]:
                dfs(city)
                count += 1
        return count
