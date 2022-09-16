# def gen(n):
#     for i in range (n):
#         yield i**2

# it=gen(30)
# print(it)
# print(it.__next__())
# print(it.__next__())
# print(next(it))
# print(next(it))

def gen(n):

    yield n

a=gen(5)

for i in range(3):

    print(a.__next__)


