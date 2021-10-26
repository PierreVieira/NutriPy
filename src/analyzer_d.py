from src.utils.pie_graph import plot_pie_graph


def output(data: dict):
    labels = [key for key in data.keys()]
    values = [value[0] for value in data.values()]
    for key, value in data.items():
        print(f'{key:<20} {value[0]} | {value[1]}')
    plot_pie_graph(labels, values)


def analyze_column_d(data: list[str]):
    possibilites = {
        '1': 0,
        '2': 0,
        '3': 0,
        '4': 0,
        '5': 0,
        'não se aplica': 0,
        'nenhuma das dimensões é trabalhada': 0,
    }
    numbers = ['1.', '2.', '3.', '4.', '5.']
    for d in data:
        have_number = False
        for number in numbers:
            if number in d:
                possibilites[number[0]] += d.count(number)
                have_number = True
        if not have_number:
            if 'Não se aplica' in d:
                possibilites['não se aplica'] += 1
            elif 'Nenhuma das dimensões é trabalhada' in d:
                possibilites['nenhuma das dimensões é trabalhada'] += 1
    total = 0
    for value in possibilites.values():
        total += value
    for key, value in possibilites.copy().items():
        possibilites[key] = (value, f'{100 * value / total:.2f}%')
    output(possibilites)
