import numpy as np
import pandas as pd


def calculate_sales_metrics(df, cost_name, date_name, sale_id_name, period, filters=None):
    """Вычисляет метрики по продажам.
    
    df - pd.DataFrame, датафрейм с данными. Пример
        pd.DataFrame(
            [[820, '2021-04-03', 1, 213]],
            columns=['cost', 'date', 'sale_id', 'shop_id']
        )
    cost_name - str, название столбца с стоимостью товара
    date_name - str, название столбца с датой покупки
    sale_id_name - str, название столбца с идентификатором покупки (в одной покупке может быть несколько товаров)
    period - dict, словарь с датами начала и конца периода пилота.
        Пример, {'begin': '2020-01-01', 'end': '2020-01-08'}.
        Дата начала периода входит в полуинтервал, а дата окончания нет,
        то есть '2020-01-01' <= date < '2020-01-08'.
    filters - dict, словарь с фильтрами. Ключ - название поля, по которому фильтруем, значение - список значений,
        которые нужно оставить. Например, {'user_id': [111, 123, 943]}.
        Если None, то фильтровать не нужно.

    return - pd.DataFrame, в индексах все даты из указанного периода отсортированные по возрастанию, 
        столбцы - метрики ['revenue', 'number_purchases', 'average_check', 'average_number_items'].
        Формат данных столбцов - float, формат данных индекса - datetime64[ns].
    """
    # YOUR_CODE_HERE
    
    # Фильтрация исходного датафрейма
    df_filtered = df.copy()
    if filters:
        for col, values in filters.items():
            df_filtered = df_filtered[df_filtered[col].isin(values)]
    
    # Фильтрация дат
    df_filtered = df_filtered[(df_filtered[date_name] >= period['begin']) \
                              & ((df_filtered[date_name] < period['end']))]
    
    # Агрегаты
    # Сначала схлопываю до заказа
    df_g = df_filtered.groupby(sale_id_name).agg(**{
        date_name: (date_name, 'max'),
        cost_name: (cost_name, 'sum'),
        'number_items': (cost_name, 'count'),
    }).reset_index()
        
    # По дням
    df_g = df_g.groupby(date_name).agg(
        revenue=(cost_name, 'sum'),
        number_purchases=(sale_id_name, 'count'),
        average_number_items=('number_items', 'mean'), 
    )
    df_g['average_check'] = df_g['revenue'] / df_g['number_purchases']
    
    # Расставляю колонки в нужном порядке
    df_g = df_g[['revenue', 'number_purchases', 'average_check', 'average_number_items']].reset_index()
    
    df_g[date_name] = pd.to_datetime(df_g[date_name])
    
    # Все даты периода
    dts = pd.date_range(start=period['begin'], end=period['end'])[:-1]
    
    df_res = pd.DataFrame({date_name: dts})
    df_res = df_res.merge(df_g, on=date_name, how='left').set_index(date_name).fillna(0)
    return df_res
