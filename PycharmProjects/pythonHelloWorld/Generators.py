#Unlike list, generators do not hold all values , once you call next or loop you will get value;

def square_numbers(nums):
    result=[]
    for i in nums:
        result.append(i*i)

    return result


num=square_numbers([1,2,3,4,5])
print(num)

#Generator
def square_number(nums):
    for i in nums:
        yield i*i


nums=square_number([1,2,3,4,5])

print(next(nums))

for num in nums:
 print(num)



