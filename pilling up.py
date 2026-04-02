
from collections import deque

def solve():
    try:
        t_str = input().strip()
        if not t_str:
            return
        t = int(t_str)
        
        for _ in range(t):
            n = int(input())
            d = deque(map(int, input().split()))
            
            last_picked = float('inf')
            possible = True
            
            while d:
                if d[0] >= d[-1]:
                    current = d.popleft()
                else:
                    current = d.pop()
                if current > last_picked:
                    possible = False
                    break
                
                last_picked = current
            
            print("Yes" if possible else "No")
    except EOFError:
        pass

if __name__ == "__main__":
    solve()
