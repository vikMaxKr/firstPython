import pandas as pd

pf=pd.read_csv('filesSort/movies.csv')
#print(pf)
#print(pf.head(2))
#print(pf.tail(2))
#print(pf.sample(3))    #any three
#print(pf[2:10])

#print(pf['imdb_rating'])

#print(pf.imdb_rating.min(), pf.imdb_rating.max(), pf.imdb_rating.mean())

avg=pf[pf.industry=='Bollywood']

print(avg.imdb_rating.min(), avg.imdb_rating.max(),avg.imdb_rating.mean())

print(pf.shape)
print(pf.industry.unique())
print(pf.industry.value_counts())
