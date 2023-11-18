import featurelib as fl
import dask.dataframe as dd
import datetime
import pandas as pd

from typing import List, Dict, Union#, Optional

def dask_groupby(
    data: dd.DataFrame,
    by: List[str],
    config: Dict[str, Union[str, List[str]]]
) -> dd.DataFrame:
    data_ = data.copy()
    dask_agg_config = dict()

    for col, aggs in config.items():
        aggs = aggs if isinstance(aggs, list) else [aggs]
        for agg in aggs:
            fictious_col = f'{col}_{agg}'
            data_ = data_.assign(**{fictious_col: lambda d: d[col]})
            dask_agg_config[fictious_col] = agg

    result = data_.groupby(by=by).agg(dask_agg_config)
    return result
    
    
class DayOfWeekReceiptsCalcer(fl.DateFeatureCalcer):
    name = 'day_of_week_receipts'
    keys = ['client_id']
            
    def __init__(self, delta: int, **kwargs):
        self.delta = delta
        super().__init__(**kwargs)
# Аргументы конструктора
#     engine: fl.Engine, # объект соединения с данными.
#     date_to: datetime.date, # дата, к которой рассчитываются признаки.
#    delta: int # длительность (в днях) периода времени, по которому считаются призн
            
    # Описание результата расчета
    def compute(self) -> dd.DataFrame:
    # implement me
        receipts = self.engine.get_table('receipts')

        date_to = datetime.datetime.combine(self.date_to, datetime.datetime.min.time())
        date_from = date_to - datetime.timedelta(days=self.delta)
        date_mask = (receipts['transaction_datetime'] >= date_from) & (receipts['transaction_datetime'] < date_to)
            
        features = (
            receipts
            .loc[date_mask]
            .assign(weekday=lambda d: d['transaction_datetime'].dt.weekday)
        )
        # Чтобы можно было сделать pivot_table по колонке 'weekday'
        features = features.categorize(columns=['weekday'])
        features = features.pivot_table(
            index='client_id', columns='weekday', values='transaction_id', aggfunc='count'
        )
        
        features = features[[0, 1, 2, 3, 4, 5, 6]]
        features.columns = [f'purchases_count_dw0__{self.delta}d',
                            f'purchases_count_dw1__{self.delta}d',
                            f'purchases_count_dw2__{self.delta}d',
                            f'purchases_count_dw3__{self.delta}d',
                            f'purchases_count_dw4__{self.delta}d',
                            f'purchases_count_dw5__{self.delta}d',
                            f'purchases_count_dw6__{self.delta}d',
                           ]
        features = features.reset_index()
        return features
        
        
# Объявление
class FavouriteStoreCalcer(fl.DateFeatureCalcer):
    name = 'favourite_store'
    keys = ['client_id']
    
    def __init__(self, delta: int, **kwargs):
        self.delta = delta
        super().__init__(**kwargs)
    
#     # Аргументы конструктора
#     engine: fl.Engine, # объект соединения с данными.
#     date_to: datetime.date, # дата, к которой рассчитываются признаки.
#     delta: int # длительность (в днях) периода времени, по которому считаются признаки
        
    # Описание результата расчета
    def compute(self) -> dd.DataFrame:
    # implement me
        
        receipts = self.engine.get_table('receipts')

        date_to = datetime.datetime.combine(self.date_to, datetime.datetime.min.time())
        date_from = date_to - datetime.timedelta(days=self.delta)
        date_mask = (receipts['transaction_datetime'] >= date_from) & (receipts['transaction_datetime'] < date_to)
    
        features = receipts.loc[date_mask]
        
        # Количество посещений клиентом каждого магазина
        # 'client_id', 'store_id', 'store_id_count'
        features = dask_groupby(
            features,
            by=['client_id', 'store_id'],
            config={
                "store_id": "count"
            }
        ).reset_index()
        
        # Магазины клиента с макимальным кол-вом посещений
        # 'client_id' 'store_id_count_max'
        features2 = dask_groupby(
            features,
            by=['client_id'],
            config={
                "store_id_count": "max"
            }
        ).reset_index()
        
        # Магазины с максимальным количеством покупок для каждого клиента
        features = (
            features
            .merge(
                features2,
                left_on=['client_id', 'store_id_count'],
                right_on=['client_id', 'store_id_count_max'],
                how='inner'
            )
        )[['client_id', 'store_id']]
        
        # Если есть дубли магазинов, то оставляю один с максимальным id
        features = dask_groupby(
            features,
            by=['client_id'],
            config={
                "store_id": "max"
            }
        ).reset_index()

        features.columns = ['client_id',
                    f'favourite_store_id__{self.delta}d',
                   ]
        
        return features   
        

# Объявление
import sklearn.base as skbase
class ExpressionTransformer(skbase.BaseEstimator, skbase.TransformerMixin):
    
    def __init__(self, expression: str, col_result: str):
        self.expression = expression
        self.col_result = col_result
    
#     # Аргументы конструктора
#     expression: str # “регулярное” выражение для расчета признака. (пример см. ниже)
#     col_result: str, # название колонки, в которой будет сохранен результат
        
    # Метод fit (пустой). Ничего не делает. Возвращает сам объект.
    def fit(self, *args, **kwargs):
        return self
    
    # Описание результата расчета
    def transform(self, data: pd.DataFrame, *args, **kwargs) -> pd.DataFrame:
        # implement me
        data[self.col_result] = eval(self.expression.format(d='data'))
        return data
        
        
# Объявление
import sklearn.base as skbase
import category_encoders as ce

class LOOMeanTargetEncoder(skbase.BaseEstimator, skbase.TransformerMixin):
    
    def __init__(self, col_categorical: str, col_target: str, col_result: str, **loo_params):
        self.col_categorical = col_categorical
        self.col_target = col_target
        self.col_result = col_result
        self.encoder_ = ce.LeaveOneOutEncoder(cols=[col_categorical], **(loo_params or {}))
    
#     # Аргументы конструктора
#     col_categorical: str, # название колонки с категориальным признаком, который нужно закодировать
#     col_target: str, # название колонки, из которой берется значение целевой переменной
#     col_result: str, # название колонки, в которой будет сохранен результат

    # Метод fit
    def fit(self, data: pd.DataFrame, *args, **kwargs):
        # Implement me
        
        # Суть: в результате вызова fit encoder должен "запомнить" для каждой категории в col_categorical,
        # чему в среднем равно значение col_target и сколько таких объектов в выборке.
        
        y = None
        if self.col_target in data.columns:
            y = data[self.col_target]
        self.encoder_.fit(data[self.col_categorical], y=y)
        
        return self
    
    
    # Описание результата расчета
    def transform(self, data: pd.DataFrame, *args, **kwargs) -> pd.DataFrame:
        # implement me
        
        y = None
        if self.col_target in data.columns:
            y = data[self.col_target]
        data[self.col_result] = self.encoder_.transform(data[self.col_categorical], y=y)
        return data     

