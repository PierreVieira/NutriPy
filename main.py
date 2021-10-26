import pandas as pd

from src.analyzer_a import analyze_column_a
from src.analyzer_b import analyze_column_b
from src.analyzer_c import analyze_column_c
from src.analyzer_d import analyze_column_d


def get_column_at_position(df, position):
    return df[df.columns[position]].tolist()


def main():
    df = pd.read_csv('input/respostas.csv')
    column = get_column_at_position(df, 3)
    analyze_column_d(column)


if __name__ == '__main__':
    main()
