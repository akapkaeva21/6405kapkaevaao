from setuptools import setup, find_packages

setup(
    name='my_time_series_analysis',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
        'matplotlib',
        'statsmodels',
        'openpyxl',
        'pytrends'
    ],
)