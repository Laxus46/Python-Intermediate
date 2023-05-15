# i want a (letter,num) pair for each letter in 'abcd' and each number in '0123'
my_list=[]
for letter in 'abcd':
    for num in range(4):
        my_list.append((letter,num))
print (my_list)

print("using list comprehension-------")
#using list comprehension

a=[(letter,num)for letter in 'abcd' for num in range(4)]
print(a)


#using dictionary comprehension

#zip takes two list as input and tuples as output
print("using two list")
name=['A','B','C','D']
age=[12,13,15,10]

a={name:age for name,age in  zip(name,age)}
print(a)

#using generator comprehension

a_list=[1,2,3,4,5,6,7,8,9,10]

def gen_fun(a_list):
    for num in a_list:
        yield num*num

my_gen=gen_fun(a_list)

for i in my_gen:
    print(i)

sq=(x**2 for x in range(10))
print(type(sq))
print(list(sq))
