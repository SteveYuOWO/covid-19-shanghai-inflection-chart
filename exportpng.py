import pandas as pd
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
fig.autofmt_xdate()
fig.canvas.set_window_title('Shanghai Infected Persons Line Chart')

df = pd.read_csv('./data.csv')

date = df.loc[:, "日期"].values[::-1]
inflection_Persons = df.loc[:, "感染者"].values[::-1]
asymptomatic_Persons = df.loc[:, "无症状感染者"].values[::-1]

plt.figure(figsize=(len(inflection_Persons) * 1.2, 6), dpi=300)

plt.title("Shanghai Infected Persons Line Chart")
plt.xlabel("Date")
plt.ylabel("Infected Persons")
plt.plot(date, inflection_Persons, label="Infected Persons")
plt.plot(date, asymptomatic_Persons, label="Asymptomatic Infected Persons")

plt.legend()
plt.savefig('preview.png')