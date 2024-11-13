import pandas as pd
import matplotlib.pyplot as plt
from pytrends.request import TrendReq
from data_analysis import TimeSeriesAnalyzer


def test_time_series_analyzer():
    pytrend = TrendReq(hl='en-US', tz=360)
    keywords = ['Python']

    pytrend.build_payload(kw_list=keywords, timeframe='today 5-y', geo='')

    data = pytrend.interest_over_time()
    pd.set_option('future.no_silent_downcasting', True)

    if data.empty:
        print("Нет данных для отображения.")
        return

    for keyword in keywords:
        print(f"\nАнализ ключевого слова: {keyword}")
        analyzer = TimeSeriesAnalyzer(data[keyword])

        peaks, troughs = analyzer.find_extrema()
        print(f"Пики для {keyword}: {peaks}")
        print(f"Минимумы для {keyword}: {troughs}")
        print(f"Библиотечная реализация {analyzer.moving_average(window=12)}")
        print(f"Собственная реализация {analyzer.moving_average_self(window=12)}")

        moving_avg = analyzer.moving_average(window=12)
        moving_avg_self=analyzer.moving_average_self(window=12)
        median_filtered = analyzer.median_filter(window=12)
        #print("\n", moving_avg)
        #print("\n", moving_avg_self)

        plt.figure(figsize=(10, 5))
        plt.plot(data[keyword], label=f'Данные', color='blue', alpha=0.5)
        plt.plot(moving_avg, label='Скользящее среднее', color='orange')
        plt.plot(moving_avg_self, label='Среднее своя реализация', color='violet')
        plt.scatter(peaks, data[keyword][peaks], color='red', label='Пики', zorder=5)
        plt.plot(median_filtered, label='Медианный фильтр', color='green')

        plt.legend()
        plt.show()

if __name__ == "__main__":
    test_time_series_analyzer()
