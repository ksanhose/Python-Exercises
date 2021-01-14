from random import choice


def count_sos_triplets(x, y):
    grid = []

    for y_index in range(y):
        tmp_row = []
        for x_index in range(x):
            tmp_row.append(choice(['S', 'O']))

        tmp_row.extend(['', ''])  # pad 2 columns for easier matching
        grid.append(tmp_row)

    grid.append([''] * len(tmp_row))  # pad 2 rows for easier matching
    grid.append([''] * len(tmp_row))

    count_sos = 0

    for y_index in range(0, y):
        tmp_grid_ = grid[y_index:y_index + 3]

        for x_index in range(0, x):
            tmp_grid = []
            for row in tmp_grid_:
                tmp_grid.append(row[x_index:x_index + 3])

            # horizontal SOS
            if tmp_grid[0][0] == 'S' and tmp_grid[0][1] == 'O' and tmp_grid[0][2] == 'S':
                count_sos += 1

            # vertical SOS
            if tmp_grid[0][0] == 'S' and tmp_grid[1][0] == 'O' and tmp_grid[2][0] == 'S':
                count_sos += 1

            # diagonals SOS
            if tmp_grid[0][0] == 'S' and tmp_grid[1][1] == 'O' and tmp_grid[2][2] == 'S':
                count_sos += 1
            if tmp_grid[2][0] == 'S' and tmp_grid[1][1] == 'O' and tmp_grid[0][2] == 'S':
                count_sos += 1

    return count_sos


if __name__ == '__main__':
    x = 15
    y = 10

    num_triples = []
    for _ in range(100):
        num_triples.append(count_sos_triplets(x, y))

print(f'Average number of SOS triples: {sum(num_triples) / 100}')
