import sys

class Klasa:
    def __init__(self, x):
        self.x = x

    def string(self, s):
        return self.x.join(s)


class Inna:
    def __str__(self):
        return "Siema zio0m"


i = Inna()
print(i)

k = Klasa("siema")
print(k.string(sys.argv))


