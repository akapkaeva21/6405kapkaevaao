import pandas as pd
import numpy as np


class TimeSeriesAnalyzer:
    def __init__(self, data):
        self.data = pd.Series(data)

    def moving_average(self, window):
        if window <= 0:
            raise ValueError("Размер окна должен быть положительным.")
        m = self.data.rolling(window=window).mean()
        #print(m)
        return m

    def moving_average_self(self, window):
        if window <= 0:
            raise ValueError("Размер окна должен быть положительным целым числом.")
        averages = []
        values_buffer = np.zeros((window,), dtype=float)
        # data_length = len(self.data)
        for i, v in enumerate(self.data):
            values_buffer[i % window] = v
            # window_slice = self.data[i:i + window]
            # window_average = sum(window_slice) / window
            timestamp = self.data.index[i]
            averages.append((timestamp, np.mean(values_buffer)))
        result_series = pd.Series(dict(averages))
        #print(result_series)
        return result_series


    def calculate_difference(self):
        return self.data.diff()

    def autocorrelation(self, lag):
        if lag < 1:
            raise ValueError("Лаг должен быть положительным.")
        return self.data.autocorr(lag=lag)

    def find_extrema(self):
        peaks = self.data[(self.data.shift(1) < self.data) & (self.data.shift(-1) < self.data)]
        troughs = self.data[(self.data.shift(1) > self.data) & (self.data.shift(-1) > self.data)]
        return peaks.index.tolist(), troughs.index.tolist()

    def median_filter(self, window):
        return self.data.rolling(window=window).median()
        #df = pd.DataFrame(self.data)
        #df.to_excel(filename, index=False)
