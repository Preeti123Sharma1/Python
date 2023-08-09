# String Iteration in Python
w = 'Welcome to Lucknow'

a = len(w)
print(a)
for t in range(a):
    print(w[t])


print(" ")

for t in range(a-1,-1,-1):              # (total index -1, -1 means we go to 0 index, we have to decrement -1)
    print(w[t])