import numpy as np
import time


class Sudoku:
    grid = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0]
                     ])
    solution = grid.copy()

    def setvalues(self, newgrid):
        self.grid = newgrid

    def printsudoku(self, g):
        res = ""
        for i in range(9):
            for j in range(9):
                if (j == 2) or (j == 5):
                    res = res + str(g[i, j]) + " | "
                elif (j == 8) & ((i == 2) or (i == 5)):
                    res = res + str(g[i, j]) + "\n---------------------\n"
                elif j == 8:
                    res = res + str(g[i, j]) + "\n"
                else:
                    res = res + str(g[i, j]) + " "
        print(res)

    def __checkifpossible(self, g, i, j, x):
        for k in range(9):
            if g[i, k] == x:
                return False
        for k in range(9):
            if g[k, j] == x:
                return False
        if i < 3:
            imin = 0
            imax = 2
        elif i < 6:
            imin = 3
            imax = 5
        else:
            imin = 6
            imax = 8
        if j < 3:
            jmin = 0
            jmax = 2
        elif j < 6:
            jmin = 3
            jmax = 5
        else:
            jmin = 6
            jmax = 8
        for k in range(imin, imax+1):
            for l in range(jmin, jmax+1):
                if g[k, l] == x:
                    return False
        return True

    def __solveefficient(self, g):
        run = True
        while run:
            run = False
            for i in range(9):
                for j in range(9):
                    if g[i, j] == 0:
                        poslist = []
                        for x in range(1, 10):
                            if self.__checkifpossible(g, i, j, x):
                                poslist.append(x)
                        if len(poslist) == 1:
                            g[i, j] = poslist[0]
                            run = True
        zeroleft = False
        for i in range(9):
            for j in range(9):
                if g[i, j] == 0:
                    zeroleft = True
        if zeroleft:
            self.__solvebacktracking(g.copy())
        else:
            self.solution = g.copy()

    def __solvebacktracking(self, g):
        for i in range(9):
            for j in range(9):
                if g[i, j] == 0:
                    for x in range(1, 10):
                        if self.__checkifpossible(g, i, j, x):
                            g[i, j] = x
                            if (i == 8) & (j == 8):
                                # self.printsudoku(g)
                                self.solution = g.copy()
                                # input("Enter für nächste Lösung")
                            else:
                                self.__solvebacktracking(g.copy())
                    return

    def solvesudoku(self):
        tic_normal = time.perf_counter()
        self.__solvebacktracking(self.grid.copy())
        toc_normal = time.perf_counter()
        print("Time taken by backtracking approach: " + str(toc_normal-tic_normal))

        tic_efficient = time.perf_counter()
        self.__solveefficient(self.grid.copy())
        toc_efficient = time.perf_counter()
        print("Time taken by efficient approach: " + str(toc_efficient-tic_efficient))

        self.printsolution()

    def printbase(self):
        self.printsudoku(self.grid)

    def printsolution(self):
        self.printsudoku(self.solution)


def main():
    test = np.array([[0, 0, 0, 0, 0, 0, 4, 0, 0],
                     [7, 0, 0, 2, 0, 3, 0, 0, 0],
                     [0, 0, 0, 0, 9, 1, 6, 0, 0],
                     [0, 0, 0, 0, 0, 0, 7, 0, 0],
                     [0, 1, 6, 4, 3, 0, 0, 0, 0],
                     [9, 0, 0, 5, 0, 0, 0, 0, 2],
                     [5, 0, 0, 0, 0, 0, 0, 0, 1],
                     [0, 7, 0, 0, 5, 0, 3, 0, 9],
                     [0, 0, 9, 0, 7, 0, 0, 0, 0]
                     ])

    sdk = Sudoku()
    sdk.setvalues(test)
    sdk.printbase()
    sdk.solvesudoku()


if __name__ == "__main__":
    main()

