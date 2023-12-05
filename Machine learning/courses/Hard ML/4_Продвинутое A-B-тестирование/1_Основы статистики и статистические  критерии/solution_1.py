import numpy as np
import pandas as pd
from scipy.stats import ttest_ind


def estimate_first_type_error(df_pilot_group, df_control_group, metric_name, alpha=0.05, n_iter=10000, seed=None):
    """Оцениваем ошибку первого рода.

    Бутстрепим выборки из пилотной и контрольной групп тех же размеров, считаем долю случаев с значимыми отличиями.
    
    df_pilot_group - pd.DataFrame, датафрейм с данными пилотной группы
    df_control_group - pd.DataFrame, датафрейм с данными контрольной группы
    metric_name - str, названия столбца с метрикой
    alpha - float, уровень значимости для статтеста
    n_iter - int, кол-во итераций бутстрапа
    seed - int or None, состояние генератора случайных чисел.

    return - float, ошибка первого рода
    """
    p_vals = []
    for _ in range(n_iter):
        a = df_control_group[metric_name].sample(frac=1, replace=True, random_state=seed)
        b = df_pilot_group[metric_name].sample(frac=1, replace=True, random_state=seed)
        _, p_val = ttest_ind(a, b)
        p_vals.append(p_val)
        
    res = sum([1 if p_val < alpha else 0 for p_val in p_vals]) / n_iter
    return res      
