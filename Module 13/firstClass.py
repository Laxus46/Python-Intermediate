def square(x):
    return x*x

#f=square(5)
#print(square)
#print(f)

#case ii
f=square
print(square)
print(f)
print(f(5))

#let's take an example of map function with take func and array 

def Map(func,arr_list):
    result=[]
    for i in arr_list:
        result.append(func(i))
    return result

test=Map(square,[1,2,3,4,5,6])
print(test)

