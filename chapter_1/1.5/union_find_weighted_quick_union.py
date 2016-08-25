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

        for i in range(n):
            self.components.append(1)

    def connected(self, p, q):
        return self.id[p] == self.id[q]

    def find(self, p):
        while p != self.id[p]:
            p = self.id[p]
        return p

    def union(self, p, q):
        i = self.find(p)
        j = self.find(q)

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
