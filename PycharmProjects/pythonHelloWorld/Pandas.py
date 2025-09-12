import pandas as pd
from numpy import int64

pf=pd.read_csv('filesSort/movies.csv')
#print(pf)
#print(pf.head(2))
#print(pf.tail(2))
#print(pf.sample(3))    #any three
#print(pf[2:10])
#print(pf.describe())
#print(pf.info())

# setting custom index
#pf.head().set_index('name', inplace=True)


# iloc and loc are the two indexing techniques that help us in selecting specific rows and columns.
# iloc is Integer-based Indexing
# pf.iloc[Rows, Columns]

#pff=pf.iloc[2,1]
# pf.iloc[2, -1]
# pf.iloc[1:5, 4:6]


data = {'A': [10, 20, 30], 'B': [40, 50, 60]}
df = pd.DataFrame(data, index=['row1', 'row2', 'row3'])
print(df)

print(df.loc['row1'])  # Accessing row using label
print(df.loc['row1', 'A'])  # Accessing specific value
print(df.loc['row1':'row2'])  # Includes 'row1' and 'row2' includes start and endIndex
print('--------dataframe---------')




# dropping null values using dropna()  in-place makes changes to the original DataFrame
# pf.dropna(inplace= True)

#print(pf['imdb_rating'])

#print(pf.imdb_rating.min(), pf.imdb_rating.max(), pf.imdb_rating.mean())

# avg=pf[pf.industry=='Bollywood']
#
# print(avg.imdb_rating.min(), avg.imdb_rating.max(),avg.imdb_rating.mean())
#
# print(pf.shape)
# print(pf.industry.unique())
# print(pf.industry.value_counts())

# pd.Series(data, index, dtype)
# data- it can be a list, a list of lists or even a dictionary
# index - the index can be explicitly defined for different values if required
#dtype- represents the data type used in series
series=pd.Series(data=[12,13,14,15,45,46,47,78,789])
#print(pd.Series([12,34,56,67], dtype=int64).index)

print(series.values)
print(series.index)
print(series[2:4])

cars_mod=pd.Series(data=[2000, 3000, 4000, 5000], index=['swift', 'Jazz', 'suzuki', 'Atlas'])
print(cars_mod)

# series can also be viewed as a specialized dictionary where key acts as index and
#corresponding values as values.

car_price_dict={'car': 7000000,
                'Byke': 7000,
                'fly' :4000 }

pd.Series(car_price_dict)


#       --------DATA-FRAME----------
# pd.DataFrame(data, index, columns)
# data - data can contain Series or list-like objects. If data is a dictionary, column order follows insertion order
#index - by default, it will be RangeIndex(0,1,2,3,...n) if no explicit index is provided
#column - if data contains labels, it will use the same, else default to RangeIndex(0,1,2,...n)

car_price={'Swift': 70000,
           'Ford': 400000,
           'Tata': 300000,
           'Mahindra': 200000}

car_manu={'Swift': 'Hyundi',
           'Ford': 'Tesla',
           'Tata': 'Tata',
           'Mahindra': 'Mahi'}

cars=pd.DataFrame({'Price': car_price, 'Manufacturer': car_manu})
print(cars)

sub_marks=pd.DataFrame([{'vikas': 20, 'Ram': 32},
              {'Abdul': 34, 'Prakash': 45}],
             index=['Maths', 'Physics'])

print(sub_marks)
