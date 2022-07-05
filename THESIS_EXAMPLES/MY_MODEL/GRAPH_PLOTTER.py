import pandas as pd 
import matplotlib.pyplot as plt

class DrawGraph:
    def __init__(self):  
        plt.style.use('seaborn') 
        experiment_data = pd.read_csv('/Users/kyungyunlee/Desktop/PYTHON/THESIS_EXAMPLES/data.csv')
        experiment_data.plot('x_value', 'y_value')
        plt.title("Tracking results")
        plt.xlabel('time')
        plt.ylabel('vertical pixel changes')
        # plt.grid()
        plt.show()
