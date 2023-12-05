import numpy as np
import pandas as pd
from scipy.stats import ttest_ind


def estimate_second_type_error(df_pilot_group, df_control_group, metric_name, effects, alpha=0.05, n_iter=10000, seed=None):
    """Оцениваем ошибки второго рода.

    Бутстрепим выборки из пилотной и контрольной групп тех же размеров, добавляем эффект к пилотной группе,
    считаем долю случаев без значимых отличий.
    
    df_pilot_group - pd.DataFrame, датафрейм с данными пилотной группы
    df_control_group - pd.DataFrame, датафрейм с данными контрольной группы
    metric_name - str, названия столбца с метрикой
    effects - List[float], список размеров эффектов ([1.03] - увеличение на 3%).
    alpha - float, уровень значимости для статтеста
    n_iter - int, кол-во итераций бутстрапа
    seed - int or None, состояние генератора случайных чисел

    return - dict, {размер_эффекта: ошибка_второго_рода}
    """
    dict_res = dict()
    for effect in effects:
        p_vals = []
        for _ in range(n_iter):
            a = df_control_group[metric_name].sample(frac=1, replace=True, random_state=seed)
            b = df_pilot_group[metric_name].sample(frac=1, replace=True, random_state=seed)
            b *= effect
            _, p_val = ttest_ind(a, b)
            p_vals.append(p_val)

        res = sum([1 if p_val >= alpha else 0 for p_val in p_vals]) / n_iter
        dict_res[effect] = res
        
    return dict_res  
