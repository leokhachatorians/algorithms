import sys

class UF():
    def __init__(self):
        self.id = []

    def UF(self, n):
        self.count = n
        for i in range(n):
            self.id.append(i)

    def connected(self, p, q):
        return self.id[p] == self.id[q]

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
        print(u.id)
        i = i.split()
        p = int(i[0])
        q = int(i[1])

        u.union(p, q)
        #print("{} {}".format(p, q))

    print(u.count, "components")
