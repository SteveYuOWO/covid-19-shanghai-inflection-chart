import pandas as pd
import matplotlib.pyplot as plt

plt.rc("font", family="Heiti TC")
plt.rcParams["figure.autolayout"] = True

fig, ax = plt.subplots()
fig.autofmt_xdate()
fig.canvas.set_window_title('上海感染者折线图')

df = pd.read_csv('./data.csv')

date = df.loc[:, "日期"].values[::-1]
inflection_people = df.loc[:, "感染者"].values[::-1]
asymptomatic_people = df.loc[:, "无症状感染者"].values[::-1]

plt.title("上海感染者折线图")
plt.xlabel("日期")
plt.ylabel("人数")
plt.plot(date, inflection_people, label="感染者")
plt.plot(date, asymptomatic_people, label="无症状感染者")

plt.legend(loc="upper right")
plt.show()
