import numpy as np
import pandas as pd


def select_stratified_groups(data, strat_columns, group_size, weights=None, seed=None):
    """Подбирает стратифицированные группы для эксперимента.

    data - pd.DataFrame, датафрейм с описанием объектов, содержит атрибуты для стратификации.
    strat_columns - List[str], список названий столбцов, по которым нужно стратифицировать.
    group_size - int, размеры групп.
    weights - dict, словарь весов страт {strat: weight}, где strat - либо tuple значений элементов страт,
        например, для strat_columns=['os', 'gender', 'birth_year'] будет ('ios', 'man', 1992),
            либо просто строка/число.
        Если None, определить веса пропорционально доле страт в датафрейме data.
    seed - int, исходное состояние генератора случайных чисел для воспроизводимости
        результатов. Если None, то состояние генератора не устанавливается.

    return (data_pilot, data_control) - два датафрейма того же формата, что и data
        c пилотной и контрольной группами.
    """
    # YOUR_CODE_HERE
    if seed:
        np.random.seed(seed)
        
    # Значения в колонках для стратификации    
    df = data.copy()
    if len(strat_columns) > 1:
        df['strat_values'] = df.apply(lambda x: tuple([x[col] for col in strat_columns]), axis=1)
    else:
        df['strat_values'] = df[strat_columns[0]]
        
    # Генерация weights из исходных данных, если weights не передали
    if not weights:
        weights = df['strat_values'].value_counts(normalize=True)
        weights = dict(weights)
        
    # Число строк в каждой страте
    strat_rows = {strat: round(w * group_size) for strat, w in weights.items()}

    # Сэмплирование
    dfs_a, dfs_b = [], []
    for strat, n_rows in strat_rows.items():
        df_strat = df[df['strat_values'] == strat]
        df_sample = df_strat.sample(2 * n_rows)
        df_sample = df_sample.drop(columns='strat_values')
        dfs_a.append(df_sample.head(df_sample.shape[0] // 2))
        dfs_b.append(df_sample.tail(df_sample.shape[0] // 2))
        
    return pd.concat(dfs_a), pd.concat(dfs_b)
