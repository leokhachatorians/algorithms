import sys
import time

class UF():
    def __init__(self):
        self.id = []
        self.components = []

    def set_up(self, n):
        self.count = n
        for i in range(n):
            self.id.append(i)
            self.components.append(1)

    def find(self, p):
        while p != self.id[p]:
            p = self.id[p]
        return p

    def root(self, p):
        while p != self.id[p]:
            self.id[p] = self.id[self.id[p]]
            p = self.id[p]
        return p

    def union(self, p, q):
        i = self.root(p)
        j = self.root(q)

        if i == j:
            return

        if self.components[i] < self.components[j]:
            self.id[i] = j
            self.components[j] += self.components[i]
        else:
            self.id[j] = i
            self.components[i] += self.components[i]

        self.count -= 1

if __name__ == '__main__':
    start_time = time.time()
    with open(sys.argv[1], 'r') as l:
        lines = l.readlines()

    u = UF()
    u.set_up(int(lines[0]))

    for i in lines[1:]:
        i = i.split()
        p = int(i[0])
        q = int(i[1])

        u.union(p, q)
        #print("{} {}".format(p, q))

    print(u.count, "components")

    print(time.time() - start_time)
