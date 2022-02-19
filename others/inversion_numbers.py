class BIT:
  def __init__(self, N):
    self.size = N
    self.data = [0]*(N+1)
  

  def sum(self, r):
    s = 0
    while r>0:
      s += self.data[r]
      r -= r&-r
    return s
  
  def add(self, i, x):
    while i<=self.size:
      self.data[i] += x
      i += i&-i 

def cnt_inv(A, N=0):
  if N==0:
    N = len(A)
  bit = BIT(N)
  s = N*(N-1)//2
  for i in A:
    s -= bit.sum(i)
    bit.add(i, 1)
  return s




def main():
  N = int(input())
  A = [int(i) for i in input().split()]
  print(cnt_inv(A))


main()