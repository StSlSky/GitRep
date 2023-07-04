'Game_Finally'

import numpy as np


def game_finally(number) -> int:
    # number = np.random.randint(1, 101) - компьютер загадывает число
    # print("num:", number)
    predict_min = 1
    predict_max = 101
    # количество попыток
    count = 1
    predict_number = np.random.randint(1, 101)  # компьюьер предсеазывает число

    while number != predict_number:
       
        if (predict_max - predict_min) < 2:
            break 
        count += 1
       

        if predict_number > number:  
            predict_max = predict_number
            predict_number = round((predict_min + predict_max) / 2)
        # если предсказанное число больше загаданного
        else:
            predict_min = predict_number
            predict_number = round((predict_min + predict_max) / 2)
        # если предсказанное число меньше загаданного
   
    return count

def score_game(game_finally) -> int:

    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(10000))  # загадали список чисел
   
    for number in random_array:
        count_ls.append(game_finally(number))
        score = int(np.mean(count_ls))
   
    return score


score_game(game_finally)