import sys
import time

class UF():
    def __init__(self):
        self.id = []

    def set_up(self, n):
        self.count = n
        for i in range(n):
            self.id.append(i)

    def connected(self, p, q):
        return self.id[p] == self.id[q]

    def find(self, p):
        while p != self.id[p]:
            p = self.id[p]
        return p

    def union(self, p, q):
        pRoot = self.find(p)
        qRoot = self.find(q)
        if pRoot == qRoot:
            return
        self.id[pRoot] = qRoot
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
