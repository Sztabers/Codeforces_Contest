import json
import urllib.request
from collections import Counter
import pandas as pd
import matplotlib.pyplot as plt

user_URL = 'https://codeforces.com/api/contest.list?gym=true'

with urllib.request.urlopen(user_URL) as url:
		user_data = json.loads(url.read().decode())

countries = []

for contest in user_data['result']:
    countries.append(contest.get('country'))

counter = Counter(countries)

df = pd.DataFrame.from_records(list(dict(counter).items()), columns=['Country', 'Contests'])

print(list(dict(counter).items()))

df = df.sort_values(['Contests'], ascending=False)

df = df.drop(0)

df = df.head(10)



df.plot(x ='Country', y='Contests', kind = 'bar')
plt.show()


