
def MyGenerator():
    for i in range(1,10):
        value=yield i
        yield value

gen=MyGenerator()
print(next(gen))
print(gen.send("I am Value"))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))