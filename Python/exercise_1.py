from random import choice


def count_fourth_digits(x, y):
    grid = []

    for y_index in range(y):
        tmp_row = []
        for x_index in range(x):
            tmp_row.append(choice(['0', '1', '0', '1']))

        tmp_row.extend(['', '', '', ''])  
        grid.append(tmp_row)

    grid.append([''] * len(tmp_row))  
    grid.append([''] * len(tmp_row))
    grid.append([''] * len(tmp_row))  
    grid.append([''] * len(tmp_row))
   

    count_digits = 0

    for y_index in range(0, y):
        tmp_grid_ = grid[y_index:y_index + 6]

        for x_index in range(0, x):
            tmp_grid = []
            for row in tmp_grid_:
                tmp_grid.append(row[x_index:x_index + 6])

            # horizontal 1111
            if tmp_grid[0][0] == '1' and tmp_grid[0][1] == '1' and tmp_grid[0][2] == '1'and tmp_grid[0][3] == '1':
                count_digits += 1

            # vertical 1111
            if tmp_grid[0][0] == '1' and tmp_grid[1][0] == '1' and tmp_grid[2][0] == '1'and tmp_grid[3][0] == '1':
                count_digits += 1

            # diagonals 1111
            if tmp_grid[0][0] == '1' and tmp_grid[1][1] == '1' and tmp_grid[2][2] == '1'and tmp_grid[3][3] == '1':
                count_digits += 1
            if tmp_grid[3][0] == '1' and tmp_grid[2][1] == '1' and tmp_grid[1][2] == '1'and tmp_grid[0][3] == '1':
                count_digits += 1

    return count_digits


if __name__ == '__main__':
    x = 10
    y = 10

    num_digits = []
    for _ in range(100):
        num_digits.append(count_fourth_digits(x, y))

print(f'Average number of units: {sum(num_digits) / 100}')
