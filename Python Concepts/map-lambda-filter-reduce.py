# lambda
# lambda arguments: expression


def square(n):
    return n ** 2

#alternate way of defining a function using lambda
square = lambda n: n ** 2

#returning max of 2 integers using lambda
maxi = lambda x, y: x if x > y else y

# ---------------------------------------------------------------------------------------------------

# Map
# map(function, iterable)
# The map function takes in a function and an iterable(list, tuple, etc.) as an input; applies passed function to each item of an iterable and returns a map object(an iterator).


squares = list(map(lambda n: n ** 2, range(1, 10, 2)))


# ---------------------------------------------------------------------------------------------------

#filter(function, iterable)
#It works similarly to the map. It returns a filter object, unlike a map object.



nums = [1, 34, 23, 56, 89, 44, 92]
odds = list(filter(lambda x: x % 2 != 0, nums))
print(odds)
# Output: [1, 23, 89]



# ---------------------------------------------------------------------------------------------------

#Reduce applies function iteratively to the iteratable , and produces a single value 
#reduce(function, iterable, [, initializer])

nums = [1, 2, 3, 4, 5]
summ = reduce(lambda x, y: x + y, nums)