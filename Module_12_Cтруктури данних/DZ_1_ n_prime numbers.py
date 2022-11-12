class Prime_numbers:
    def __init__(self, max):
        self.max = max

    def __iter__(self):
        self.count = 0
        self.last_number = 1
        return self

    def __next__(self):
        self.count += 1
        for i in range(self.last_number + 1, self.max * self.max):
            delitel = 0
            for j in range(1, i + 1):
                if i % j == 0:
                     delitel += 1
            if delitel == 2:
                self.last_number = i
                break

        if self.count > self.max:
            raise StopIteration
        return self.last_number

a = Prime_numbers(5)

for number in a:
    print(number)