import pandas as pd
import numpy as np

def calculate_linearized_metric(
    df, value_name, user_id_name, list_user_id, date_name, period, metric_name, kappa=None
):
    """Вычисляет значение линеаризованной метрики для списка пользователей в определённый период.
    
    df - pd.DataFrame, датафрейм с данными
    value_name - str, название столбца со значениями для вычисления целевой метрики
    user_id_name - str, название столбца с идентификаторами пользователей
    list_user_id - List[int], список идентификаторов пользователей, для которых нужно посчитать метрики
    date_name - str, название столбца с датами
    period - dict, словарь с датами начала и конца периода, за который нужно посчитать метрики.
        Пример, {'begin': '2020-01-01', 'end': '2020-01-08'}. Дата начала периода входит в
        полуинтервал, а дата окончания нет, то есть '2020-01-01' <= date < '2020-01-08'.
    metric_name - str, название полученной метрики
    kappa - float, коэффициент в функции линеаризации.
        Если None, то посчитать как ratio метрику по имеющимся данным.

    return - pd.DataFrame, со столбцами [user_id_name, metric_name], кол-во строк должно быть равно
        кол-ву элементов в списке list_user_id.
    """
    # YOUR_CODE_HERE
    
    # Фильтрация пользователей
    df_filtered = df[df[user_id_name].isin(list_user_id)]
    # Фильтрация дат
    df_filtered = df_filtered[(df_filtered[date_name] >= period['begin']) & \
                             (df_filtered[date_name] < period['end'])]
    
    # Расчет числителя и знаменателя
    df_g = df_filtered.groupby(user_id_name).agg(**{
        'x': (value_name, 'sum'),
        'y': (value_name, 'count'),
    }).reset_index()
    
    # Коэффициент линеаризации
    if not kappa:
        kappa = df_g['x'].sum() / df_g['y'].sum()
        
    # Расчет линеаризованной метрики
    df_g[metric_name] = df_g['x'] - kappa * df_g['y']

    # Приводим к нужному числу строк
    df_res = pd.DataFrame({user_id_name: list_user_id}) \
        .merge(df_g[[user_id_name, metric_name]], how='left', on=user_id_name) \
        .fillna(0)
    
    return df_res
    
