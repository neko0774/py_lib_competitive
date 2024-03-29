from heapq import heappush, heappop
inf = 10**18

def dijkstra(s, G, node=None):#s = start, n = number of the node
	if node==None: node = len(G)
	cost = [inf]*node
	hq = [(0, s)]
	seen = [False]*node
	cost[s] = 0
	while hq:
		d, v = heappop(hq)
		seen[v] = True
		if d>cost[v]: continue
		for to, weight in G[v]:
			if not seen[to] and cost[v] + weight < cost[to]:
				cost[to] = cost[v] + weight
				heappush(hq, (cost[to], to))
	return cost

# ノード数, エッジ数, 始点ノード
V, E, r = map(int, input().split())
# adj[s]: ノード s に隣接する(ノード, 重み)をリストで持つ
G = [[] for _ in range(V)]
for i in range(E):
	s, t, d = map(int, input().split())
	G[s].append((t, d))
	#G[t].append((s, d))

l = dijkstra(r, G)
for i in l:
	print("INF" if i==inf else i)

#ref
#https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/1/GRL_1_A