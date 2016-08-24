import sys

class UF():
    def __init__(self):
        self.id = []

    def UF(self, n):
        self.count = n
        for i in range(n):
            self.id.append(i)

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def find(self, p):
        return self.id[p]

    def union(self, p, q):
        if self.connected(p, q):
            return
        pid = self.id[p]
        for i in range(len(self.id)):
            if self.id[i] == pid:
                self.id[i] = self.id[q]
        self.count -= 1

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as l:
        lines = l.readlines()
    u = UF()
    u.UF(int(lines[0]))

    for i in lines[1:]:
        i = i.split()
        p = int(i[0])
        q = int(i[1])

        if u.connected(p, q):
            continue
        u.union(p, q)
        print("{} {}".format(p, q))

    print(u.count, "components")
