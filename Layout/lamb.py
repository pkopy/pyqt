def make_incrementor(n):
    print(n)
    return lambda x: x
class Xman():
    def __init__(self, *args, **kwargs):
        self.args = args
    def connect(self, fn, n):
        fn(n)
# print(make_incrementor)

xman = Xman()
# x = make_incrementor(1)
xman.connect(make_incrementor, 'r')
# make_incrementor('d')