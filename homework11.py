print("Дз 23")
class Counter:

    def __init__(self, min_value, max_value, start_value):
        self.min_value = min_value
        self.max_value = max_value
        self.start_value = start_value

    def min(self, min_value):
        self.min_value = min_value

    def max(self, max_value):
        self.max_value = max_value

    def start(self, start_value):
        self.start_value = start_value

    def count(self):
        if self.start_value < self.max_value:
            self.start_value += 1
        else:
            return self.max_value

    def pop(self):
        return self.start_value


a = Counter(0, 9999, 5)
a.count()
value = a.pop()
print(value)
