import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from model import curve_regression
import time

DAY = 86400
INTERVAL = 2

fig, ax = plt.subplots()
fig.autofmt_xdate()
fig.canvas.manager.set_window_title('Shanghai Infected Persons Line Chart')

df = pd.read_csv('./data.csv')

date = np.array(list(map(lambda x: x.replace("月", ".").replace("日", ""), df.loc[:, "日期"].values[::-1])))
inflection_Persons = df.loc[:, "感染者"].values[::-1]
asymptomatic_Persons = df.loc[:, "无症状感染者"].values[::-1]

def get_perdict_date(start_date=1647187200, length=14):
    return [time.strftime("%-m月%-d日", time.localtime(start_date + DAY * i)) for i in range(length)]

predict_date = np.array(list(map(lambda x: x.replace("月", ".").replace("日", ""), get_perdict_date(length=len(df) + INTERVAL))))
predict_Persions = curve_regression(df, len(df) + INTERVAL)

plt.figure(figsize=(len(inflection_Persons) * 0.6, 6), dpi=400)

plt.title("Shanghai Infected Persons Line Chart")
plt.xlabel("Date")
plt.ylabel("Infected Persons")
plt.scatter(date, inflection_Persons)
plt.scatter(date, asymptomatic_Persons)
plt.scatter(date, predict_Persions[:len(date)])
plt.plot(date, inflection_Persons, label="Infected Persons")
plt.plot(date, asymptomatic_Persons, label="Asymptomatic Infected Persons")
plt.plot(predict_date, predict_Persions, label="Expotional Regression")

plt.plot(time.strftime("%-m.%-d", time.localtime(time.time() - DAY)), 
         predict_Persions[-INTERVAL - 1], 'bo')
plt.text(time.strftime("%-m.%-d", time.localtime(time.time() - DAY)), 
         predict_Persions[-INTERVAL - 1], 
         f"{int(predict_Persions[-INTERVAL - 1])}", 
         ha='center', va='bottom')
now = time.time() - DAY
next_time = time.time()
for i in range(INTERVAL):
    now_str = time.strftime("%-m.%-d", time.localtime(now))
    next_str = time.strftime("%-m.%d", time.localtime(next_time))
    plt.annotate(f"+{int(predict_Persions[-(INTERVAL - i)] - predict_Persions[-(INTERVAL + 1 - i)])}", 
                 xy=(next_str, predict_Persions[-(INTERVAL - i)] - 1500))
    plt.text(next_str, predict_Persions[-(INTERVAL - i)], 
             f"{int(predict_Persions[-(INTERVAL- i)])}", 
             ha='center', va='bottom')
    
    plt.plot(next_str, predict_Persions[-(INTERVAL - i)], 'ro')
    now, next_time = next_time, next_time + DAY

plt.legend()
plt.savefig('preview.png')