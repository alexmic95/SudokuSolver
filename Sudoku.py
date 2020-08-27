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

    def setvalues(self, newgrid):
        self.grid = newgrid

    def printsudoku(self):
        res = ""
        for i in range(9):
            for j in range(9):
                if (j == 2) or (j == 5):
                    res = res + str(self.grid[i, j]) + " | "
                elif (j == 8) & ((i == 2) or (i == 5)):
                    res = res + str(self.grid[i, j]) + "\n---------------------\n"
                elif j == 8:
                    res = res + str(self.grid[i, j]) + "\n"
                else:
                    res = res + str(self.grid[i, j]) + " "
        print(res)




def main():
    sdk = Sudoku()
    sdk.printsudoku()


if __name__ == "__main__":
    main()

