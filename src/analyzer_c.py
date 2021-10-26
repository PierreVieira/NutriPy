from itertools import groupby

from src.utils.formatter import group_list
from src.utils.pie_graph import plot_pie_graph


def unify(data: list[str]) -> list[str]:
    data_unify = []
    for d in data:
        data_unify.extend(d.split(', '))
    return data_unify


def compact(key: str) -> str:
    return key[:20] + '...' if len(key) > 20 else key


def output(data_dict: dict):
    labels = []
    values = []
    for key, value in data_dict.items():
        print(f'{key:<70} {value[0]} | {value[1]}')
        labels.append(compact(key))
        values.append(value[0])
    plot_pie_graph(labels, values)


def analyze_column_c(data: list[str]):
    data = unify(data)
    data.sort()
    total = len(data)
    data = list(map(lambda word: word.lower(), data))
    data = group_list(data)
    data_dict = {}
    for d in data:
        amount = len(d)
        data_dict[d[0]] = (amount, f'{100 * (amount / total):.2f}%')
    output(data_dict)
