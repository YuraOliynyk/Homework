print("Дз 25")


class Buffer:
    def __init__(self):
        self.list_of_numbers = []

    def add(self, *a):
        self.list_of_numbers.extend(a)
        while len(self.list_of_numbers) < 5:
            return None
        else:
            print(sum(self.list_of_numbers[:5]))
            self.list_of_numbers = self.list_of_numbers[5:]

    def get_current_part(self):
        return sum(self.list_of_numbers)


if __name__ == "__main__":
    buf = Buffer()
    buf.add(5, 5, 6)
    buf.get_current_part()
    buf.add(1, 11, 5, 8, 6, 4)
    buf.get_current_part()
    buf.add(1, 2)
    buf.get_current_part()
    buf.add(1, 2, 3, 4)
    buf.get_current_part()
    buf.add(15, 24, 45, 89)
    buf.get_current_part()
