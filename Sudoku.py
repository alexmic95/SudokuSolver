import numpy as np


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

    def __solveg(self, g):
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
                                self.__solveg(g.copy())
                    return

    def solvesudoku(self):
        self.__solveg(self.grid)
        self.printsudoku(self.solution)

    def printbase(self):
        self.printsudoku(self.grid)

    def printsolution(self):
        self.printsudoku(self.solution)


def main():
    test = np.array([[1, 0, 0, 0, 0, 3, 0, 0, 2],
                     [0, 3, 0, 8, 0, 0, 6, 0, 0],
                     [4, 9, 0, 0, 6, 0, 0, 3, 1],
                     [0, 2, 0, 0, 0, 6, 4, 0, 0],
                     [0, 8, 3, 5, 0, 7, 0, 0, 0],
                     [6, 5, 0, 0, 0, 0, 8, 0, 3],
                     [0, 0, 0, 1, 2, 0, 5, 0, 0],
                     [0, 7, 0, 0, 0, 0, 0, 1, 0],
                     [8, 0, 2, 7, 5, 9, 0, 0, 0]
                     ])
    sdk = Sudoku()
    sdk.setvalues(test)
    sdk.printsudoku(sdk.grid)
    sdk.solvesudoku()


if __name__ == "__main__":
    main()

