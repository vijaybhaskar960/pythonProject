def generator():

    yield 10
    yield 20
    yield 30
    yield 40

g  = generator()
print(next(g))

for i in g:
    print(i)