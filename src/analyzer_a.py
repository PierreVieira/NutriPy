from itertools import groupby
from collections import OrderedDict

from src.utils.formatter import group_list
from src.utils.pie_graph import plot_pie_graph


def compact_diffs(data: list[str]) -> list[str]:
    return list(
        map(lambda word: word
            .strip()
            .lower()
            .strip('.')
            .replace('auxilia de educadora', 'auxiliar de educação'), data)
    )


def educador_is_professor(data) -> list[str]:
    return list(map(lambda word: word if word != 'educadora' else 'professor', data))


def is_email(word: str) -> bool:
    return '@' in word


def is_estudante(word: str) -> bool:
    return ('estudante' in word) or ('cursista' in word)


def valid_word(word: str) -> bool:
    return not is_email(word) and not is_estudante(word)


def map_wrong(data: list[str]):
    return list(map(lambda word: word if valid_word(word) else 'inválido', data))


def filter_data_to_graph(data):
    others = 0
    for key, values in data.copy().items():
        if values[0] < 6 or key == 'inválido':
            others += values[0]
            del data[key]
    data['outros'] = (others, None)
    labels = [key for key in data.keys()]
    values = [value[0] for value in data.values()]
    return labels, values


def analyze_column_a(data: list[str]):
    data = compact_diffs(data)
    data = map_wrong(data)
    data = educador_is_professor(data)
    data.sort()
    total = len(data)
    data_grouped = group_list(data)
    data_grouped_dict = OrderedDict()
    for d in data_grouped:
        amount = len(d)
        percent = amount / total
        data_grouped_dict[d[0]] = (amount, f'{percent * 100:.2f}%')
    for key, value in data_grouped_dict.items():
        print(f'{key}: {value}')
    labels, values = filter_data_to_graph(data_grouped_dict)
    plot_pie_graph(labels, values)
