# enumerate returnează un iterator
# cu elemente (index, value)

lst = ["ala", "bala", "porto", "cala"] * 4
for idx, elem in enumerate(lst):
    print(idx, ':', elem)


# also useful: map

# dat fiind range(10, 20)
# calculați o listă cu pătratele numerelor
def square(x):
    return x * x

iterable = range(10, 20)
for elem in map(square, iterable):
    print(elem)

map(square, iterable)
# este echivalent cu
(
    square(elem)
    for elem in iterable
)