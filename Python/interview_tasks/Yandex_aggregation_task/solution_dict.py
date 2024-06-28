'''
Описание задачи:
Есть файл csv с оценками документов асессорами.
Формат строки данных:
worker_id, document_id, label
worker_id, document_id - целые числа
label - строка
Гарантируется, что асессор не может оценить один и тот же документ 2 раза.

Необходимо посчитать точность для каждого асессора в формате:
worker_id, accuracy,
где accuracy - это процент правильных меток, поставленных данным асессором.
Под правильной меткой понимается та, которую поставило большинство асессоров для данного документа.
Если кол-во разных меток по одному документу одинаковое, то какая - то из них случайно назначается правильной,
а остальные - неправильными
'''

import csv

with open('dataset.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    next(reader, None)  # skip the headers
    dataset = [row for row in reader]

# Подсчет количества оценок
labels_count = {}
for worker_id, document_id, label in dataset:
    if document_id in labels_count:
        labels_count[document_id][label] = labels_count[document_id].get(label, 0) + 1
    else:
        labels_count[document_id] = {}
        labels_count[document_id][label] = 1

# Определение правильной оценки
correct_labels = {}
for document_id in labels_count:
    best = max(labels_count[document_id], key=labels_count[document_id].get)
    correct_labels[document_id] = best

# Подсчет верных и неверных оценок
worker_total_labels_count = {}
worker_correct_labels_count = {}
for worker_id, document_id, label in dataset:
    worker_total_labels_count[worker_id] = worker_total_labels_count.get(worker_id, 0) + 1
    if correct_labels[document_id] == label:
        worker_correct_labels_count[worker_id] = worker_correct_labels_count.get(worker_id, 0) + 1

# Подсчет точности оценки каждым ассессором
result = {}
for worker_id in worker_total_labels_count:
    result[worker_id] = round(100 * worker_correct_labels_count.get(worker_id, 0)
                              / worker_total_labels_count[worker_id], 2)

print('Входные данные:')
print(dataset)
print('Кол-во меток к документам:')
print(labels_count)
print('Правильные метки для документов:')
print(correct_labels)
print('Общее кол-во оцененных документов асессорами:')
print(worker_total_labels_count)
print('Кол-во документов, оцененных ассесорами правильно:')
print(worker_correct_labels_count)
print('Результат (ассессор: точность оценки в %):')
print(result)
