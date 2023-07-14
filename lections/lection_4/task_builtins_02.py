"""filter(function, iterable)"""
numbers = [42, -43, 1024]
res = tuple(filter(lambda x: x > 0, numbers))
print(res)