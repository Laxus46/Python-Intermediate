def Myrange(start,end):
    current=start
    while current<end:
        yield current
        current+=1


nums= Myrange(1,10)
# print(next(nums))
# print(next(nums))

for num in nums:
    print(num)