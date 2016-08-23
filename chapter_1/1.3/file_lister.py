import os
import sys


class Checker():
    """
    Exercise 1.3.43

    - Didn't feel like dealing with having user input
      specific folder to search. Just does it in the
      calling directory.
    """
    def __init__(self):
        self.folders = []

    def start(self):
        for f in os.listdir('.'):
            self.check(f)
        if self.folders:
            for folder in self.folders:
                print(folder)
                for f in os.listdir(folder):
                    self.check(f)

    def check(self, f):
        if os.path.isdir(f):
            self.folders.append(f)
        else:
            print("\t{}".format(f))

if __name__ == '__main__':
    c = Checker()
    c.start()
