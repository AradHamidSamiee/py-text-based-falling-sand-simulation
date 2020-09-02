import os
import time

delay_time = 0.4

# world creation
# def create_world():
world_matrix_size = 10
world_matrix = [[0 for x in range(world_matrix_size)] for y in range(world_matrix_size)]
for i in range(world_matrix_size):
    for j in range(world_matrix_size):
        world_matrix[i].append(0)

def init_active_cell(i,j):
    x = int(i)
    y = int(j)
    try:
        world_matrix[x][y] = 1
    except:
        print('out of bounds - be reasonable')

def matrix_data_draw():
    for i in range(world_matrix_size):
        for j in range(world_matrix_size):
            if world_matrix[i][j] == 0:
                # print(' |', world_matrix[i][j], end=' |')
                print(chr(32), end='')
            elif world_matrix[i][j] == 1:
                # print(' |', world_matrix[i][j], end=' |')
                print(chr(35), end='')
        print('\n',end='')
    print('\n',end='')

def matrix_data_index():
    filled_cells_indexes = list()
    for i in range(world_matrix_size):
        for j in range(world_matrix_size):
            if world_matrix[i][j] == 1:
                filled_cells_indexes.append((i,j))
    return filled_cells_indexes

def gravity_mark1():
    for tuple in matrix_data_index():
        if tuple <= (world_matrix_size-2,world_matrix_size-2) and world_matrix[tuple[0]+1][tuple[1]] != 1:
            print(tuple, world_matrix_size-2)
            world_matrix[tuple[0]][tuple[1]] = 0
            world_matrix[tuple[0]+1][tuple[1]] = 1

def delay():
    time.sleep(delay_time)

def clear_Screen():
    os.system('cls')

def task_list():
    clear_Screen()
    matrix_data_draw()
    try:
        gravity_mark1()
    except:
        pass
    delay()

# main
while True:
    command = input('> ')
    if command == 'end' or command == 'exit' or command == 'quit':
        quit()
    elif command == 'next':
        task_list()
    elif command == 'init cell':
        i = input('> i: ')
        j = input('> j: ')
        init_active_cell(i,j)
        print('> cell['+i+']['+j+'] is active now')
    # else:
    #     print('> command not eligible')
