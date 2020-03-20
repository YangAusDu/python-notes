
def task1(n):
    for i in range(n+1):
        print("I am listening to {} song ".format(i))
        yield None



def task2(n):
    for i in range(n+1):
        print("I am eating {} chocolate  ".format(i))
        yield None



def gen():
    i = 0
    while i < 5:
        temp = yield i  #yield is like a temporary return
        print("temp: ",temp)
        i += 1
    return "nothing more"
    


g = gen()
print(next(g))
n1 = g.send(None)
print("n1: " , n1)
n2 = g.send("haha")
print("n2: ",n2)
print(g.__next__())


g1 = task1(10)
g2 = task2(10)
while True:
    try:
        g1.__next__()
        g2.__next__()
    except StopIteration:
        break