import pandas as pd

#Complete Python Pandas Data Science Tutorial- -Reading CSVExcel files- Sorting- Filtering- Groupby-.mp4
dataframecsv = pd.read_csv("pokemon_data.csv")
#dataframeexcel = pd.read_excel("pokemon_data.xlsx")
#dataframetext = pd.read_csv("pokemon_data.txt", delimiter="\t")
#print(dataframecsv)
'''
 #                       Name    Type 1  Type 2   HP  Attack  Defense  \
0      1                  Bulbasaur     Grass  Poison   45      49       49   
1      2                    Ivysaur     Grass  Poison   60      62       63   
2      3                   Venusaur     Grass  Poison   80      82       83   
3      3      VenusaurMega Venusaur     Grass  Poison   80     100      123   
4      4                 Charmander      Fire     NaN   39      52       43   
5      5                 Charmeleon      Fire     NaN   58      64       58   
    Sp. Atk  Sp. Def  Speed  Generation  Legendary  
0         65       65     45           1      False  
1         80       80     60           1      False  
2        100      100     80           1      False  
3        122      120     80           1      False  
4         60       50     65           1      False  
5         80       65     80           1      False  
'''
print(dataframecsv.head(3)) #Read first 3 rows.  Default is five
print(dataframecsv.tail(3)) #Read last 3 rows.  Default is five
print(dataframecsv.columns) #print Index(['#', 'Name', 'Type 1', 'Type 2', 'HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed', 'Generation', 'Legendary'], dtype='object') Print headers
print(dataframecsv["Name"]) #print Name column Bulbasaur\n Ivysaur\n Venusaur . . .
print(dataframecsv["Name"].head(3)) #print first 3 rows in Name column Bulbasaur\n Ivysaur\n Venusaur
print(dataframecsv["Name"][0:3]) #print first 3 rows in Name column Bulbasaur\n Ivysaur\n Venusaur
print(dataframecsv[["Name", "Type 1", "HP"]]) #print Name Type 1 HP columns
print(dataframecsv.iloc[1]) #print the Ivysaur row in a column format.  iloc is integer location.
'''
#                   2
Name          Ivysaur
Type 1          Grass
Type 2         Poison
HP                 60
Attack             62
Defense            63
Sp. Atk            80
Sp. Def            80
Speed              60
Generation          1
Legendary       False
Name: 1, dtype: object
'''
print(dataframecsv.iloc[1:4]) #print rows 1, 2, and 3 iloc is integer location.
'''
   #                   Name Type 1  Type 2  HP  Attack  Defense  Sp. Atk  \
1  2                Ivysaur  Grass  Poison  60      62       63       80   
2  3               Venusaur  Grass  Poison  80      82       83      100   
3  3  VenusaurMega Venusaur  Grass  Poison  80     100      123      122   

   Sp. Def  Speed  Generation  Legendary  
1       80     60           1      False  
2      100     80           1      False  
3      120     80           1      False  
'''
print(dataframecsv.iloc[2, 1]) #print Venusaur.  Row 2 column 1.
for index, row in dataframecsv.iterrows():
    print(index, row) #print each row in a column format.
for index, row in dataframecsv.iterrows():
    print(index, row["Name"]) #print Now row in a column format.
