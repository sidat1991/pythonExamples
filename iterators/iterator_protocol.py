class MyRange:
    def __init__(self, start, end, step=1):
        self.start = start
        self.end = end
        self.step = step
        self.is_valid_range = self.validate_range()

    def validate_range(self):
        if self.step >= 1 and self.start <= self.end:
            return True
        if self.start >= self.end and self.step < 0:
            return True
        return False

    def __iter__(self):
        return self

    def __next__(self):
        if not self.is_valid_range or self.step == 0:
            raise StopIteration()
        if (self.start >= self.end and self.step >= 1) or \
                (self.start <= self.end and self.step < 0):
            raise StopIteration()
        temp = self.start
        self.start += self.step
        return temp


print("Test1")
for num in MyRange(0, 9, 1):
    print(num)

print("Test2")
for num in MyRange(0, 9, -2):
    print(num)

print("Test3")
for num in MyRange(9, 0, -2):
    print(num)

print("Test4")
for num in MyRange(-9, 0):
    print(num)

print("Test5")
for num in MyRange(0, -9, -1):
    print(num)


