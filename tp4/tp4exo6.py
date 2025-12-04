L = [5, 2, 4, 8, 1, 3]
N = len(L)

print(f"Phase 0 {L}")

for i in range(N):

    for j in range(0, N-i-1):
        if L[j] > L[j+1]:
          
            temp = L[j]
            L[j] = L[j+1]
            L[j+1] = temp
    print(f"Etape {i+1} {L}")

