#pypy may be better
#if compare func is min
initial_value = 10**18
#if compare function is max/gcd
#initial_value = 0
class SegTree:
	def __init__(self, N, array=None):
		self.size = 1
		while self.size < N:
			self.size *= 2
		self.n = self.size*2-1
		self.tree = [initial_value]*(self.n)
		if array!=None:
			for i in range(N):
				self.tree[self.n//2+i] = array[i]
			for i in range(self.n//2-1,0,-1):
				self.tree[i] = self.compare(self.tree[2*i+1], self.tree[2*i+2])

	def update(self, i, v):
		#0 index
		# update ith value to v
		i += self.size-1
		self.tree[i] = v
		while i>0:
			i = (i-1)//2
			self.tree[i] = self.compare(self.tree[2*i+1], self.tree[2*i+2]) 
	
	def get(self, l, r, k=0, ll=0, rr=None):
		#0 index
		#return the value of the "compare" in [l, r)
		if rr==None:
			rr=self.size
		if rr<=l or r<=ll: return initial_value
		if l<=ll and rr<=r: return self.tree[k]
		else:
			left = self.get(l, r, 2*k+1, ll, (ll+rr)//2)
			right = self.get(l, r, 2*k+2, (ll+rr)//2, rr)
			return self.compare(left, right) 

	def compare(self, a, b):
		#the condition to return
		#such as min, max, gcd, etc
		return 
		

