import pandas as pd
import numpy as np

stats = {

    'GP': [60,58,60,58,62,58,58,57,60,59], 
    'W': [43,41,42,39,38,35,34,32,33,32], 
    'L': [17,17,18,19,24,23,24,25,27,27], 
    'WIN%': [.717,.707,.700,.672,.613,.603,.586,.561,.550,.542], 
    'MIN': [48.7,48.4,48.2,48.4,48.2,48.5,48.4,48.1,48.7,48.3], 
    'PTS': [118.3,114.8,117.1,114.3,111.7,115.9,114.0,119.5,114.6,108.3]

}

df = pd.DataFrame(stats, index = ('Boston Celtics', 'Milwaukee Bucks', 'Denver Nuggets', 'Philadelphia 76ers', 'Cleveland Cavaliers', 'Memphis Grizzlies', 'Brooklyn Nets', 'Sacramento Kings', 'New York Knicks', 'Miami Heat'))
df.index.name = 'Stats'
print(df)
# 1
# Row
print(df.shape[0])
# Columns
print(df.shape[1])
print(df.dtypes)

denver = df.loc['Denver Nuggets']
boston = df.loc['Boston Celtics']
print(denver)
print(boston)

assists = [26.4,24.7,29.1,25.1,24.9,25.3,25.8,26.8,22.4,23.4]
df.insert(loc=6, column='AST', value=assists)
print(df)

la = pd.DataFrame({
    'GP': 59, 
    'W': 27, 
    'L': 32, 
    'WIN%': .458, 
    'MIN': 48.6, 
    'PTS': 117.0,
    'AST': 25.2
}, index=['Los Angeles Lakers'])

df = pd.concat([df, la])
df.index.name = 'Teams'
df.sort_values(by='PTS', ascending=False, inplace=True)

print(df)

df.to_csv('NBA Teams.csv', index=True)