'''
0 Bulbasaur
1 Ivysaur
2 Venusaur
3 VenusaurMega Venusaur
'''
print(dataframecsv.loc[dataframecsv["Type 1"] == "Fire"]) #print rows with Type 1 is Fire
'''
 #                       Name Type 1    Type 2   HP  Attack  Defense  \
4      4                 Charmander   Fire       NaN   39      52       43   
5      5                 Charmeleon   Fire       NaN   58      64       58   
6      6                  Charizard   Fire    Flying   78      84       78   
7      6  CharizardMega Charizard X   Fire    Dragon   78     130      111   
8      6  CharizardMega Charizard Y   Fire    Flying   78     104       78   
...
 Sp. Atk  Sp. Def  Speed  Generation  Legendary  
4         60       50     65           1      False  
5         80       65     80           1      False  
6        109       85    100           1      False  
7        130       85    100           1      False  
8        159      115    100           1      False  
...
'''
#print(dataframecsv.loc[[dataframecsv["Type 1"] == "Fire"], [dataframecsv["HP"] >= 100]]) #ValueError: too many values to unpack (expected 1)
print(dataframecsv.describe())  #print statistics
'''
                #          HP      Attack     Defense     Sp. Atk     Sp. Def  \
count  800.000000  800.000000  800.000000  800.000000  800.000000  800.000000   
mean   362.813750   69.258750   79.001250   73.842500   72.820000   71.902500   
std    208.343798   25.534669   32.457366   31.183501   32.722294   27.828916   
min      1.000000    1.000000    5.000000    5.000000   10.000000   20.000000   
25%    184.750000   50.000000   55.000000   50.000000   49.750000   50.000000   
50%    364.500000   65.000000   75.000000   70.000000   65.000000   70.000000   
75%    539.250000   80.000000  100.000000   90.000000   95.000000   90.000000   
max    721.000000  255.000000  190.000000  230.000000  194.000000  230.000000   

            Speed  Generation  
count  800.000000   800.00000  
mean    68.277500     3.32375  
std     29.060474     1.66129  
min      5.000000     1.00000  
25%     45.000000     2.00000  
50%     65.000000     3.00000  
75%     90.000000     5.00000  
max    180.000000     6.00000  
'''
print(dataframecsv.sort_values("Name", ascending=True))  #print all data sorted by Name column
'''
      #                       Name    Type 1    Type 2   HP  Attack  Defense  \
510  460                  Abomasnow     Grass       Ice   90      92       75   
511  460    AbomasnowMega Abomasnow     Grass       Ice   90     132      105   
68    63                       Abra   Psychic       NaN   25      20       15   
392  359                      Absol      Dark       NaN   65     130       60   
393  359            AbsolMega Absol      Dark       NaN   65     150       60   
Sp. Atk  Sp. Def  Speed  Generation  Legendary  
510       92       85     60           4      False  
511      132      105     30           4      False  
68       105       55     90           1      False  
392       75       60     75           3      False  
393      115       60    115           3      False  
'''
print(dataframecsv.sort_values(["Type 1", "HP"], ascending=[True, True]))  #print all data sorted by Type 1 and HP columns
'''
 #                   Name Type 1    Type 2   HP  Attack  Defense  \
316  292               Shedinja    Bug     Ghost    1      90       45   
230  213                Shuckle    Bug      Rock   20      10      230   
462  415                 Combee    Bug    Flying   30      30       42   
603  543               Venipede    Bug    Poison   30      45       59   
314  290                Nincada    Bug    Ground   31      45       90   
Sp. Atk  Sp. Def  Speed  Generation  Legendary  
316       30       30     40           3      False  
230       10      230      5           2      False  
462       30       42     70           4      False  
603       30       39     57           5      False  
314       30       30     40           3      False  
'''
dataframecsv["NewColumnTotal"] = dataframecsv["HP"] + dataframecsv["Attack"] + dataframecsv["Defense"] + dataframecsv["Sp. Atk"] + dataframecsv["Sp. Def"] + dataframecsv["Speed"] #Create new column NewColumnTotal
print(dataframecsv.head(3))
'''
   #       Name Type 1  Type 2  HP  Attack  Defense  Sp. Atk  Sp. Def  Speed  \
0  1  Bulbasaur  Grass  Poison  45      49       49       65       65     45   
1  2    Ivysaur  Grass  Poison  60      62       63       80       80     60   
2  3   Venusaur  Grass  Poison  80      82       83      100      100     80   

   Generation  Legendary  NewColumnTotal  
0           1      False             318  
1           1      False             405  
2           1      False             525  
'''
dataframecsv = dataframecsv.drop(columns=["NewColumnTotal"]) #Delete column
print(dataframecsv.head(3))
'''
   #       Name Type 1  Type 2  HP  Attack  Defense  Sp. Atk  Sp. Def  Speed  \
0  1  Bulbasaur  Grass  Poison  45      49       49       65       65     45   
1  2    Ivysaur  Grass  Poison  60      62       63       80       80     60   
2  3   Venusaur  Grass  Poison  80      82       83      100      100     80   

   Generation  Legendary  
0           1      False  
1           1      False  
2           1      False  
'''
dataframecsv["NewColumnTotaliloc"] = dataframecsv.iloc[:, 4:10].sum(axis=1)  #[:, 4:9] all rows and columns 4 to 9.  axis=0 is add rows.
print(dataframecsv.head(3))
'''
   #       Name Type 1  Type 2  HP  Attack  Defense  Sp. Atk  Sp. Def  Speed  \
0  1  Bulbasaur  Grass  Poison  45      49       49       65       65     45   
1  2    Ivysaur  Grass  Poison  60      62       63       80       80     60   
2  3   Venusaur  Grass  Poison  80      82       83      100      100     80   

   Generation  Legendary  NewColumnTotaliloc  
0           1      False                 318  
1           1      False                 405  
2           1      False                 525  
'''
customoutput = dataframecsv[["Name", "Type 1", "NewColumnTotaliloc"]]
print(customoutput.head(3))
'''
        Name Type 1  NewColumnTotaliloc
0  Bulbasaur  Grass                 318
1    Ivysaur  Grass                 405
2   Venusaur  Grass                 525
'''
columnslist = list(dataframecsv.columns.values)
print(columnslist) #print ['#', 'Name', 'Type 1', 'Type 2', 'HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed', 'Generation', 'Legendary', 'NewColumnTotaliloc']
customoutputfromcolumnslist = dataframecsv[columnslist[0:5] + [columnslist[-1]] + [columnslist[11]]]
print(customoutputfromcolumnslist.head(3))
'''
   #       Name Type 1  Type 2  HP  NewColumnTotaliloc  Legendary
0  1  Bulbasaur  Grass  Poison  45                 318      False
1  2    Ivysaur  Grass  Poison  60                 405      False
2  3   Venusaur  Grass  Poison  80                 525      False
'''
customoutputfromcolumnslist.to_csv("pokemon_datamodified.csv", index=False)  #save custom output .csv file as pokemon_datamodified.csv without index row number
customoutputfromcolumnslist.to_excel("pokemon_datamodified.xlsx", index=False)  #save custom output .xlsx file as pokemon_datamodified.xlsx without index row number
customoutputfromcolumnslist.to_csv("pokemon_datamodified.txt", index=False, sep="\t")  #sep is used to specify the delimiter