n=int(input())
q={}
for x in range (n):
    a=input()
    q[x]=a

print()

m=int(input())
w={}
for x in range (m):
    a=input()
    w[x]=a
q_values = set(q.values())
w_values = set(w.values())
d = q_values - w_values

print()

print(len(d))
for t in sorted(list(d)):
    print(t)

