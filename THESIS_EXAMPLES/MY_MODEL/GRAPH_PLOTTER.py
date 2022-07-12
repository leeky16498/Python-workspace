import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

class DrawGraph:
    def time_pixeldata(self):  
        plt.style.use('seaborn') 
        experiment_data = pd.read_csv('/Users/kyungyunlee/Desktop/PYTHON_FOLDER/THESIS_EXAMPLES/data.csv')
        experiment_data.plot('time', 'y_value')
        plt.title("Tracking results")
        plt.xlabel('time')
        plt.ylabel('vertical pixel changes')
        # plt.grid()
        plt.show()
    
    def draw_frequency(self):
        pass
        # ##---------Hz data analysis--------##
        # df = pd.read_csv("/Users/kyungyunlee/Desktop/PYTHON_FOLDER/THESIS_EXAMPLES/data.csv")
        # df["peak_num"] = 0
        # cond1 = df.y_value > df.y_value.shift()
        # cond2 = df.y_value > df.y_value.shift(-1)
        # df.loc[cond1&cond2, "peak_num"] = 1
        # df = df.loc[df["peak_num"] == 1]
        # df["time_gap"] = df.x_value - df.x_value.shift()
        # df["frequencies(HZ)"] = 1 / df["time_gap"]
        # frequency_mean = df["frequencies(HZ)"].mean()
        # df_a = df.copy()
        # df_a.to_csv("/Users/kyungyunlee/Desktop/PYTHON_FOLDER/THESIS_EXAMPLES/data_frequency.csv")
        
        # ##---------Plotting calculated frequency-------##
        # plt.style.use('seaborn')
        # frequency_data = pd.read_csv("/Users/kyungyunlee/Desktop/PYTHON_FOLDER/THESIS_EXAMPLES/data_frequency.csv")
        # frequency_data.plot('x_value', 'frequencies(HZ)')
        # plt.title("Tracking results") 
        # plt.xlabel('time')
        # plt.ylabel('expected frequency')
        # # plt.text(1, 1, "Frequency : {}".format(frequency_mean))
        # # plt.grid()
        # plt.show()
