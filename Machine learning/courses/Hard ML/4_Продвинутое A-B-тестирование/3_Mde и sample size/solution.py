import numpy as np
import pandas as pd
from scipy import stats


def estimate_sample_size(df, metric_name, effects, alpha=0.05, beta=0.2):
    """Оцениваем sample size для списка эффектов.

    df - pd.DataFrame, датафрейм с данными
    metric_name - str, название столбца с целевой метрикой
    effects - List[float], список ожидаемых эффектов. Например, [1.03] - увеличение на 3%
    alpha - float, ошибка первого рода
    beta - float, ошибка второго рода

    return - pd.DataFrame со столбцами ['effect', 'sample_size']    
    """
    # YOUR_CODE_HERE
    t_alpha = stats.norm.ppf(1 - alpha / 2)
    t_beta = stats.norm.ppf(1 - beta)
    # ddof=0 нужен, чтобы pandas считал std также, как и numpy, который использует автор задания
    std = df[metric_name].std(ddof=0)
    ns = []
    for effect in effects:
        epsilon = df[metric_name].mean() * (effect - 1)
        n = ((t_alpha + t_beta) ** 2 * 2 * std ** 2) / epsilon ** 2
        ns.append(int(np.ceil(n)))
    return pd.DataFrame({'effect': effects, 'sample_size': ns})
