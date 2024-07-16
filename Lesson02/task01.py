a = 5
print(type(a), id(a))
a = "hello world"
print(type(a), id(a))
a = 42.0 * 3.141592 / 2.71828
print(type(a), id(a))


data = 42
print(isinstance(data, int))

data = True
print(isinstance(data, int))

data = 3.14
print(isinstance(data, (int, float, complex)))


num = 2 + 2 * 2
digit = 36 / 6
print(num, digit)
print(num == digit)
print(num is digit)

