def f1(x):
    def f2(x):
        return x+10
    print(x)
    print(f2(x))


f1(5)
