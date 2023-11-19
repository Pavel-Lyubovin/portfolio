import numpy as np


def get_bernoulli_confidence_interval(values: np.array):
    """Вычисляет доверительный интервал для параметра распределения Бернулли.

    :param values: массив элементов из нулей и единиц.
    :return (left_bound, right_bound): границы доверительного интервала.
    """
    # Кол-во наблюдений
    n =  values.shape[0]
    # Оценка параметра p распределения Бернулли
    p_hat = values.sum() / n
    # Оценка математического ожидания распределения Бернулли
    mu_hat = p_hat
    # Оценка дисперсии распределения Бернулли
    d_hat = p_hat * (1 - p_hat)
    # Стандартная ошибка
    se = (d_hat / n) ** 0.5
    # Z-коэффициент для альфа/2, если альфа = 0.05
    Z_ALPHA_HALF = 1.96
    
    # Зная мат. ожидание, дисперсию и z, рассчитываем доверительный интервал по центральной предельной теореме
    left_bound = mu_hat - Z_ALPHA_HALF * se
    right_bound = mu_hat + Z_ALPHA_HALF * se
    
    # Т.к. у нас распределение Бернулли, то оно по определению ограничено 0 и 1
    # расчетный доверительный интервал  нужно тоже ограничить
    left_bound = max(0, left_bound)
    right_bound = min(1, right_bound)
    
    return left_bound, right_bound
