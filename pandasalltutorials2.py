import numpy as np
import pandas as pd

#Python - Pandas Tutorial _ Intro to DataFrames-e60ItwlZTKM
#data source https://github.com/joeyajames/Python/blob/master/Pandas/pandas_weather.py
def header(msg):
  print("-" * 50)
  print("[" + msg + "]")


header("1. load hard-coded data into a dfdataframe") #return [1. load hard-coded data into a dfdataframe]
dfdataframe = pd.DataFrame([['Jan', 58, 42, 74, 22, 2.95], ['Feb', 61, 45, 78, 26, 3.02], ['Mar', 65, 48, 84, 25, 2.34], ['Apr', 67, 50, 92, 28, 1.02], ['May', 71, 53, 98, 35, 0.48], ['Jun', 75, 56, 107, 41, 0.11], ['Jul', 77, 58, 105, 44, 0.0], ['Aug', 77, 59, 102, 43, 0.03], ['Sep', 77, 57, 103, 40, 0.17], ['Oct', 73, 54, 96, 34, 0.81], ['Nov', 64, 48, 84, 30, 1.7], ['Dec', 58, 42, 73, 21, 2.56]], index=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], columns=['month', 'avg_high', 'avg_low', 'record_high', 'record_low', 'avg_precipitation'])  #RM:  index is the row numbers starting with zero
print(dfdataframe)
'''
   month  avg_high  avg_low  record_high  record_low  avg_precipitation
0    Jan        58       42           74          22               2.95
1    Feb        61       45           78          26               3.02
2    Mar        65       48           84          25               2.34
3    Apr        67       50           92          28               1.02
4    May        71       53           98          35               0.48
5    Jun        75       56          107          41               0.11
6    Jul        77       58          105          44               0.00
7    Aug        77       59          102          43               0.03
8    Sep        77       57          103          40               0.17
9    Oct        73       54           96          34               0.81
10   Nov        64       48           84          30               1.70
11   Dec        58       42           73          21               2.56
'''
header("2. read text file into a df") #return [2. read text file into a df]
filename = "fremontweather.txt"
dfdataframe = pd.read_csv(filename)
print(dfdataframe)
'''
   month  avg_high  avg_low  record_high  record_low  avg_precipitation
0    Jan        58       42           74          22               2.95
1    Feb        61       45           78          26               3.02
2    Mar        65       48           84          25               2.34
3    Apr        67       50           92          28               1.02
4    May        71       53           98          35               0.48
5    Jun        75       56          107          41               0.11
6    Jul        77       58          105          44               0.00
7    Aug        77       59          102          43               0.03
8    Sep        77       57          103          40               0.17
9    Oct        73       54           96          34               0.81
10   Nov        64       48           84          30               1.70
11   Dec        58       42           73          21               2.56
'''
header("3. df.head()") #return [3. df.head()]
print(dfdataframe.head())  #RM:  .head always return the first five rows
'''
  month  avg_high  avg_low  record_high  record_low  avg_precipitation
0   Jan        58       42           74          22               2.95
1   Feb        61       45           78          26               3.02
2   Mar        65       48           84          25               2.34
3   Apr        67       50           92          28               1.02
4   May        71       53           98          35               0.48
'''
header("3. df.tail(3)") #return [3. df.tail(3)]
print(dfdataframe.tail(3))
'''
   month  avg_high  avg_low  record_high  record_low  avg_precipitation
9    Oct        73       54           96          34               0.81
10   Nov        64       48           84          30               1.70
11   Dec        58       42           73          21               2.56
'''
header("4. df.dtypes")
print(dfdataframe.dtypes)
'''
month                 object
avg_high               int64
avg_low                int64
record_high            int64
record_low             int64
avg_precipitation    float64
dtype: object
'''
header("4. df.index")
print(dfdataframe.index) #print RangeIndex(start=0, stop=12, step=1)
header("4. df.columns")
print(dfdataframe.columns) #print Index(['month', 'avg_high', 'avg_low', 'record_high', 'record_low', 'avg_precipitation'], dtype='object')
print(dfdataframe.columns[0]) #print month
header("4. df.values")
print(dfdataframe.values)
'''
[['Jan' 58 42 74 22 2.95]
 ['Feb' 61 45 78 26 3.02]
 ['Mar' 65 48 84 25 2.34]
 ['Apr' 67 50 92 28 1.02]
 ['May' 71 53 98 35 0.48]
 ['Jun' 75 56 107 41 0.11]
 ['Jul' 77 58 105 44 0.0]
 ['Aug' 77 59 102 43 0.03]
 ['Sep' 77 57 103 40 0.17]
 ['Oct' 73 54 96 34 0.81]
 ['Nov' 64 48 84 30 1.7]
 ['Dec' 58 42 73 21 2.56]]
'''
header("5. df.describe()")
print(dfdataframe.describe())
'''
        avg_high    avg_low  record_high  record_low  avg_precipitation
count  12.000000  12.000000    12.000000   12.000000          12.000000
mean   68.583333  51.000000    91.333333   32.416667           1.265833
std     7.366488   6.060303    12.323911    8.240238           1.186396
min    58.000000  42.000000    73.000000   21.000000           0.000000
25%    63.250000  47.250000    82.500000   25.750000           0.155000
50%    69.000000  51.500000    94.000000   32.000000           0.915000
75%    75.500000  56.250000   102.250000   40.250000           2.395000
max    77.000000  59.000000   107.000000   44.000000           3.020000
'''
header("6. df.sort_values('record_high', ascending=False)")
print(dfdataframe.sort_values('record_high', ascending=False))
'''
   month  avg_high  avg_low  record_high  record_low  avg_precipitation
5    Jun        75       56          107          41               0.11
6    Jul        77       58          105          44               0.00
8    Sep        77       57          103          40               0.17
7    Aug        77       59          102          43               0.03
4    May        71       53           98          35               0.48
9    Oct        73       54           96          34               0.81
3    Apr        67       50           92          28               1.02
2    Mar        65       48           84          25               2.34
10   Nov        64       48           84          30               1.70
1    Feb        61       45           78          26               3.02
0    Jan        58       42           74          22               2.95
11   Dec        58       42           73          21               2.56
'''
twosorts = dfdataframe.sort_values("record_high", ascending=False).sort_values("avg_high", ascending=False)  #sort first starts on the furthest right of the .sortvalues()
print(twosorts)
'''
   month  avg_high  avg_low  record_high  record_low  avg_precipitation
6    Jul        77       58          105          44               0.00
8    Sep        77       57          103          40               0.17
7    Aug        77       59          102          43               0.03
5    Jun        75       56          107          41               0.11
9    Oct        73       54           96          34               0.81
4    May        71       53           98          35               0.48
3    Apr        67       50           92          28               1.02
2    Mar        65       48           84          25               2.34
10   Nov        64       48           84          30               1.70
1    Feb        61       45           78          26               3.02
0    Jan        58       42           74          22               2.95
11   Dec        58       42           73          21               2.56
'''
header("7. slicing -- df.avg_low")
print(dfdataframe.avg_low) #index with single column or print one column
'''
0     42
1     45
2     48
3     50
4     53
5     56
6     58
7     59
8     57
9     54
10    48
11    42
Name: avg_low, dtype: int64
'''
header("7. slicing -- df['avg_low']")
print(dfdataframe['avg_low'])  #print one column
'''
0     42
1     45
2     48
3     50
4     53
5     56
6     58
7     59
8     57
9     54
10    48
11    42
Name: avg_low, dtype: int64
'''
header("7. slicing -- df[2:4]") #index with single column
print(dfdataframe[2:4]) #rows 2 to 3
'''
  month  avg_high  avg_low  record_high  record_low  avg_precipitation
2   Mar        65       48           84          25               2.34
3   Apr        67       50           92          28               1.02
'''
header("7. slicing -- df[['avg_low','avg_high']]")
print(dfdataframe[['avg_low', 'avg_high']]) #print two columns
'''
    avg_low  avg_high
0        42        58
1        45        61
2        48        65
3        50        67
4        53        71
5        56        75
6        58        77
7        59        77
8        57        77
9        54        73
10       48        64
11       42        58
'''
header("7. slicing -- df.loc[:,['avg_low','avg_high']]")
print(dfdataframe.loc[:, ['avg_low', 'avg_high']]) # multiple columns: df.loc[from_row:to_row,['column1','column2']].  .loc is location.  print two columns
'''
    avg_low  avg_high
0        42        58
1        45        61
2        48        65
3        50        67
4        53        71
5        56        75
6        58        77
7        59        77
8        57        77
9        54        73
10       48        64
11       42        58
'''
header("7. slicing scalar value -- df.loc[9,['avg_precipitation']]")
print(dfdataframe.loc[9, ['avg_precipitation']])  #print the ninth row avg_precipitation data cell
'''
avg_precipitation    0.81
Name: 9, dtype: object
'''
print(dfdataframe.loc[8:11, ['avg_precipitation', "avg_high", "avg_low"]]) #print the rows 8-11 and columns avg_precipitation, avg_high, and avg_low
'''
    avg_precipitation  avg_high  avg_low
8                0.17        77       57
9                0.81        73       54
10               1.70        64       48
11               2.56        58       42
'''
header("7. df.iloc[3:5,[0,3]]") #index location can receive range or list of indices.  ,iloc is index location print row 3 and 4 print column 0, column1, and column 2.
print(dfdataframe.iloc[3:5, [0, 3]])  #columns are index, month, and record_high columns 0-2.
'''
  month  record_high
3   Apr           92
4   May           98
'''
header("8. df[df.avg_precipitation > 1.0]") #filter on column values
print(dfdataframe[dfdataframe.avg_precipitation > 1.0])
'''
   month  avg_high  avg_low  record_high  record_low  avg_precipitation
0    Jan        58       42           74          22               2.95
1    Feb        61       45           78          26               3.02
2    Mar        65       48           84          25               2.34
3    Apr        67       50           92          28               1.02
10   Nov        64       48           84          30               1.70
11   Dec        58       42           73          21               2.56
'''
header("8. df[df['month'].isin['Jun','Jul','Aug']]")
print(dfdataframe[dfdataframe['month'].isin(['Jun', 'Jul', 'Aug'])])
'''
  month  avg_high  avg_low  record_high  record_low  avg_precipitation
5   Jun        75       56          107          41               0.11
6   Jul        77       58          105          44               0.00
7   Aug        77       59          102          43               0.03
'''
rowsoneonethree = dfdataframe[dfdataframe["avg_precipitation"].isin([1.02])]
print(rowsoneonethree)
'''
  month  avg_high  avg_low  record_high  record_low  avg_precipitation
3   Apr        67       50           92          28               1.02
'''
header("9. df.loc[9,['avg_precipitation']] = 101.3")
dfdataframe.loc[9, ['avg_precipitation']] = 101.3 #assign a cell value given the row and column.  Row 9 and column avg_precipitation.
print(dfdataframe.iloc[9])
'''
month                  Oct
avg_high                73
avg_low                 54
record_high             96
record_low              34
avg_precipitation    101.3
Name: 9, dtype: object
'''
print(dfdataframe.iloc[9:10])
'''
  month  avg_high  avg_low  record_high  record_low  avg_precipitation
9   Oct        73       54           96          34              101.3
'''
header("9. df.loc[9,['avg_precipitation']] = np.nan")
dfdataframe.loc[9, ['avg_precipitation']] = np.nan #assign a cell value given the row and column.  Row 9 and column avg_precipitation not a number nan
print(dfdataframe.iloc[9:10])
'''
  month  avg_high  avg_low  record_high  record_low  avg_precipitation
9   Oct        73       54           96          34                NaN
'''
header("9. df.loc[:,'avg_low'] = np.array([5] * len(df))")
dfdataframe.loc[:, 'avg_low'] = np.array([5] * len(dfdataframe))  #all rows avg_low column change avg_low to the number 5
#also
#dfdataframe.loc[:, 'avg_low'] = 5  #all rows avg_low column change avg_low to the number 5
print(dfdataframe.head())
'''
  month  avg_high  avg_low  record_high  record_low  avg_precipitation
0   Jan        58        5           74          22               2.95
1   Feb        61        5           78          26               3.02
2   Mar        65        5           84          25               2.34
3   Apr        67        5           92          28               1.02
4   May        71        5           98          35               0.48
'''
header("9. df['avg_day'] = (df.avg_low + df.avg_high) / 2")
dfdataframe['avg_day'] = (dfdataframe.avg_low + dfdataframe.avg_high) / 2 #add a column avg_day
print(dfdataframe.head())
'''
  month  avg_high  avg_low  record_high  record_low  avg_precipitation  \
0   Jan        58        5           74          22               2.95   
1   Feb        61        5           78          26               3.02   
2   Mar        65        5           84          25               2.34   
3   Apr        67        5           92          28               1.02   
4   May        71        5           98          35               0.48   

   avg_day  
0     31.5  
1     33.0  
2     35.0  
3     36.0  
4     38.0 
'''
header("10. df.rename(columns = {'avg_precipitation':'new column name avg_rain'}, inplace=True)")
dfdataframe.rename(columns={'avg_precipitation': 'new column name avg_rain'}, inplace=True) #rename 1 column use dictionary to rename column
print(dfdataframe.head())
'''
  month  avg_high  avg_low  record_high  record_low  new column name avg_rain  \
0   Jan        58        5           74          22                      2.95   
1   Feb        61        5           78          26                      3.02   
2   Mar        65        5           84          25                      2.34   
3   Apr        67        5           92          28                      1.02   
4   May        71        5           98          35                      0.48   

   avg_day  
0     31.5  
1     33.0  
2     35.0  
3     36.0  
4     38.0
'''
header("10. df.columns = ['month','av_hi','av_lo','rec_hi','rec_lo','av_rain','av_day']")
dfdataframe.columns = ['month', 'av_hi', 'av_lo', 'rec_hi', 'rec_lo', 'av_rain', 'av_day'] #rename all columns using a list in order from left to right
print(dfdataframe.head())
'''
  month  av_hi  av_lo  rec_hi  rec_lo  av_rain  av_day
0   Jan     58      5      74      22     2.95    31.5
1   Feb     61      5      78      26     3.02    33.0
2   Mar     65      5      84      25     2.34    35.0
3   Apr     67      5      92      28     1.02    36.0
4   May     71      5      98      35     0.48    38.0
'''
header("11. iterate rows of df with a for loop")
for index, row in dfdataframe.iterrows():  #iterate a dataframe
  print(index, row["month"], row["av_hi"])
  '''
    0 Jan 58
    1 Feb 61
    2 Mar 65
    3 Apr 67
    4 May 71
    5 Jun 75
    6 Jul 77
    7 Aug 77
    8 Sep 77
    9 Oct 73
    10 Nov 64
    11 Dec 58
    '''
dfdataframe.to_csv('foo.csv') #write Panda to .csv file
