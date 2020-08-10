def fn(a, /, b, *args, c, d=2, **kwargs):
    print('a', a)
    print('b', b)
    print('c', c)
    print('d', d)
    print('args')
    for i in range(len(args)):
        print(i, args[i])
    print('kwargs')
    for index in kwargs:
        print(index, kwargs[index])


# fn(4, 1, 3, c=3, k=27)

a = [*'sadfj;']

print(a)
