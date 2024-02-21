from flask import Flask

app = Flask('app')
def foo_bar(x):
    for i in range(1, x + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FooBar")
        elif i % 3 == 0:
            print("Foo")
        elif i % 5 == 0:
            print("Bar")
        else:
            print(i)

foo_bar(30)
