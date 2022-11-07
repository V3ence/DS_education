import numpy as np


def mid_predict(number):
    """Угадываем число по алгоритму "среднего"

    Args:
        number (int, optional): Загаданное целое число. 

    Returns:
        int: Число попыток.
    """

    count = 0
    
    # определяем границы интервала угадывания
    min_number = 0
    max_number = 100

    while True:
        count += 1
        predict_number = round((min_number + max_number)/2) # вычисляем загаданное число методом "среднего"
        if number == predict_number:
            break # выход из цикла, если угадали
        elif number > predict_number:
            min_number = predict_number # уменьшаем интервал угадывания
        else:
            max_number = predict_number # уменьшаем интервал угадывания 
    return(count)


def score_game(mid_predict):
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        mid_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(mid_predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

# RUN
if __name__ == '__main__':
    score_game(mid_predict)