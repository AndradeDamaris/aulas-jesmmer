# T = int(input())
# N = [T]
# for i,v in enumerate(N):
#     N[i] = T
#     if N[i] < T:
        
#         N.append()
    
# print(N)

T = int(input())
N = [T] 
for i in range(10):
    if N[i] == T:
        N[i] = 0
    else:
        dif = N[i]+1
        N.append(dif)
        
for i,v in enumerate(N):
    print(f'N[{i}] = {v}')