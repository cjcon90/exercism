from typing import List

class Matrix:
    def __init__(self, matrix_string: str) -> None:
        self.grid = [
            tuple([int(col) for col in row.split()])
            for row in matrix_string.splitlines()
        ]

    def row(self, index: int) -> List[int]:
        for row in self.grid:
            print(row)
        return list(self.grid[index - 1])

    def column(self, index: int) -> List[int]:
        return [row[index - 1] for row in self.grid]



matrix = Matrix(
    """\
    1 2 3
    4 5 6
    7 8 9
    """
)

print(matrix.row(2))

second_row = matrix.row(2)
second_row[2] = 99
print(matrix.row(2))
