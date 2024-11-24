import numpy as np
import random
import matplotlib.pyplot as plt

# Константы
N = 50  # Размерность n x n
BLUE_PERCENTAGE = 0.45
RED_PERCENTAGE = 0.45
EMPTY_PERCENTAGE = 0.10
STEPS = 10000  # Количество шагов в моделировании


# Создание начальной сетки
def initialize_grid(n):
    total_cells = n * n
    num_blue = int(total_cells * BLUE_PERCENTAGE)
    num_red = int(total_cells * RED_PERCENTAGE)
    num_empty = total_cells - num_blue - num_red

    grid = (['B'] * num_blue) + (['R'] * num_red) + (['E'] * num_empty)
    random.shuffle(grid)
    return np.array(grid).reshape(n, n)


# Проверка "счастья" клетки
def is_happy(grid, x, y):
    color = grid[x][y]
    if color == 'E':
        return True  # Пустая клетка всегда "счастлива"

    neighbors = get_neighbors(grid, x, y)

    same_color_count = sum(1 for n in neighbors if grid[n[0]][n[1]] == color)
    return same_color_count >= 2


# Получение соседей клетки
def get_neighbors(grid, x, y):
    neighbors = []
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue  # игнорируем саму клетку
            nx, ny = x + dx, y + dy
            if 0 <= nx < grid.shape[0] and 0 <= ny < grid.shape[1]:
                neighbors.append((nx, ny))
    return neighbors


# Перемещение несчастной клетки
def move_unhappy(grid):
    unhappy_cells = [(i, j) for i in range(grid.shape[0]) for j in range(grid.shape[1]) if not is_happy(grid, i, j)]

    if not unhappy_cells:
        return False  # Все клетки счастливы

    # Выбираем случайную несчастную клетку
    x, y = random.choice(unhappy_cells)

    # Находим случайную пустую клетку
    empty_cells = [(i, j) for i in range(grid.shape[0]) for j in range(grid.shape[1]) if grid[i][j] == 'E']
    new_x, new_y = random.choice(empty_cells)

    # Перемещаем клетку
    grid[new_x][new_y] = grid[x][y]  # Перемещаем цвет (синий или красный)
    grid[x][y] = 'E'  # Делает старую клетку пустой
    return True


# Основная функция моделирования
def run_simulation(n, steps):
    grid = initialize_grid(n)
    for step in range(steps):
        move_unhappy(grid)
        plt.imshow(grid == 'B', cmap='Blues', alpha=0.5)
        plt.imshow(grid == 'R', cmap='Reds', alpha=0.5)
        plt.title(f'Step {step + 1}')
        plt.axis('off')
        plt.pause(0.1)  # Задержка для визуализации
    plt.show()


# Запуск моделирования
if __name__ == "__main__":
    run_simulation(N, STEPS)
