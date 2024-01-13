from dataclasses import dataclass, field
from typing import Dict, List
from collections import namedtuple

row_col = namedtuple("row_col", ["row", "col"])


@dataclass
class Cell:
    val: int = 0


@dataclass
class Row:
    row: List[Cell] = field(default_factory=list)


@dataclass
class SudokoTable:
    rows: List[Row] = field(default_factory=list)


class Sudoko:
    def __init__(self):
        self.__n_size: int = 9
        self.__grid_size: int = 3
        self.__table: SudokoTable = SudokoTable()
        self._initialize_table()

    @property
    def get_n(self) -> int:
        return self.__n_size

    def _get_new_row(self):
        rw = Row()
        for _ in range(self.__n_size):
            rw.row.append(Cell())
        return rw

    def _initialize_table(self):
        for _ in range(self.__n_size):
            self.__table.rows.append(self._get_new_row())

    def _is_number_exist_in_row(self, number: int, row: int) -> bool:
        for cell in self.__table.rows[row].row:
            if number == cell.val:
                return True
        return False

    def _is_number_exist_in_col(self, number: int, col: int) -> bool:
        for i in range(self.__n_size):
            if number == self.__table.rows[i].row[col].val:
                return True
        return False

    def add_number_to_cell(self, number: int, row: int, col: int) -> None:
        cell = self.__table.rows[row].row[col]
        cell.val = number

    def get_value_of_cell(self, row: int, col: int) -> int:
        return self.__table.rows[row].row[col].val

    def reset_cell(self, row: int, col: int) -> None:
        sqr = self.__table.rows[row].row[col]
        sqr.val = 0

    def _is_number_present_in_grid(self, row: int, col: int, number: int) -> bool:
        startRow = row - row % self.__grid_size
        startCol = col - col % self.__grid_size
        for i in range(self.__grid_size):
            for j in range(self.__grid_size):
                if self.__table.rows[i + startRow].row[j + startCol].val == number:
                    return True
        return False

    def is_safe_to_add(self, number: int, row: int, col: int) -> bool:
        if self._is_number_exist_in_row(number, row) or self._is_number_exist_in_col(number, col):
            return False
        if self._is_number_present_in_grid(row, col, number):
            return False
        return True


class SudokoSolver:
    def __init__(self):
        self.sudoko = Sudoko()

    def add_input(self, inputs: List[Dict[row_col, int]]) -> bool:
        for inpt in inputs:
            rw_col = tuple(inpt.keys())[-1]
            number = inpt[rw_col]
            if not self.sudoko.is_safe_to_add(number, rw_col.row - 1, rw_col.col - 1):
                return False
            self.sudoko.add_number_to_cell(number, rw_col.row - 1, rw_col.col - 1)
        return True

    def solve(self, row: int = 0, col: int = 0) -> bool:
        if row == self.sudoko.get_n - 1 and col == self.sudoko.get_n:
            return True
        if col == self.sudoko.get_n:
            row, col = row + 1, 0
        if self.sudoko.get_value_of_cell(row, col) != 0:
            return self.solve(row, col + 1)

        for number in range(1, self.sudoko.get_n + 1):
            if self.sudoko.is_safe_to_add(number, row, col):
                self.sudoko.add_number_to_cell(number, row, col)
                if self.solve(row, col + 1):
                    return True
                self.sudoko.reset_cell(row, col)
        return False

    def print_sudoko(self) -> None:
        for row in range(self.sudoko.get_n):
            for col in range(self.sudoko.get_n):
                print(self.sudoko.get_value_of_cell(row, col), end=" ")
            print("")


solver = SudokoSolver()
lst = [{row_col(row=1, col=4): 8}, {row_col(row=1, col=8): 1}, {row_col(row=8, col=9): 7}]
solver.add_input(lst)
solver.solve()
solver.print_sudoko()
