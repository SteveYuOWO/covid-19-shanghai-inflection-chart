import pandas as pd
import matplotlib.pyplot as plt
import matplotlib 
import numpy as np

matplotlib.rc("font", family="Heiti TC")

fig, ax = plt.subplots()
fig.autofmt_xdate()

df = pd.read_csv('./data.csv')

date = df.loc[:, "日期"].values
inflection_people = df.loc[:, "感染者"].values[::-1]
asymptomatic_people = df.loc[:, "无症状感染者"].values[::-1]

plt.plot(date, inflection_people, label="感染者")
plt.plot(date, asymptomatic_people, label="无症状感染者")

plt.show()
# print(date)
# print(inflection_people)
# print(asymptomatic_people)
