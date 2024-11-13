import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pytrends.request import TrendReq
from data_analysis import TimeSeriesAnalyzer

def create_tested_analyser():
    pytrend = TrendReq(hl='en-US', tz=360)
    keywords = ['Python']

    pytrend.build_payload(kw_list=keywords, timeframe='today 5-y', geo='')

    data = pytrend.interest_over_time()
    pd.set_option('future.no_silent_downcasting', True)

    if data.empty:
        print("Нет данных для отображения.")
        return None

    for keyword in keywords:
        print(f"\nАнализ ключевого слова: {keyword}")
        return TimeSeriesAnalyzer(data[keyword])

    return None

def test_moving_average_self(data_set: TimeSeriesAnalyzer):
        """Тестирование метода moving_average_self."""
        result = data_set.moving_average_self(window=12)[13:].values
        expected = data_set.moving_average(window=12)[13:].values

        pd.testing.assert_series_equal(pd.Series(result), pd.Series(expected))


    # Запуск теста
if  __name__ == "__main__":
    if (data := create_tested_analyser()) is None:
        print("No data load")
        exit(-1)
    test_moving_average_self(data)

