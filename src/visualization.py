import matplotlib.pyplot as plt
import seaborn as sns

def plot_color_behavior(data, column1, column2, title, x_label, y_label, output_path):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=column1, y=column2, data=data)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.savefig(output_path)
    plt.close()

def plot_heatmap(data, index, columns, values, title, output_path):
    pivot_table = data.pivot_table(index=index, columns=columns, values=values)
    plt.figure(figsize=(10, 8))
    sns.heatmap(pivot_table, annot=True, fmt=".1f", cmap="viridis")
    plt.title(title)
    plt.savefig(output_path)
    plt.close()
