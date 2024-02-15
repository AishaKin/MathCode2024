import pathlib
import random
import time
import typing as tp
import multiprocessing
import test_sudoku
T = tp.TypeVar("T")


def read_sudoku(path: tp.Union[str, pathlib.Path]) -> tp.List[tp.List[str]]:
    """ Прочитать Судоку из указанного файла """
    path = pathlib.Path(path)
    with path.open() as f:
        puzzle = f.read()
    return create_grid(puzzle)


def create_grid(puzzle: str) -> tp.List[tp.List[str]]:
    digits = [c for c in puzzle if c in "123456789."]
    grid = group(digits, 9)
    return grid


def group(values: tp.List[T], n: int) -> tp.List[tp.List[T]]:
    L = [values[n * i: n * (i + 1)] for i in range(n)]
    return L


def display(grid: tp.List[tp.List[str]]) -> None:
    """Вывод Судоку """
    width = 2
    line = "+".join(["-" * (width * 3)] * 3)
    for row in range(9):
        print(
            "".join(
                grid[row][col].center(width) + ("|" if str(col) in "25" else "") for col in range(9)
            )
        )
        if str(row) in "25":
            print(line)
    print()


def get_row(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    pos_row = (pos[0])
    row = grid[pos_row]
    return row


def get_col(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    pos_col = (pos[1])
    n = len(grid)
    col = []
    for i in range(n):
        row = grid[i]
        for col_el in row:
            col_el = row[pos_col]
        col.append(col_el)
    return col


def get_block(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    pos_row = (pos[0])
    pos_col = (pos[1])
    block = []
    el_all = []
    if 0 <= pos_row <= 2:
        grid_1 = []
        grid_1.append(grid[0])
        grid_1.append(grid[1])
        grid_1.append(grid[2])
        for i in range(len(grid_1)):
            if 0 <= pos_col <= 2:
                for j in range(0, 3):
                    el = grid_1[i][j]
                    el_all.append(el)
            if 3 <= pos_col <= 5:
                for j in range(3, 6):
                    el = grid_1[i][j]
                    el_all.append(el)
            if 6 <= pos_col <= 8:
                for j in range(6, 9):
                    el = grid_1[i][j]
                    el_all.append(el)
        block.append(el_all)
        block = sum(block, [])

    if 3 <= pos_row <= 5:
        grid_2 = []
        grid_2.append(grid[3])
        grid_2.append(grid[4])
        grid_2.append(grid[5])
        for i in range(len(grid_2)):
            if 0 <= pos_col <= 2:
                for j in range(0, 3):
                    el = grid_2[i][j]
                    el_all.append(el)
            if 3 <= pos_col <= 5:
                for j in range(3, 6):
                    el = grid_2[i][j]
                    el_all.append(el)
            if 6 <= pos_col <= 8:
                for j in range(6, 9):
                    el = grid_2[i][j]
                    el_all.append(el)
        block.append(el_all)
        block = sum(block, [])

    if 6 <= pos_row <= 8:
        grid_3 = []
        grid_3.append(grid[6])
        grid_3.append(grid[7])
        grid_3.append(grid[8])
        for i in range(len(grid_3)):
            if 0 <= pos_col <= 2:
                for j in range(0, 3):
                    el = grid_3[i][j]
                    el_all.append(el)
            if 3 <= pos_col <= 5:
                for j in range(3, 6):
                    el = grid_3[i][j]
                    el_all.append(el)
            if 6 <= pos_col <= 8:
                for j in range(6, 9):
                    el = grid_3[i][j]
                    el_all.append(el)
        block.append(el_all)
        block = sum(block, [])

    return block


def find_empty_positions(grid: tp.List[tp.List[str]]) -> tp.Optional[tp.Tuple[int, int]]:
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == ".":
                return (i, j)


def find_possible_values(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.Set[str]:
    values, values1, values2 = [], [], []
    row1 = get_row(grid, pos)
    col1 = get_col(grid, pos)
    block = get_block(grid, pos)

    for i in range(1, 10):
        flag = 0
        for j in range(len(row1)):
            if row1[j] == str(i):
                flag = 1
                break
        if flag == 0:
            if len(values) == 0:
                values.append(str(i))
            else:
                for key in range(len(values)):
                    if str(i) != values[key]:
                        values.append(str(i))

    for i in range(1, 10):
        flag = 0
        for j in range(len(col1)):
            if col1[j] == str(i):
                flag = 1
                break
        if flag == 0:
            if len(values1) == 0:
                values1.append(str(i))
            else:
                for key in range(len(values1)):
                    if str(i) != values1[key]:
                        values1.append(str(i))

    for i in range(1, 10):
        flag = 0
        for j in range(len(block)):
            if block[j] == str(i):
                flag = 1
                break
        if flag == 0:
            if len(values2) == 0:
                values2.append(str(i))
            else:
                for key in range(len(values2)):
                    if str(i) != values2[key]:
                        values2.append(str(i))

    result = list(set(values1).intersection(values2))
    result = list(set(result).intersection(values))

    return set(result)

def solve(grid: tp.List[tp.List[str]]) -> tp.Optional[tp.List[tp.List[str]]]:
    empty_position = find_empty_positions(grid)

    if not empty_position:
        # Если нет пустых позиций, значит, Судоку уже решено
        return grid

    row, col = empty_position

    possible_values = find_possible_values(grid, (row, col))

    for value in possible_values:
        # Пробуем установить возможное значение на пустую позицию
        grid[row][col] = value

        # Рекурсивно вызываем solve() для следующей пустой позиции
        result = solve(grid)

        if result:
            # Если решение найдено, возвращаем его
            return result

        # Если решение не найдено, откатываем установку значения
        grid[row][col] = '.'

    # Если не удалось найти решение для текущей ситуации
    return None

    """ Решение пазла, заданного в grid """
    """ Как решать Судоку?
        1. Найти свободную позицию
        2. Найти все возможные значения, которые могут находиться на этой позиции
        3. Для каждого возможного значения:
            3.1. Поместить это значение на эту позицию
            3.2. Продолжить решать оставшуюся часть пазла

    >>> grid = read_sudoku('puzzle1.txt')
    >>> solve(grid)
    [['5', '3', '4', '6', '7', '8', '9', '1', '2'],
     ['6', '7', '2', '1', '9', '5', '3', '4', '8'],
     ['1', '9', '8', '3', '4', '2', '5', '6', '7'],
     ['8', '5', '9', '7', '6', '1', '4', '2', '3'],
     ['4', '2', '6', '8', '5', '3', '7', '9', '1'],
     ['7', '1', '3', '9', '2', '4', '8', '5', '6'],
     ['9', '6', '1', '5', '3', '7', '2', '8', '4'],
     ['2', '8', '7', '4', '1', '9', '6', '3', '5'], 
     ['3', '4', '5', '2', '8', '6', '1', '7', '9']]
    """
    # pass



def check_solution(solution: tp.List[tp.List[str]]) -> bool:
    flag = 0

    for i in range(len(solution)):
        for j in range(len(solution[i])):
            if solution[i][j] != '.':
                row = get_row(solution, (i, j))
                col = get_col(solution, (i, j))
                block = get_block(solution, (i, j))

                if sorted(row) == sorted(list(set(row))) and sorted(col) == sorted(list(set(col))) and sorted(block) == sorted(list(set(block))):
                    flag = 1
                else:
                    return False
            else:
                return False
    if flag == 1:
        return True

    return None


def generate_sudoku(N: int) -> tp.List[tp.List[str]]:
    if N > 81:
        N = 81

    # Генерируем решенный пазл
    solved_puzzle = solve(read_sudoku('puzzle1.txt'))

    # Создаем копию решенного пазла
    puzzle = [row.copy() for row in solved_puzzle]

    # Определение количества чисел, которые нужно удалить
    cells_to_remove = 81 - N

    # Удаление случайных чисел
    positions = [(row, col) for row in range(9) for col in range(9)]
    random.shuffle(positions)

    for row, col in positions[:cells_to_remove]:
        puzzle[row][col] = '.'

    return puzzle


if __name__ == "__main__":
    for fname in ["puzzle1.txt", "puzzle2.txt", "puzzle3.txt"]:
        grid = read_sudoku(fname)
        display(grid)
        solution = solve(grid)
        if not check_solution(solution):
            print(f"Puzzle {fname} can't be solved")
        else:
            display(solution)