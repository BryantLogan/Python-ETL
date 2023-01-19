import pandas

CSV_URL = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us.csv'
RECOVERY_URL = 'https://raw.githubusercontent.com/datasets/covid-19/master/data/time-series-19-covid-combined.csv'
data = pandas.read_csv(CSV_URL)
recovered = pandas.read_csv(RECOVERY_URL)

date = sorted(data)[1]
print(date)

# date, cases, deaths, recoveries 