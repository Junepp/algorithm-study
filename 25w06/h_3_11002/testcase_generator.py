import random

N = random.randint(30, 30)
M = random.randint(30, 30)

with open('testcase.txt','w') as f:
    f.write(f"{N} {M}\n")

    for i in range(N):
        n = random.randint(0, 2**M - 1)
        n = bin(n)[2:]
        n = n.rjust(M, "0")
        
        f.write(f"{n}\n")
