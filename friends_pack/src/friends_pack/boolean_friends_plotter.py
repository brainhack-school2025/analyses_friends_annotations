import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def boolean_True_plotter(df,list_of_columns, title, x_label, y_label) :
    counts = df[list_of_columns].sum()
    max_y = counts.max() 

    plt.figure(figsize=(20, 10))
    plt.bar(counts.index, counts.values)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.yticks(np.arange(0, max_y + 50, 50))
    
    plt.show()
