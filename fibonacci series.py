c = int(input("enter your number" ))
d = int(input("enter your range" ))

class fibonacci_series():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def series(self):
        while (True):
            yield (self.b)
            self.a, self.b = self.b, self.a + self.b

f = fibonacci_series(c,d)


for (x) in f.series():
    if x > 100:
        break
    print(x)