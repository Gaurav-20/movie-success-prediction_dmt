import pandas as pd
import numpy as np
from dateutil import parser

df = pd.read_csv('movies-raw.csv')

df = df.drop_duplicates()

df = df[(df['runtime'] > 0) & (df['runtime'].notnull()) &
        (df['revenue'] != 0) & (df['revenue'].notnull()) &
        (df['budget'] != 0) & (df['budget'].notnull()) &
        (df['adult'] == False) &
        (df['year'] >= 1970)
        (df['vote_count'] < 5)]

df.loc[df['certification_US'].isnull(), 'certification_US'] = 'NR'
df.loc[df['certification_US'] == 'None', 'certification_US'] = 'NR'

df.loc[df['genre'].isnull(), 'genre'] = 'None'

for index, row in df.iterrows():
    try:
        date = parser.parse(row['release_date'])
        year = date.year
        newDate = f'{date.year}-{date.month}-{date.day}'
    except:
        year = np.nan
        newDate = np.nan

    df.at[index, 'year'] = year
    df.at[index, 'release_date'] = newDate

for index, row in df.iterrows():
    try:
        budget = df.at[index, 'budget']
        revenue = df.at[index, 'revenue']
        if (revenue >= budget * 2):
            success = True
        else:
            success = False
    except:
        success = np.nan

    df.at[index, 'success'] = success

for index, row in df.iterrows():
    try:
        genres = df.at[index, 'genres']
        genre = eval(genres)[0]['name']
    except:
        genre = np.nan
    df.at[index, 'genre'] = genre

for index, row in df.iterrows():
    try:
        countries = df.at[index, 'production_countries']
        country = eval(countries)[0]['name']
    except:
        country = np.nan
    df.at[index, 'country'] = country

# remove movies with country with low frequency in dataset
df = df.groupby('country').filter(lambda x: len(x) >= 5)

df = df.sort_values(by = ['release_date'])

df = df.drop(columns=['original_title',
                      'release_date',
                      'adult',
                      'popularity',
                      'genres',
                      'status',
                      'production_companies',
                      'production_countries'
                      ])

df.to_csv('movies.csv', encoding='utf-8', index=False)
print('Preprocessing Finished')
