"""map(function, iterable)"""
texts = ["Hello", "Здарова", "ПривеТствую"]
res = map(lambda x : x.lower(), texts)
print(*res)