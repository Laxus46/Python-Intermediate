outer=[]
for i in range(10):
    inner=[]
    for j in range(i):
        inner.append(j*3)
        
    outer.append(inner)
print(outer)


#using nested comprehension

y=[[j*3 for j in range (i)] for i in range(10)]
print(y)