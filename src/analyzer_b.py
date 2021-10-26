from itertools import groupby

from src.utils.formatter import group_list
from src.utils.pie_graph import plot_pie_graph


def output(data: dict):
    labels = []
    values = []
    for key, value in data.items():
        print(f'{key:<20} {value[0]} | {value[1]}')
        labels.append(key)
        values.append(value[0])
    plot_pie_graph(labels, values)


def analyze_column_b(data: list[str]):
    total = len(data)
    data.sort()
    data = list(map(lambda word: word.lower(), data))
    data_grouped = group_list(data)
    dict_data_grouped = {}
    for d in data_grouped:
        amount = len(d)
        dict_data_grouped[d[0]] = (amount, f'{100 * (amount / total):.2f}%')
    output(dict_data_grouped)
