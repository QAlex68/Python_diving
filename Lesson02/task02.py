a = 5
print(a, id(a))
a += 1
print(a, id(a))

# txt = 'Hello world!'
# txt[5] = '_'

txt = 'Hello world!'
print(txt, id(txt))
txt = txt.replace(' ', '_')
print(txt, id(txt))


a = c = 2
b = 3
print(a, id(a), b, id(b), c, id(c))
a = b + c
print(a, id(a), b, id(b), c, id(c))

