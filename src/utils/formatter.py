from itertools import groupby


def group_list(list_to_group: list[str]):
    return [list(j) for _, j in groupby(list_to_group)]
