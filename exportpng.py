import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import time

DAY = 86400
INTERVAL = 2

fig, ax = plt.subplots()
fig.autofmt_xdate()
fig.canvas.manager.set_window_title('Shanghai Infected Persons Line Chart')

df = pd.read_csv('./data.csv') # data frame

date = np.array(list(map(lambda x: x.replace("月", ".").replace("日", ""), df.loc[:, "日期"].values[::-1])))
inflection_Persons = df.loc[:, "感染者"].values[::-1]
asymptomatic_Persons = df.loc[:, "无症状感染者"].values[::-1]
date_index = np.arange(0, len(date))

def get_perdict_date(start_date=1647187200, length=14):
    return [time.strftime("%-m月%-d日", time.localtime(start_date + DAY * i)) for i in range(length)]

plt.figure(figsize=(len(inflection_Persons) * 0.6, 6), dpi=400)

plt.title("Shanghai Infected Persons Line Chart")
plt.xlabel("Date")
plt.ylabel("Infected Persons")
plt.scatter(date, inflection_Persons)
plt.scatter(date, asymptomatic_Persons)
plt.plot(date, inflection_Persons, label="Infected Persons")
plt.plot(date, asymptomatic_Persons, label="Asymptomatic Infected Persons")

# polyfit to get the linear regression. y = ax + b
# But this data fits better with the exponential regression
# use y = ae^(bx) to fit the data => Equivalent y = e^(ax + b) => lny = ax + b
# Then the result shows y = e^b * e^(ax)
[a, b] = np.polyfit(date_index, np.log(asymptomatic_Persons), 1) 
plt.plot(date, np.exp(a * date_index + b), label=f"y = {np.exp(b):.1f} * e ^ ({a:.1f} * x)")

plt.legend()
plt.savefig('preview.png')