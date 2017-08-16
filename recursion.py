def hello(x):
    if x<5:
        hello(x+1)
    print(x)

hello(0)
