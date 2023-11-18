import numpy as np
from typing import Iterable

class UpliftTreeRegressor:
    def __init__(
        self,
        max_depth: int = 3, # максимальная глубина дерева.
        min_samples_leaf: int = 1000, # минимальное необходимое число обучающих объектов в листе дерева.
        min_samples_leaf_treated: int = 300, # минимальное необходимое число обучающих объектов с Т=1 в листе дерева.
        min_samples_leaf_control: int = 300, # минимальное необходимое число обучающих объектов с Т=0 в листе дерева.
    ):
        self.max_depth = max_depth
        self.min_samples_leaf = min_samples_leaf
        self.min_samples_leaf_treated = min_samples_leaf_treated
        self.min_samples_leaf_control = min_samples_leaf_control
    
    def fit(
        self,
        X: np.ndarray,  # массив (n * k) с признаками.
        treatment: np.ndarray,  # массив (n) с флагом воздействия.
        y: np.ndarray  # массив (n) с целевой переменной.
    ) -> None:
        # fit the model
        
        def ate(idx: np.ndarray) -> float:
            """
            Расчет ATE (Average Treatment Effect) = E[Y ∣T = 1] − E[Y ∣T = 0]
            """
            y_ate = y[idx]
            tr_ate = treatment[idx]
            return (y_ate * tr_ate).sum() / tr_ate.sum() - (y_ate * (1 - tr_ate)).sum() / (1 - tr_ate).sum()
        
        def compute_delta_delta_p(idx1: np.ndarray, idx2: np.ndarray) -> float:
            """
            Расчет критерия для разбиения элементов по листам
            """
            tau_left = (y[idx1] * treatment[idx1]).sum() / treatment[idx1].sum() \
                        - (y[idx1] * (1 - treatment[idx1])).sum() / (1 - treatment[idx1]).sum()
            tau_right = (y[idx2] * treatment[idx2]).sum() / treatment[idx2].sum() \
                        - (y[idx2] * (1 - treatment[idx2])).sum() / (1 - treatment[idx2]).sum()
            return abs(tau_left - tau_right)
        
        
        def build(idx: np.ndarray, parent: int, depth: int) -> None:
            """
            Построение дерева и выделение 2 новых листов
            :idx: np.ndarray - индексы элементов в текущем листе
            """
            
            # Построение текущего листа
            leaf_id = len(self.tree)  # id текущего листа
            leaf = {
                'item_ids': idx,
                'n_items': len(idx),
                'ATE': ate(idx),
                'split_feat': None,
                'split_threshold': None,
                'parent': parent,
                'depth': depth,
                'children': []
            }
            self.tree.append(leaf)
            if parent >= 0:
                self.tree[parent]['children'].append(leaf_id)
            
            if depth == self.max_depth:
                return  # Достигли предельной глубины дерева
            
            items = X[idx]  # Все элементы в листе
            ddps = {}  # словарь для значений критерия для всех возможных разбиений
            # Перебираю все признаки
            for i in range(X.shape[1]):
                # Перебираю варианты порога
                column_values = items[:, i]
                unique_values = np.unique(column_values)
                if len(unique_values) > 10:
                    percentiles = np.percentile(column_values, [3, 5, 10, 20, 30, 50, 70, 80, 90, 95, 97])
                else:
                    percentiles = np.percentile(column_values, [10, 50, 90])
                threshold_options = np.unique(percentiles)  # Значения порогов для перебора
                for thr in threshold_options:
                    # Разбиваю признак по порогу
                    item_idx_left = idx[column_values <= thr]
                    item_idx_right = idx[column_values > thr]
                    if min(len(item_idx_left), len(item_idx_right)) < self.min_samples_leaf \
                            or treatment[item_idx_left].sum() < self.min_samples_leaf_treated \
                            or len(items) - treatment[item_idx_left].sum() < self.min_samples_leaf_control \
                            or treatment[item_idx_right].sum() < self.min_samples_leaf_treated \
                            or len(items) - treatment[item_idx_right].sum() < self.min_samples_leaf_control:
                        continue  # Пропускаем порог, т.к. после разбиения не выполняются требования к новым листам
                    # Считаю критерий delta_delta_p
                    ddp = compute_delta_delta_p(item_idx_left, item_idx_right)
                    ddps[(i, thr)] = ddp
            
            if not ddps:
                return  # Ни один вариант разбиения не подошел
            # Выбираем наилучшее по значению критерия разбиение.
            factor, threshold = max(ddps, key=lambda x: ddps[x])
            # Запоминаю условия разбиения (фактор и порог) в текущий лист
            self.tree[leaf_id]['split_feat'] = f'feat{factor}'
            self.tree[leaf_id]['split_threshold'] = threshold
            # По лучшему разбиению создаем левую вершину и правую вершину.
            column_values = items[:, factor]
            item_idx_left = column_values <= threshold
            item_idx_right = column_values > threshold
            
            build(idx[item_idx_left], parent=leaf_id, depth=depth+1)
            build(idx[item_idx_right], parent=leaf_id, depth=depth+1)
            # --- end build()---
        
        self.tree = []
        # Запуск построения дерева
        build(np.arange(len(X)), parent=-1, depth=0)
        # В рамках этого задания первый узел считается нулевым (depth=0)
        # Хотя в стандартных библиотеках он первый.
    
    
    def predict(self, X: np.ndarray) -> Iterable[float]:
        # compute predictions
        predictions = []
        for item in X:
            leaf_id = 0
            # Пока есть дети
            while self.tree[leaf_id]['children']:
                factor = int(self.tree[leaf_id]['split_feat'][4:])
                if item[factor] <= self.tree[leaf_id]['split_threshold']:
                    leaf_id = self.tree[leaf_id]['children'][0]
                else:
                    leaf_id = self.tree[leaf_id]['children'][1]
            pred = self.tree[leaf_id]['ATE']
            predictions.append(pred)
        
        return predictions
