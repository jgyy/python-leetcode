"""
UnionFind class
"""
from time import time


class UnionFind:
    """
    UnionFind class
    """

    def __init__(self, size):
        self.root = list(range(size))

    def find(self, xint):
        """
        find method
        """
        if xint == self.root[xint]:
            return xint
        self.root[xint] = self.find(self.root[xint])
        return self.root[xint]

    def union(self, xint, yint):
        """
        union method
        """
        rootx = self.find(xint)
        rooty = self.find(yint)
        if rootx != rooty:
            self.root[rooty] = rootx

    def connected(self, xint, yint):
        """
        connected method
        """
        return self.find(xint) == self.find(yint)


if __name__ == "__main__":
    a = time()
    # Test Case
    uf = UnionFind(10)
    # 1-2-5-6-7 3-8-9 4
    uf.union(1, 2)
    uf.union(2, 5)
    uf.union(5, 6)
    uf.union(6, 7)
    uf.union(3, 8)
    uf.union(8, 9)
    print(uf.connected(1, 5))  # true
    print(uf.connected(5, 7))  # true
    print(uf.connected(4, 9))  # false
    # 1-2-5-6-7 3-8-9-4
    uf.union(9, 4)
    print(uf.connected(4, 9))  # true
    print(time() - a)
