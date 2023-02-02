def generator():

    yield 10
    yield 20
    yield 30
    yield 40


g = generator()
print(next(g))

for i in g:
    print(i)


# Example 2

def top_ten():

    n = 1

    while n <= 10:
        sq = n*n
        yield sq
        n = n+1

m = top_ten()

# print(next(m))
# print(next(m))


for i in m:
    print(i)