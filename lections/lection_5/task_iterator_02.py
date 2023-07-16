"""next(iterable[, default])"""

data = [2, 4, 6, 8]
list_iter = iter(data)

print(next(list_iter))
print(next(list_iter))
print(next(list_iter))
print(next(list_iter))
# print(next(list_iter)) #StopIteration
print()

data_2 = [2, 4, 6, 8]
list_iter_2 = iter(data)

print(next(list_iter_2, 56))
print(next(list_iter_2, 56))
print(next(list_iter_2, 56))
print(next(list_iter_2, 56))
print(next(list_iter_2, 56))

