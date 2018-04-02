# 1
# 1 2
# 1 2 3
# 1 2 3 4
for i in range(1,5):
    for j in range(1, i+1):
        print(j, end=' ');
    print();


def order(a, b):
    if a<b:
        return a, b
    else:
        return b, a

# not interest, use '_'
_, max = order(7,5)

print(max)