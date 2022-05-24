class Spam:
    def __init__(self,n): self.n = n
    def __lt__(self, other): return self.n < other.n
    def __repr__(self):return f'Spam({self.n})'

l = [Spam(n) for n in range(5,0,-1)]
print(sorted(l))