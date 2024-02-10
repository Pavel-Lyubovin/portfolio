import numpy as np
import pandas as pd


def calculate_metric(
    df, value_name, user_id_name, list_user_id, date_name, period, metric_name
):
    """Вычисляет значение метрики для списка пользователей в определённый период.
    
    df - pd.DataFrame, датафрейм с данными
    value_name - str, название столбца со значениями для вычисления целевой метрики
    user_id_name - str, название столбца с идентификаторами пользователей
    list_user_id - List[int], список идентификаторов пользователей, для которых нужно посчитать метрики
    date_name - str, название столбца с датами
    period - dict, словарь с датами начала и конца периода, за который нужно посчитать метрики.
        Пример, {'begin': '2020-01-01', 'end': '2020-01-08'}. Дата начала периода входит нужный
        полуинтервал, а дата окончание нет, то есть '2020-01-01' <= date < '2020-01-08'.
    metric_name - str, название полученной метрики

    return - pd.DataFrame, со столбцами [user_id_name, metric_name], кол-во строк должно быть равно
        кол-ву элементов в списке list_user_id.
    """
    # YOUR_CODE_HERE
    
    # Фильтрую пользователей
    df_filtered = df[df[user_id_name].isin(list_user_id)]
    # Фильтрую даты
    df_filtered = df_filtered[(df_filtered[date_name] >= period['begin']) \
                              & (df_filtered[date_name] < period['end'])]
    # Сумма по пользователям
    df_g = df_filtered.groupby(user_id_name).agg(**{
        metric_name: (value_name, 'sum')
    }).reset_index()
    # Результат с кол-вом строк в list_user_id
    df_res = pd.DataFrame({user_id_name: list_user_id})
    df_res = df_res.merge(df_g, how='left', on=user_id_name).fillna(value={metric_name: 0})
    return df_res
    


def calculate_metric_cuped(
    df, value_name, user_id_name, list_user_id, date_name, periods, metric_name
):
    """Вычисляет метрики во время пилота, коварианту и преобразованную метрику cuped.
    
    df - pd.DataFrame, датафрейм с данными
    value_name - str, название столбца со значениями для вычисления целевой метрики
    user_id_name - str, название столбца с идентификаторами пользователей
    list_user_id - List[int], список идентификаторов пользователей, для которых нужно посчитать метрики
    date_name - str, название столбца с датами
    periods - dict, словарь с датами начала и конца периода пилота и препилота.
        Пример, {
            'prepilot': {'begin': '2020-01-01', 'end': '2020-01-08'},
            'pilot': {'begin': '2020-01-08', 'end': '2020-01-15'}
        }.
        Дата начала периода входит в полуинтервал, а дата окончания нет,
        то есть '2020-01-01' <= date < '2020-01-08'.
    metric_name - str, название полученной метрики

    return - pd.DataFrame, со столбцами
        [user_id_name, metric_name, f'{metric_name}_prepilot', f'{metric_name}_cuped'],
        кол-во строк должно быть равно кол-ву элементов в списке list_user_id.
    """
    # YOUR_CODE_HERE
    
    # Данные пилота
    df_pilot = calculate_metric(df,
                                   value_name,
                                   user_id_name,
                                   list_user_id,
                                   date_name,
                                   periods['pilot'],
                                   metric_name)
    # Данные предпилота
    df_prepilot = calculate_metric(df,
                                   value_name,
                                   user_id_name,
                                   list_user_id,
                                   date_name,
                                   periods['prepilot'],
                                   f'{metric_name}_prepilot')

    # Объединяю оба фрейма
    df_res = df_pilot.merge(df_prepilot, how='left', on=user_id_name)
    # cuped
    theta = np.cov(df_pilot[metric_name], df_prepilot[f'{metric_name}_prepilot'])[0, 1] \
                    / df_prepilot[f'{metric_name}_prepilot'].var(ddof=0)
    df_res[f'{metric_name}_cuped'] = df_res[metric_name] - theta * df_res[f'{metric_name}_prepilot']
    return df_res
