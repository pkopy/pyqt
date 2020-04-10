from typing import List
from typing import TypeVar, Generic
from logging import Logger

def greeting(name: str) -> str:
    return 'Hello ' + name

print(greeting('1'))



Vector = List[float]

def scale(scalar: float, vector: Vector) -> Vector:
    return [scalar * num for num in vector]

# typechecks; a list of floats qualifies as a Vector.
new_vector = scale(2, [1.0, -4.2, 5.4])
print(new_vector)

T = TypeVar('T')

class Test(Generic[T]):
    def __init__(self, value: T, name: str) -> None:
        self.name = name
        self.value = value

    def set(self, new: T) -> None:
        
        self.value = new
        print('Set ' + repr(self.value))

    def get(self) -> T:
        print('Get ' + repr(self.value))
        return self.value

    def log(self, message: str) -> None:
        print('%s: %s', self.name, message)

test = Test(45, 'oko')

test.get()
test.set('ooo')

s: str = '3'

print(s)