import random

class Grid():
    def __init__(self, amount):
        self.grid = []
        self.amount = amount
        self._generate_connections()

    def _generate_connections(self):
        for i in range(self.amount ** 2):
            p = random.randint(0, self.amount ** 2)
            q = random.randint(0, self.amount ** 2)
            while q == p:
                q = random.randint(0, self.amount ** 2)
            self.grid.append(
                Connection(p=p, q=q)
            )

    def _output_randomly(self):
        i = self.amount ** 2
        print(i)
        while i != 0:
            r = random.randint(0, i - 1)
            print(self.grid[r].p, self.grid[r].q)
            del self.grid[r]
            i -= 1

class Connection():
    def __init__(self, p, q):
        self.p = p
        self.q = q


if __name__ == '__main__':
    amount = int(input('Enter a number: '))
    g = Grid(amount=amount)
    g._output_randomly()




