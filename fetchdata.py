import requests
from bs4 import BeautifulSoup


def get_dt_data(url, infected_datas):
    request = requests.get(url)
    request.encoding = 'utf-8'
    html_text = request.text
    soup = BeautifulSoup(html_text, 'html.parser')

    for link in soup.find_all('dt'):
        link_str = link.get_text()
        if ("上海新增" in link_str and "例本土确诊 " in link_str and "例无症状" in link_str and "时" not in link_str):
            infected_datas.append(link_str)


class CovidObject:
    def __init__(self, date, inflection_people, asymptomatic_people):
        self.date = date
        self.inflection_people = inflection_people
        self.asymptomatic_people = asymptomatic_people

    def toCsvFormat(self):
        return "{},{},{}\n".format(self.date, self.inflection_people, self.asymptomatic_people)


def get_all_infected_datas():
    infected_datas = []
    covidobjs = []
    for i in range(1, 99):
        print("fetch {}/{}...".format(i, 99))
        url = 'http://m.sh.bendibao.com/news/list_17_753_{}.htm'.format(i)
        get_dt_data(url, infected_datas)
    for data in infected_datas:
        splits_array = data.split("上海新增")
        date = splits_array[0]
        splits_array2 = splits_array[1].split("例本土确诊 ")
        inflection_people = splits_array2[0]
        asymptomatic_people = splits_array2[1].split("例无症状")[0]
        covidobjs.append(CovidObject(date, inflection_people, asymptomatic_people))
    return covidobjs


covidObjs = get_all_infected_datas()
result = ["日期,感染者,无症状感染者\n"]
for covidObj in covidObjs:
    result.append(covidObj.toCsvFormat())
result_texture = ''.join(result)
f = open('data.csv', 'w')
f.write(result_texture)
f.close()
