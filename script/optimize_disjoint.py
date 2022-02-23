"""
UnionFind class
"""
from time import time


class UnionFind:
    """
    UnionFind class
    """

    def __init__(self, size):
        """
        Use a rank array to record the height of each vertex, i.e., the "rank" of each vertex.
        The initial "rank" of each vertex is 1, because each of them is
        a standalone vertex with no connection to other vertices.
        """
        self.root = list(range(size))
        self.rank = [1] * size

    def find(self, xint):
        """
        The find function here is the same as that in the disjoint set with path compression.
        """
        if xint == self.root[xint]:
            return xint
        self.root[xint] = self.find(self.root[xint])
        return self.root[xint]

    def union(self, xint, yint):
        """
        The union function with union by rank
        """
        rootx = self.find(xint)
        rooty = self.find(yint)
        if rootx != rooty:
            if self.rank[rootx] > self.rank[rooty]:
                self.root[rooty] = rootx
            elif self.rank[rootx] < self.rank[rooty]:
                self.root[rootx] = rooty
            else:
                self.root[rooty] = rootx
                self.rank[rootx] += 1

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
