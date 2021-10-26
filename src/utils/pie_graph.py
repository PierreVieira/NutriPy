import matplotlib.pyplot as plt


def plot_pie_graph(labels, values):
    plt.pie(values, labels=labels)
    plt.show()
