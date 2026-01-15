class MyHashSet:

    def __init__(self):
        self.mod_div = 10000
        size=10000
        self.arr = [False] * size

    def add(self, key: int) -> None:
        i = key % self.mod_div
        self.arr[i] = True

    def remove(self, key: int) -> None:
        i = key % self.mod_div
        self.arr[i] = False

    def contains(self, key: int) -> bool:
        i = key % self.mod_div
        return self.arr[i]


# Your MyHashSet object will be instantiated and called as such:
obj = MyHashSet()
obj.add(1)
print(obj.arr)
obj.add(2)
print(obj.arr)
obj.add(1)
print(obj.arr)
obj.add(3)
print(obj.arr)
obj.remove(3)
print(obj.arr)
param_3 = obj.contains(2)
print(param_3)
param_3 = obj.contains(3)
print(param_3)
