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
import pandas as pd

dataframecsv = pd.read_csv("pokemon_data.csv")
#print(dataframecsv.loc[dataframecsv["Type 1"] == "Grass"]) #print rows with Type 1 Grass
#print(dataframecsv.loc[(dataframecsv["Type 1"] == "Grass") & (dataframecsv["Type 2"] == "Poison")]) #print rows with Type 1 Grass and Type 2 Poison
#print(dataframecsv.loc[(dataframecsv["Type 1"] == "Grass") | (dataframecsv["Type 2"] == "Poison")]) #print rows with Type 1 Grass or Type 2 Poison
grasspoisonhp70plus = dataframecsv.loc[(dataframecsv["Type 1"] == "Grass") & (dataframecsv["Type 2"] == "Poison") & (dataframecsv["HP"] > 70)]
#print(grasspoisonhp70plus) #print rows with Type 1 Grass and Type 2 Poison and HP greater than 70
#grasspoisonhp70plus.to_csv("grasspoisonhp70plusexporttocsvfile") #export rows with Type 1 Grass and Type 2 Poison and HP greater than 70 to .csv file
resetindex = grasspoisonhp70plus.reset_index(drop=False) #reset index number to zero for filtered data.  Set drop to False to keep Original index number column from source data.
#print(resetindex) #a new column leftmost new index column starting at zero.
'''
   index    #                   Name Type 1  Type 2   HP  Attack  Defense  \
0      2    3               Venusaur  Grass  Poison   80      82       83
1      3    3  VenusaurMega Venusaur  Grass  Poison   80     100      123
2     50   45              Vileplume  Grass  Poison   75      80       85
3     77   71             Victreebel  Grass  Poison   80     105       65
4    652  591              Amoonguss  Grass  Poison  114      85       70
...
'''
megapokemoncasesensitive = dataframecsv.loc[dataframecsv["Name"].str.contains("Mega")]
#print(megapokemoncasesensitive) #print rows Pokemon contains Mega
notmegapokemoncasesensitive = dataframecsv.loc[~dataframecsv["Name"].str.contains("Mega")]
#print(notmegapokemoncasesensitive) #print rows Pokemon not contains Mega
import re
# fireorgrasspokemonregularexpressions = dataframecsv.loc[dataframecsv["Type 1"].str.contains("Fire|Grass", regex=True)]
# print(fireorgrasspokemonregularexpressions)
fireorgrasspokemonregularexpressions = dataframecsv.loc[dataframecsv["Type 1"].str.contains("fire|grass", flags=re.I, regex=True)] #re.I ignores case
#print(fireorgrasspokemonregularexpressions)
pokemonnameincludespi = dataframecsv.loc[dataframecsv["Name"].str.contains("pi[a-z]*", flags=re.I, regex=True)] #re.I ignores case
#print(pokemonnameincludespi)
pokemonnamebeginswithpi = dataframecsv.loc[dataframecsv["Name"].str.contains("^pi[a-z]*", flags=re.I, regex=True)] #re.I ignores case
#print(pokemonnamebeginswithpi)
renameflamerpokemon = dataframecsv.loc[dataframecsv["Type 1"] == "Fire", "Type 1"] = "Flamer"
#print(dataframecsv) #Pokemon with Type 1 Fire changed to Flamer
'''
#                       Name    Type 1  Type 2   HP  Attack  Defense  \
0      1                  Bulbasaur     Grass  Poison   45      49       49
1      2                    Ivysaur     Grass  Poison   60      62       63
2      3                   Venusaur     Grass  Poison   80      82       83
3      3      VenusaurMega Venusaur     Grass  Poison   80     100      123
4      4                 Charmander    Flamer     NaN   39      52       43
...
'''
dataframecsv.loc[dataframecsv["Type 1"] == "Flamer", "Type 1"] = "Fire" #change Flamer back to Fire
dataframecsv.loc[dataframecsv["Type 1"] == "Fire", "Legendary"] = True #set Type 1 Fire pokemon Legendary to True
dataframecsv = pd.read_csv("pokemon_data.csv") #reset Pokemon data csv
#update multiple columns multiple values
totalgreater500500club = dataframecsv.loc[dataframecsv["HP"] + dataframecsv["Attack"] + dataframecsv["Defense"] + dataframecsv["Sp. Atk"] + dataframecsv["Sp. Def"] + dataframecsv["Speed"] > 500, ["Type 1", "Type 2"]] = ["500 Club", "5000 Clubs"]
#print(dataframecsv) #numbers greater than 500 Type 1 and Type 2 changed to 500 Club
'''
#                       Name    Type 1      Type 2   HP  Attack  \
0      1                  Bulbasaur     Grass      Poison   45      49   
1      2                    Ivysaur     Grass      Poison   60      62   
2      3                   Venusaur  500 Club  5000 Clubs   80      82   
3      3      VenusaurMega Venusaur  500 Club  5000 Clubs   80     100   
4      4                 Charmander      Fire         NaN   39      52   
...
'''
dataframecsv = pd.read_csv("pokemon_data.csv") #reset Pokemon data csv
#print(dataframecsv.groupby(["Type 1"]).mean().sort_values("Defense", ascending=False))  #mean, sum, count
'''
                   #         HP      Attack     Defense    Sp. Atk    Sp. Def  \
Type 1                                                                          
Steel     442.851852  65.222222   92.703704  126.370370  67.518519  80.629630   
Rock      392.727273  65.363636   92.863636  100.795455  63.340909  75.477273   
Dragon    474.375000  83.312500  112.125000   86.375000  96.843750  88.843750   
Ground    356.281250  73.781250   95.750000   84.843750  56.468750  62.750000   
Ghost     486.500000  64.437500   73.781250   81.187500  79.343750  76.468750   
Water     303.089286  72.062500   74.151786   72.946429  74.812500  70.517857
...
'''
createvariablereturncount = dataframecsv.groupby(["Type 1"]).count()
#print(createvariablereturncount)
'''
            #  Name  Type 2   HP  Attack  Defense  Sp. Atk  Sp. Def  Speed  \
Type 1                                                                       
Bug        69    69      52   69      69       69       69       69     69   
Dark       31    31      21   31      31       31       31       31     31   
Dragon     32    32      21   32      32       32       32       32     32   
Electric   44    44      17   44      44       44       44       44     44   
Fairy      17    17       2   17      17       17       17       17     17   
Fighting   27    27       7   27      27       27       27       27     27 
...
'''
#print(createvariablereturncount["#"])
'''
Type 1
Bug          69
Dark         31
Dragon       32
Electric     44
Fairy        17
Fighting     27
...
Steel        27
Water       112
Name: #, dtype: int64
'''
#print(dataframecsv.groupby(["Type 1"]).count()["#"])
'''
Type 1
Bug          69
Dark         31
Dragon       32
Electric     44
Fairy        17
Fighting     27
...
Steel        27
Water       112
Name: #, dtype: int64
'''
#print(dataframecsv.groupby(["Type 1", "Type 2"]).count()["#"])
'''
Type 1    Type 2  
Bug       Electric     2
          Fighting     2
          Fire         2
          Flying      14
          Ghost        1
          Grass        6
          Ground       2
          Poison      12
          Rock         3
          Steel        7
          Water        1
Dark      Dragon       3
          Fighting     2
          Fire         3
          Flying       5
          Ghost        2
          Ice          2
          Psychic      2
          Steel        2
...
'''
getfiverows = pd.read_csv("pokemon_data.csv", chunksize=5)
print(getfiverows) #print <pandas.io.parsers.TextFileReader object at 0x7fe5cc8120f0>
for eachgetfiverows in getfiverows:
  print(eachgetfiverows)
  '''
       #                   Name Type 1  Type 2  HP  Attack  Defense  Sp. Atk  \
    0  1              Bulbasaur  Grass  Poison  45      49       49       65   
    1  2                Ivysaur  Grass  Poison  60      62       63       80   
    2  3               Venusaur  Grass  Poison  80      82       83      100   
    3  3  VenusaurMega Venusaur  Grass  Poison  80     100      123      122   
    4  4             Charmander   Fire     NaN  39      52       43       60   

       Sp. Def  Speed  Generation  Legendary  
    0       65     45           1      False  
    1       80     60           1      False  
    2      100     80           1      False  
    3      120     80           1      False  
    4       50     65           1      False  
       #                       Name Type 1  Type 2  HP  Attack  Defense  Sp. Atk  \
    5  5                 Charmeleon   Fire     NaN  58      64       58       80   
    6  6                  Charizard   Fire  Flying  78      84       78      109   
    7  6  CharizardMega Charizard X   Fire  Dragon  78     130      111      130   
    8  6  CharizardMega Charizard Y   Fire  Flying  78     104       78      159   
    9  7                   Squirtle  Water     NaN  44      48       65       50   

       Sp. Def  Speed  Generation  Legendary  
    5       65     80           1      False  
    6       85    100           1      False  
    7       85    100           1      False  
    8      115    100           1      False  
    9       64     43           1      False  
         #                     Name Type 1  Type 2  HP  Attack  Defense  Sp. Atk  \
    10   8                Wartortle  Water     NaN  59      63       80       65   
    11   9                Blastoise  Water     NaN  79      83      100       85   
    12   9  BlastoiseMega Blastoise  Water     NaN  79     103      120      135   
    13  10                 Caterpie    Bug     NaN  45      30       35       20   
    14  11                  Metapod    Bug     NaN  50      20       55       25   

        Sp. Def  Speed  Generation  Legendary  
    10       80     58           1      False  
    11      105     78           1      False  
    12      115     78           1      False  
    13       20     45           1      False  
    14       25     30           1      False  
    ...
    '''

#Python Pandas Tutorial -Part 1- Getting Started with Data Analysis - Installation and Loading Data
dataframedf = pd.read_csv("developer_survey_2019/survey_results_public.csv")
print(dataframedf)
'''
 Respondent                                         MainBranch Hobbyist  \
0               1             I am a student who is learning to code      Yes   
1               2             I am a student who is learning to code       No   
2               3  I am not primarily a developer, but I write co...      Yes   
3               4                     I am a developer by profession       No   
4               5                     I am a developer by profession      Yes   
5               6  I am not primarily a developer, but I write co...      Yes   
6               7                     I am a developer by profession       No   
...
'''
print(dataframedf.head(5)) #return number of rows starting from the top or first rows
'''
 Respondent                                         MainBranch Hobbyist  \
0           1             I am a student who is learning to code      Yes   
1           2             I am a student who is learning to code       No   
2           3  I am not primarily a developer, but I write co...      Yes   
3           4                     I am a developer by profession       No   
4           5                     I am a developer by profession      Yes   
'''
print(dataframedf.tail(5)) #return number of rows starting from the bottom or last rows
'''
  Respondent MainBranch Hobbyist  \
88878       88377        NaN      Yes   
88879       88601        NaN       No   
88880       88802        NaN       No   
88881       88816        NaN       No   
88882       88863        NaN      Yes   
'''
print(dataframedf.shape) #print (88883, 85) (columns, rows)
print(dataframedf.info())
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 88883 entries, 0 to 88882
Data columns (total 85 columns):
Respondent                88883 non-null int64
MainBranch                88331 non-null object
Hobbyist                  88883 non-null object
OpenSourcer               88883 non-null object
OpenSource                86842 non-null object
...
Age                       79210 non-null float64
Gender                    85406 non-null object
Trans                     83607 non-null object
Sexuality                 76147 non-null object
Ethnicity                 76668 non-null object
Dependents                83059 non-null object
SurveyLength              86984 non-null object
SurveyEase                87081 non-null object
dtypes: float64(5), int64(1), object(79)
memory usage: 57.6+ MB
None
'''
pd.set_option("display.max_columns", 85) #allows number of columns to display horizontally
readtheschema = pd.read_csv("developer_survey_2019/survey_results_schema.csv")
print(readtheschema)
'''
            Column                                       QuestionText
0       Respondent  Randomized respondent ID number (not in order ...
1       MainBranch  Which of the following options best describes ...
2         Hobbyist                            Do you code as a hobby?
3      OpenSourcer        How often do you contribute to open source?
4       OpenSource  How do you feel about the quality of open sour...
5       Employment  Which of the following best describes your cur...
6          Country          In which country do you currently reside?
'''
pd.set_option("display.max_columns", 1) #allows number of columns to display horizontally
pd.set_option("display.max_rows", 3) #allows number of rows to display horizontally
print(readtheschema)
'''
        Column     ...    
0   Respondent     ...    
..         ...     ...    
84  SurveyEase     ...    

[85 rows x 2 columns]
'''

#Python Pandas Tutorial -Part 2- DataFrame and Series Basics - Selecting Rows and Columns
peopledatafreamedictionary = {"firstcolumn1": ["Corey", "Jane", "John", "row1"], "lastcolumn2": ["Shafer", "Doe", "Doe", "row2"], "emailcolumn3": ["coreymschafer@gmail.com", "janedoe@email.com", "johndoe@email.com", "row3"]}
print(peopledatafreamedictionary) #print {'firstcolumn1': ['Corey', 'Jane', 'John', 'row1'], 'lastcolumn2': ['Shafer', 'Doe', 'Doe', 'row2'], 'emailcolumn3': ['coreymschafer@gmail.com', 'janedoe@email.com', 'johndoe@email.com', 'row3']}
print(peopledatafreamedictionary["emailcolumn3"]) #print ['coreymschafer@gmail.com', 'janedoe@email.com', 'johndoe@email.com', 'row3']
dataframeasdf = pd.DataFrame(peopledatafreamedictionary)
print(dataframeasdf)
'''
              emailcolumn3 firstcolumn1 lastcolumn2
0  coreymschafer@gmail.com        Corey      Shafer
1        janedoe@email.com         Jane         Doe
2        johndoe@email.com         John         Doe
3                     row3         row1        row2
'''
print(dataframeasdf["emailcolumn3"])
'''
0    coreymschafer@gmail.com
1          janedoe@email.com
2          johndoe@email.com
3                       row3
Name: emailcolumn3, dtype: object
'''
print(type(dataframeasdf["emailcolumn3"])) #print <class 'pandas.core.series.Series'>
print(dataframeasdf.emailcolumn3)
'''
0    coreymschafer@gmail.com
1          janedoe@email.com
2          johndoe@email.com
3                       row3
Name: emailcolumn3, dtype: object
'''
print(dataframeasdf[["lastcolumn2", "emailcolumn3"]])
'''
  lastcolumn2             emailcolumn3
0      Shafer  coreymschafer@gmail.com
1         Doe        janedoe@email.com
2         Doe        johndoe@email.com
3        row2                     row3
'''
print(type(dataframeasdf[["lastcolumn2", "emailcolumn3"]])) #print <class 'pandas.core.frame.DataFrame'>
print(dataframeasdf.columns) #print Index(['emailcolumn3', 'firstcolumn1', 'lastcolumn2'], dtype='object')
print(dataframeasdf.iloc[0])  #RM:  iloc is integer location
'''
emailcolumn3    coreymschafer@gmail.com
firstcolumn1                      Corey
lastcolumn2                      Shafer
Name: 0, dtype: object
'''
print(dataframeasdf.iloc[[0, 1]])  #RM:  iloc is integer location
'''
              emailcolumn3 firstcolumn1 lastcolumn2
0  coreymschafer@gmail.com        Corey      Shafer
1        janedoe@email.com         Jane         Doe
'''
print(dataframeasdf.iloc[[0, 1], [1, 2]])  #RM:  iloc is integer location
'''
  firstcolumn1 lastcolumn2
0        Corey      Shafer
1         Jane         Doe
'''
print(dataframeasdf.loc[0])  #RM:  loc is label location
'''
emailcolumn3    coreymschafer@gmail.com
firstcolumn1                      Corey
lastcolumn2                      Shafer
Name: 0, dtype: object
'''
print(dataframeasdf.loc[[0, 1]])  #RM:  loc is label location
'''
              emailcolumn3 firstcolumn1 lastcolumn2
0  coreymschafer@gmail.com        Corey      Shafer
1        janedoe@email.com         Jane         Doe
'''
#print(dataframeasdf.loc[[0, 1], [1, 2]]) #KeyError: 'None of [[1, 2]] are in the [columns]'
print(dataframeasdf.loc[[0, 1], ["firstcolumn1", "lastcolumn2"]])
'''
  firstcolumn1 lastcolumn2
0        Corey      Shafer
1         Jane         Doe
'''
dataframedf = pd.read_csv("developer_survey_2019/survey_results_public.csv")
readtheschema = pd.read_csv("developer_survey_2019/survey_results_schema.csv")
pd.set_option("display.max_columns", 85) #allows number of columns to display horizontally
pd.set_option("display.max_rows", 85) #allows number of rows to display horizontally
print(dataframedf.head())
'''
Respondent                                         MainBranch Hobbyist  \
0           1             I am a student who is learning to code      Yes
1           2             I am a student who is learning to code       No
2           3  I am not primarily a developer, but I write co...      Yes
3           4                     I am a developer by profession       No
4           5                     I am a developer by profession      Yes

                  OpenSourcer  \
0                       Never
1     Less than once per year
2                       Never
3                       Never
4  Once a month or more often

                                          OpenSource  \
0  The quality of OSS and closed source software ...
1  The quality of OSS and closed source software ...
2  The quality of OSS and closed source software ...
3  The quality of OSS and closed source software ...
4  OSS is, on average, of HIGHER quality than pro...
...
'''
print(readtheschema.head())
'''
 Column                                       QuestionText
0   Respondent  Randomized respondent ID number (not in order ...
1   MainBranch  Which of the following options best describes ...
2     Hobbyist                            Do you code as a hobby?
3  OpenSourcer        How often do you contribute to open source?
...
'''
print(dataframedf.shape) #print (88883, 85) (88883 rows, 85 columns)
print(dataframedf.columns) #print Index(['Respondent', 'MainBranch', 'Hobbyist', 'OpenSourcer', 'OpenSource','Employment', 'Country', 'Student', 'EdLevel', 'UndergradMajor', 'EduOther', 'OrgSize', 'DevType', 'YearsCode', 'Age1stCode', 'YearsCodePro', 'CareerSat', 'JobSat', 'MgrIdiot', 'MgrMoney', 'MgrWant', 'JobSeek', 'LastHireDate', 'LastInt', 'FizzBuzz', 'JobFactors', 'ResumeUpdate', 'CurrencySymbol', 'CurrencyDesc', 'CompTotal', 'CompFreq', 'ConvertedComp', 'WorkWeekHrs', 'WorkPlan', 'WorkChallenge', 'WorkRemote', 'WorkLoc', 'ImpSyn', 'CodeRev', 'CodeRevHrs', 'UnitTests', 'PurchaseHow', 'PurchaseWhat', 'LanguageWorkedWith', 'LanguageDesireNextYear', 'DatabaseWorkedWith', 'DatabaseDesireNextYear', 'PlatformWorkedWith', 'PlatformDesireNextYear', 'WebFrameWorkedWith', 'WebFrameDesireNextYear', 'MiscTechWorkedWith', 'MiscTechDesireNextYear', 'DevEnviron', 'OpSys', 'Containers', 'BlockchainOrg', 'BlockchainIs', 'BetterLife', 'ITperson', 'OffOn', 'SocialMedia', 'Extraversion', 'ScreenName', 'SOVisit1st', 'SOVisitFreq', 'SOVisitTo', 'SOFindAnswer', 'SOTimeSaved', 'SOHowMuchTime', 'SOAccount', 'SOPartFreq', 'SOJobs', 'EntTeams', 'SOComm', 'WelcomeChange', 'SONewContent', 'Age', 'Gender', 'Trans', 'Sexuality', 'Ethnicity', 'Dependents', 'SurveyLength', 'SurveyEase'], dtype='object')
print(dataframedf["Hobbyist"])
'''
0        Yes
1         No
2        Yes
3         No
4        Yes
...
88879     No
88880     No
88881     No
88882    Yes
Name: Hobbyist, Length: 88883, dtype: object
'''
print(dataframedf["Hobbyist"].value_counts())
'''
Yes    71257
No     17626
Name: Hobbyist, dtype: int64
'''
print(dataframedf.loc[0])
'''
Respondent                                                                1
MainBranch                           I am a student who is learning to code
Hobbyist                                                                Yes
OpenSourcer                                                           Never
OpenSource                The quality of OSS and closed source software ...
Employment                           Not employed, and not looking for work
Country                                                      United Kingdom
...
'''
print(dataframedf.loc[0, "Hobbyist"]) #print Yes
print(dataframedf.loc[[0, 1, 2], "Hobbyist"]) #Slicing is inclusive:inclusive
'''
0    Yes
1     No
2    Yes
Name: Hobbyist, dtype: object
'''
print(dataframedf.loc[0:2, "Hobbyist":"Employment"]) #Slicing is inclusive:inclusive
'''
  Hobbyist              OpenSourcer  \
0      Yes                    Never   
1       No  Less than once per year   
2      Yes                    Never   

                                          OpenSource  \
0  The quality of OSS and closed source software ...   
1  The quality of OSS and closed source software ...   
2  The quality of OSS and closed source software ...   

                               Employment  
0  Not employed, and not looking for work  
1      Not employed, but looking for work  
2                      Employed full-time  
'''

#Python Pandas Tutorial -Part 3- Indexes - How to Set- Reset- and Use Indexes
peopledatafreamedictionary = {"firstcolumn1": ["Corey", "Jane", "John", "row1"], "lastcolumn2": ["Shafer", "Doe", "Doe", "row2"], "emailcolumn3": ["coreymschafer@gmail.com", "janedoe@email.com", "johndoe@email.com", "row3"]}
print(peopledatafreamedictionary) #print {'firstcolumn1': ['Corey', 'Jane', 'John', 'row1'], 'lastcolumn2': ['Shafer', 'Doe', 'Doe', 'row2'], 'emailcolumn3': ['coreymschafer@gmail.com', 'janedoe@email.com', 'johndoe@email.com', 'row3']}
print(peopledatafreamedictionary["emailcolumn3"]) #print ['coreymschafer@gmail.com', 'janedoe@email.com', 'johndoe@email.com', 'row3']
dataframeasdf = pd.DataFrame(peopledatafreamedictionary)
print(dataframeasdf)
'''
              emailcolumn3 firstcolumn1 lastcolumn2
0  coreymschafer@gmail.com        Corey      Shafer
1        janedoe@email.com         Jane         Doe
2        johndoe@email.com         John         Doe
3                     row3         row1        row2
'''
print(dataframeasdf.index) #print RangeIndex(start=0, stop=4, step=1)  RM:  default index numbers
print(dataframeasdf["emailcolumn3"])
'''
0    coreymschafer@gmail.com
1          janedoe@email.com
2          johndoe@email.com
3                       row3
Name: emailcolumn3, dtype: object
'''
dataframeasdf.set_index("emailcolumn3")
print(dataframeasdf)
'''
              emailcolumn3 firstcolumn1 lastcolumn2
0  coreymschafer@gmail.com        Corey      Shafer
1        janedoe@email.com         Jane         Doe
2        johndoe@email.com         John         Doe
3                     row3         row1        row2
'''
dataframeasdf.set_index("emailcolumn3", inplace=True)
print(dataframeasdf)
'''
                        firstcolumn1 lastcolumn2
emailcolumn3
coreymschafer@gmail.com        Corey      Shafer
janedoe@email.com               Jane         Doe
johndoe@email.com               John         Doe
row3                            row1        row2
'''
print(dataframeasdf.index) #print Index(['coreymschafer@gmail.com', 'janedoe@email.com', 'johndoe@email.com', 'row3'], dtype='object', name='emailcolumn3')
print(dataframeasdf.loc["coreymschafer@gmail.com"])
'''
firstcolumn1     Corey
lastcolumn2     Shafer
Name: coreymschafer@gmail.com, dtype: object
'''
print(dataframeasdf.loc["coreymschafer@gmail.com", "lastcolumn2"]) #print Shafer
#print(dataframeasdf.loc[0]) #print TypeError: cannot do label indexing on <class 'pandas.core.indexes.base.Index'> with these indexers [0] of <class 'int'>
print(dataframeasdf.iloc[0])
'''
firstcolumn1     Corey
lastcolumn2     Shafer
Name: coreymschafer@gmail.com, dtype: object
'''
dataframeasdf.reset_index(inplace=True)
print(dataframeasdf)
'''
              emailcolumn3 firstcolumn1 lastcolumn2
0  coreymschafer@gmail.com        Corey      Shafer
1        janedoe@email.com         Jane         Doe
2        johndoe@email.com         John         Doe
3                     row3         row1        row2
'''
dataframedf = pd.read_csv("developer_survey_2019/survey_results_public.csv", index_col="Respondent")
readtheschema = pd.read_csv("developer_survey_2019/survey_results_schema.csv", index_col="Column")
pd.set_option("display.max_columns", 85) #allows number of columns to display horizontally
pd.set_option("display.max_rows", 85) #allows number of rows to display horizontally
print(dataframedf.head())
'''
MainBranch Hobbyist  \
Respondent                                                               
1                      I am a student who is learning to code      Yes   
2                      I am a student who is learning to code       No   
3           I am not primarily a developer, but I write co...      Yes   
4                              I am a developer by profession       No   
5                              I am a developer by profession      Yes   

                           OpenSourcer  \
Respondent                               
1                                Never   
2              Less than once per year   
3                                Never   
4                                Never   
5           Once a month or more often   

                                                   OpenSource  \
Respondent                                                      
1           The quality of OSS and closed source software ...   
2           The quality of OSS and closed source software ...   
3           The quality of OSS and closed source software ...   
4           The quality of OSS and closed source software ...   
5           OSS is, on average, of HIGHER quality than pro...   
...
'''
#dataframedf.set_index("Respondent") #RM:  an efficient way declare index at pd.read_csv()
print(dataframedf.loc[1])
'''
MainBranch                           I am a student who is learning to code
Hobbyist                                                                Yes
OpenSourcer                                                           Never
OpenSource                The quality of OSS and closed source software ...
...
'''
#readtheschema.set_index("Column") #RM:  an efficient way declare index at pd.read_csv()
print(readtheschema.head())
'''
 QuestionText
Column                                                        
Respondent   Randomized respondent ID number (not in order ...
MainBranch   Which of the following options best describes ...
Hobbyist                               Do you code as a hobby?
OpenSourcer        How often do you contribute to open source?
OpenSource   How do you feel about the quality of open sour...
'''
print(readtheschema.loc["Hobbyist"]) #print the Hobbyist row
'''
QuestionText    Do you code as a hobby?
Name: Hobbyist, dtype: object
#RM:  Column is the index.  Under Column column there is a Hobbyist row.  Under QuestionText column, the entry at Hobbyist row is Do you code as a hobby?
'''
print(readtheschema.loc["MgrIdiot"])
'''
QuestionText    How confident are you that your manager knows ...
Name: MgrIdiot, dtype: object
'''
print(readtheschema.loc["MgrIdiot", "QuestionText"]) #print How confident are you that your manager knows what they’re doing?  #RM:  print the data at row MgrIdiot and column QuestionText
print(readtheschema.sort_index(ascending=True, inplace=False)) #sort index column alphabetically
'''
QuestionText
Column                                                                   
Age                     What is your age (in years)? If you prefer not...
Age1stCode              At what age did you write your first line of c...
BetterLife              Do you think people born today will have a bet...
BlockchainIs            Blockchain / cryptocurrency technology is prim...
BlockchainOrg           How is your organization thinking about or imp...
CareerSat               Overall, how satisfied are you with your caree...
CodeRev                          Do you review code as part of your work?
...
'''

#Python Pandas Tutorial -Part 4- Filtering - Using Conditionals to Filter Rows and Columns
import pandas as pd
peopledatafreamedictionary = {"firstcolumn1": ["Corey", "Jane", "John", "row1"], "lastcolumn2": ["Schafer", "Doe", "Doe", "row2"], "emailcolumn3": ["coreymschafer@gmail.com", "janedoe@email.com", "johndoe@email.com", "row3"]}
dataframe = pd.DataFrame(peopledatafreamedictionary)
print(dataframe)
'''
              emailcolumn3 firstcolumn1 lastcolumn2
0  coreymschafer@gmail.com        Corey      Schafer
1        janedoe@email.com         Jane         Doe
2        johndoe@email.com         John         Doe
3                     row3         row1        row2
'''
print(dataframe["lastcolumn2"] == "Doe")
'''
0    False
1    True
2    True
3    False
Name: lastcolumn2, dtype: bool
'''
filterdoe = dataframe["lastcolumn2"] == "Doe"
print(dataframe[filterdoe])
'''
        emailcolumn3 firstcolumn1 lastcolumn2
1  janedoe@email.com         Jane         Doe
2  johndoe@email.com         John         Doe
'''
print(dataframe.loc[filterdoe])
'''
        emailcolumn3 firstcolumn1 lastcolumn2
1  janedoe@email.com         Jane         Doe
2  johndoe@email.com         John         Doe
'''
print(dataframe.loc[filterdoe, "emailcolumn3"])
'''
1    janedoe@email.com
2    johndoe@email.com
Name: emailcolumn3, dtype: object
'''
filterjohndoe = (dataframe["lastcolumn2"] == "Doe") & (dataframe["firstcolumn1"] == "John")
print(dataframe.loc[filterjohndoe])
'''
        emailcolumn3 firstcolumn1 lastcolumn2
2  johndoe@email.com         John         Doe
'''
print(dataframe.loc[filterjohndoe, "emailcolumn3"])
'''
2    johndoe@email.com
Name: emailcolumn3, dtype: object
'''
filterjohnschafer = (dataframe["lastcolumn2"] == "Schafer") | (dataframe["firstcolumn1"] == "John")
print(dataframe.loc[filterjohnschafer])
'''
              emailcolumn3 firstcolumn1 lastcolumn2
0  coreymschafer@gmail.com        Corey     Schafer
2        johndoe@email.com         John         Doe
'''
print(dataframe.loc[filterjohnschafer, "emailcolumn3"])
'''
0    coreymschafer@gmail.com
2          johndoe@email.com
Name: emailcolumn3, dtype: object
'''
#Use tilda ~ for not
filternotjohnschafer = (dataframe["lastcolumn2"] == "Schafer") | (dataframe["firstcolumn1"] == "John")
print(dataframe.loc[~filterjohnschafer, "emailcolumn3"])
'''
1    janedoe@email.com
3                 row3
Name: emailcolumn3, dtype: object
'''
dataframedf = pd.read_csv("developer_survey_2019/survey_results_public.csv", index_col="Respondent")
readtheschema = pd.read_csv("developer_survey_2019/survey_results_schema.csv", index_col="Column")
pd.set_option("display.max_columns", 85) #allows number of columns to display horizontally
pd.set_option("display.max_rows", 85) #allows number of rows to display horizontally
#print(dataframedf.head())
highsalary = dataframedf["ConvertedComp"] > 70000
print(dataframedf.loc[highsalary])
'''
 MainBranch Hobbyist  \
Respondent                                                               
6           I am not primarily a developer, but I write co...      Yes   
9                              I am a developer by profession      Yes   
13                             I am a developer by profession      Yes   
16                             I am a developer by profession      Yes   
22                             I am a developer by profession      Yes   
26                             I am a developer by profession      Yes   
29                             I am a developer by profession      Yes   
...
'''
print(dataframedf.loc[highsalary, ["Country", "LanguageWorkedWith", "ConvertedComp"]])
'''
                 Country                                 LanguageWorkedWith  \
Respondent                                                                      
6                   Canada                                         Java;R;SQL   
9              New Zealand  Bash/Shell/PowerShell;C#;HTML/CSS;JavaScript;P...   
13           United States  Bash/Shell/PowerShell;HTML/CSS;JavaScript;PHP;...   
16          United Kingdom  Bash/Shell/PowerShell;C#;HTML/CSS;JavaScript;T...   
22           United States  Bash/Shell/PowerShell;C++;HTML/CSS;JavaScript;...   
26           United States  Bash/Shell/PowerShell;C++;C#;HTML/CSS;JavaScri...   
29           United States               Bash/Shell/PowerShell;JavaScript;SQL 
...
'''
topcountries = ["United States", "India", "United Kingdom", "Germany", "Canada"]
topcountriesfilter = dataframedf["Country"].isin(topcountries)
print(dataframedf.loc[topcountriesfilter, ["Country", "LanguageWorkedWith"]])
'''
  Country                                 LanguageWorkedWith
Respondent                                                                   
1           United Kingdom                    HTML/CSS;Java;JavaScript;Python
4            United States                                C;C++;C#;Python;SQL
6                   Canada                                         Java;R;SQL
8                    India  Bash/Shell/PowerShell;C;C++;HTML/CSS;Java;Java...
10                   India                      C#;Go;JavaScript;Python;R;SQL
12                  Canada   Bash/Shell/PowerShell;HTML/CSS;Java;Python;R;SQL
13           United States  Bash/Shell/PowerShell;HTML/CSS;JavaScript;PHP;...
14                 Germany                                                C++
...
'''
pythonlanguage = dataframedf["LanguageWorkedWith"].str.contains("Python", na=False) #nulls are excluded
print(dataframedf.loc[pythonlanguage, ["LanguageWorkedWith", "ConvertedComp"]])
'''
  LanguageWorkedWith  ConvertedComp
Respondent                                                                  
1                             HTML/CSS;Java;JavaScript;Python            NaN
2                                         C++;HTML/CSS;Python            NaN
4                                         C;C++;C#;Python;SQL        61000.0
5                 C++;HTML/CSS;Java;JavaScript;Python;SQL;VBA            NaN
8           Bash/Shell/PowerShell;C;C++;HTML/CSS;Java;Java...            NaN
9           Bash/Shell/PowerShell;C#;HTML/CSS;JavaScript;P...        95179.0
...
'''

#Python Pandas Tutorial -Part 5- Updating Rows and Columns - Modifying Data Within DataFrames
import pandas as pd
peopledatafreamedictionary = {"firstcolumn1": ["Corey", "Jane", "John", "row1"], "lastcolumn2": ["Schafer", "Doe", "Doe", "row2"], "emailcolumn3": ["coreymschafer@gmail.com", "janedoe@email.com", "johndoe@email.com", "row3"]}
dataframe = pd.DataFrame(peopledatafreamedictionary)
print(dataframe)
'''
              emailcolumn3 firstcolumn1 lastcolumn2
0  coreymschafer@gmail.com        Corey     Schafer
1        janedoe@email.com         Jane         Doe
2        johndoe@email.com         John         Doe
3                     row3         row1        row2
'''
print(dataframe.columns) #print Index(['emailcolumn3', 'firstcolumn1', 'lastcolumn2'], dtype='object')
print(type(dataframe.columns)) #print <class 'pandas.core.indexes.base.Index'>
dataframe.columns = ["email", "firstname", "lastname"]
print(dataframe)
'''
                     email firstname lastname
0  coreymschafer@gmail.com    Corey  Schafer
1        janedoe@email.com     Jane      Doe
2        johndoe@email.com     John      Doe
3                     row3     row1     row2
'''
dataframe.columns = [x.upper() for x in dataframe.columns]
print(dataframe)
'''
                     EMAIL FIRSTNAME LASTNAME
0  coreymschafer@gmail.com     Corey  Schafer
1        janedoe@email.com      Jane      Doe
2        johndoe@email.com      John      Doe
3                     row3      row1     row2
'''
dataframe.columns = dataframe.columns.str.replace(" ", "_") #Replace spaces with underscores
peopledatafreamedictionary = {"firstcolumn1": ["Corey", "Jane", "John", "row1"], "lastcolumn2": ["Schafer", "Doe", "Doe", "row2"], "emailcolumn3": ["coreymschafer@gmail.com", "janedoe@email.com", "johndoe@email.com", "row3"]}
dataframe = pd.DataFrame(peopledatafreamedictionary)
print(dataframe)
'''
              emailcolumn3 firstcolumn1 lastcolumn2
0  coreymschafer@gmail.com        Corey     Schafer
1        janedoe@email.com         Jane         Doe
2        johndoe@email.com         John         Doe
3                     row3         row1        row2
'''
dataframe.rename(columns={"firstcolumn1": "newcolumnnamefirst", "lastcolumn2": "newcolumnnamelast"}, inplace=True) #RM:  No need to asssign to a variable.  Immediate update because of inplace?
print(dataframe)
'''
              emailcolumn3 newcolumnnamefirst newcolumnnamelast
0  coreymschafer@gmail.com              Corey           Schafer
1        janedoe@email.com               Jane               Doe
2        johndoe@email.com               John               Doe
3                     row3               row1              row2
'''
print(dataframe.loc[2])
'''
emailcolumn3          johndoe@email.com
newcolumnnamefirst                 John
newcolumnnamelast                   Doe
Name: 2, dtype: object
'''
dataframe.loc[2] = ["johnsmith@email.com", "John", "Smith"]
print(dataframe)
'''
              emailcolumn3 newcolumnnamefirst newcolumnnamelast
0  coreymschafer@gmail.com              Corey           Schafer
1        janedoe@email.com               Jane               Doe
2      johnsmith@email.com               John             Smith
3                     row3               row1              row2
'''
print(dataframe.loc[2, ["newcolumnnamelast", "emailcolumn3"]])
'''
newcolumnnamelast                  Smith
emailcolumn3         johnsmith@email.com
Name: 2, dtype: object
'''
dataframe.loc[2, ["newcolumnnamelast", "emailcolumn3"]] = ["Doe", "johndoe@email.com"]
print(dataframe)
'''
              emailcolumn3 newcolumnnamefirst newcolumnnamelast
0  coreymschafer@gmail.com              Corey           Schafer
1        janedoe@email.com               Jane               Doe
2        johndoe@email.com               John               Doe
3                     row3               row1              row2
'''
dataframe.loc[2, "newcolumnnamelast"] = "Smith"
print(dataframe)
'''
              emailcolumn3 newcolumnnamefirst newcolumnnamelast
0  coreymschafer@gmail.com              Corey           Schafer
1        janedoe@email.com               Jane               Doe
2        johndoe@email.com               John             Smith
3                     row3               row1              row2
'''
dataframe.at[2, "newcolumnnamelast"] = "Doe"
print(dataframe)
'''
              emailcolumn3 newcolumnnamefirst newcolumnnamelast
0  coreymschafer@gmail.com              Corey           Schafer
1        janedoe@email.com               Jane               Doe
2        johndoe@email.com               John               Doe
3                     row3               row1              row2
'''
filteremailjohndoe = (dataframe["emailcolumn3"] == "johndoe@email.com")
dataframe.loc[filteremailjohndoe, "newcolumnnamelast"] = "Smith"
print(dataframe)
'''
              emailcolumn3 newcolumnnamefirst newcolumnnamelast
0  coreymschafer@gmail.com              Corey           Schafer
1        janedoe@email.com               Jane               Doe
2        johndoe@email.com               John             Smith
3                     row3               row1              row2
'''
dataframe["emailcolumn3"] = dataframe["emailcolumn3"].str.upper()
print(dataframe)
'''
              emailcolumn3 newcolumnnamefirst newcolumnnamelast
0  COREYMSCHAFER@GMAIL.COM              Corey           Schafer
1        JANEDOE@EMAIL.COM               Jane               Doe
2        JOHNDOE@EMAIL.COM               John             Smith
3                     ROW3               row1              row2
'''
#apply, map, applymap, replace
print(dataframe["emailcolumn3"].apply(len))
'''
0    23
1    17
2    17
3     4
Name: emailcolumn3, dtype: int64
'''
def updatemail(email):
  return email.lower()


dataframe["emailcolumn3"] = dataframe["emailcolumn3"].apply(updatemail)
#dataframe["emailcolumn3"] = dataframe["emailcolumn3"].apply(lambda x: x.lower())
print(dataframe)
'''
              emailcolumn3 newcolumnnamefirst newcolumnnamelast
0  coreymschafer@gmail.com              Corey           Schafer
1        janedoe@email.com               Jane               Doe
2        johndoe@email.com               John             Smith
3                     row3               row1              row2
'''
print(dataframe.apply(len))
'''
emailcolumn3          4
newcolumnnamefirst    4
newcolumnnamelast     4
dtype: int64
'''
print(len(dataframe["emailcolumn3"])) #print 4
print(dataframe.apply(len, axis="columns"))
'''
0    3
1    3
2    3
3    3
dtype: int64
'''
print(dataframe.apply(pd.Series.min))
#print(dataframe.apply(lambda ascendingfirstvalue: ascendingfirstvalue.min()))
'''
emailcolumn3          coreymschafer@gmail.com
newcolumnnamefirst                      Corey
newcolumnnamelast                         Doe
dtype: object
'''
print(dataframe.applymap(len))
'''
   emailcolumn3  newcolumnnamefirst  newcolumnnamelast
0            23                   5                  7
1            17                   4                  3
2            17                   4                  5
3             4                   4                  4
'''
print(dataframe.applymap(str.upper))
#print(dataframe.applymap(lambda x: x.upper()))
'''
              emailcolumn3 newcolumnnamefirst newcolumnnamelast
0  COREYMSCHAFER@GMAIL.COM              COREY           SCHAFER
1        JANEDOE@EMAIL.COM               JANE               DOE
2        JOHNDOE@EMAIL.COM               JOHN             SMITH
3                     ROW3               ROW1              ROW2
'''
#RM:  The previous exercises I used print statements.  The print statements are not permanent changes.  Must assign to dataframe variable.
firstnamemap = dataframe["newcolumnnamefirst"].map({"Corey": "Chris", "Jane": "Mary"})
print(firstnamemap)
'''
0    Chris
1     Mary
2      NaN
3      NaN
Name: newcolumnnamefirst, dtype: object
'''
print(dataframe)
'''
              emailcolumn3 newcolumnnamefirst newcolumnnamelast
0  coreymschafer@gmail.com              Corey           Schafer
1        janedoe@email.com               Jane               Doe
2        johndoe@email.com               John             Smith
3                     row3               row1              row2
'''
firstnamereplace = dataframe["newcolumnnamefirst"].replace({"Corey": "Chris", "Jane": "Mary"})
print(firstnamereplace)
'''
0    Chris
1     Mary
2     John
3     row1
Name: newcolumnnamefirst, dtype: object
'''
print(dataframe)
'''
              emailcolumn3 newcolumnnamefirst newcolumnnamelast
0  coreymschafer@gmail.com              Corey           Schafer
1        janedoe@email.com               Jane               Doe
2        johndoe@email.com               John             Smith
3                     row3               row1              row2
'''
dataframe["newcolumnnamefirst"] = dataframe["newcolumnnamefirst"].replace({"Corey": "Chris", "Jane": "Mary"})
print(dataframe)
'''
              emailcolumn3 newcolumnnamefirst newcolumnnamelast
0  coreymschafer@gmail.com              Chris           Schafer
1        janedoe@email.com               Mary               Doe
2        johndoe@email.com               John             Smith
3                     row3               row1              row2
'''

dataframedf = pd.read_csv("developer_survey_2019/survey_results_public.csv", index_col="Respondent")
readtheschema = pd.read_csv("developer_survey_2019/survey_results_schema.csv", index_col="Column")
pd.set_option("display.max_columns", 85) #allows number of columns to display horizontally
pd.set_option("display.max_rows", 85) #allows number of rows to display horizontally
#print(dataframedf.head())
dataframedf.rename(columns={"ConvertedComp": "SalaryUSD"}, inplace=True)  #RM:  No need to asssign to a variable.  Immediate update because of inplace?
print(dataframedf["SalaryUSD"])
'''
Respondent
1              NaN
2              NaN
3           8820.0
4          61000.0
5              NaN
6         366420.0
7              NaN
8              NaN
9          95179.0
10         13293.0
'''
dataframedf["Hobbyist"].map({"Yes": True, "No": False})
print(dataframedf["Hobbyist"])
'''
Respondent
1        Yes
2         No
3        Yes
4         No
5        Yes
6        Yes
7         No
8        Yes
9        Yes
10       Yes
'''
dataframedf["Hobbyist"] = dataframedf["Hobbyist"].map({"Yes": True, "No": False})
print(dataframedf["Hobbyist"])
'''
Respondent
1         True
2        False
3         True
4        False
5         True
6         True
7        False
8         True
9         True
10        True
'''
dataframedf["Hobbyist"] = dataframedf["Hobbyist"].replace({True: "Yes", False: "No"})
print(dataframedf["Hobbyist"])
'''
Respondent
1        Yes
2         No
3        Yes
4         No
5        Yes
6        Yes
7         No
8        Yes
9        Yes
10       Yes
'''

#Python Pandas Tutorial -Part 6- AddRemove Rows and Columns From DataFrames
import pandas as pd
peopledirtylist = {"first": ["Corey", "Jane", "John"], "last": ["Schafer", "Doe", "Doe"], "email": ["coreymschafer@gmail.com", "janedoe@email.com", "johndoe@email.com"]}
peopledirtylistdataframe = pd.DataFrame(peopledirtylist)
print(peopledirtylistdataframe)
'''
                     email  first     last
0  coreymschafer@gmail.com  Corey  Schafer
1        janedoe@email.com   Jane      Doe
2        johndoe@email.com   John      Doe
'''
print(peopledirtylistdataframe["first"] + " " + peopledirtylistdataframe["last"])
'''
0    Corey Schafer
1         Jane Doe
2         John Doe
dtype: object
'''
peopledirtylistdataframe["combinecolumnsfirstlast"] = peopledirtylistdataframe["first"] + " " + peopledirtylistdataframe["last"]
print(peopledirtylistdataframe)
'''
                     email  first     last combinecolumnsfirstlast
0  coreymschafer@gmail.com  Corey  Schafer           Corey Schafer
1        janedoe@email.com   Jane      Doe                Jane Doe
2        johndoe@email.com   John      Doe                John Doe
'''
peopledirtylistdataframedeletecolumns = peopledirtylistdataframe.drop(columns=["first", "last"], inplace=False)
print(peopledirtylistdataframedeletecolumns)
'''
                     email combinecolumnsfirstlast
0  coreymschafer@gmail.com           Corey Schafer
1        janedoe@email.com                Jane Doe
2        johndoe@email.com                John Doe
'''
splitcolumn = peopledirtylistdataframedeletecolumns["combinecolumnsfirstlast"].str.split(" ", expand=False)
print(splitcolumn)
'''
0    [Corey, Schafer]
1         [Jane, Doe]
2         [John, Doe]
Name: combinecolumnsfirstlast, dtype: object
'''
splitcolumn = peopledirtylistdataframedeletecolumns["combinecolumnsfirstlast"].str.split(" ", expand=True)
print(splitcolumn)
'''
       0        1
0  Corey  Schafer
1   Jane      Doe
2   John      Doe
'''
peopledirtylistdataframedeletecolumns[["splitcolumnheader1", "splitcolumnheader2"]] = peopledirtylistdataframedeletecolumns["combinecolumnsfirstlast"].str.split(" ", expand=True)
print(peopledirtylistdataframedeletecolumns)
'''
                     email combinecolumnsfirstlast splitcolumnheader1  \
0  coreymschafer@gmail.com           Corey Schafer              Corey   
1        janedoe@email.com                Jane Doe               Jane   
2        johndoe@email.com                John Doe               John   

  splitcolumnheader2  
0            Schafer  
1                Doe  
2                Doe
'''
peopledirtylistdataframeaddrow = peopledirtylistdataframedeletecolumns.append({"splitcolumnheader1": "Tony"}, ignore_index=True)
print(peopledirtylistdataframeaddrow)
'''
                     email combinecolumnsfirstlast splitcolumnheader1  \
0  coreymschafer@gmail.com           Corey Schafer              Corey   
1        janedoe@email.com                Jane Doe               Jane   
2        johndoe@email.com                John Doe               John   
3                      NaN                     NaN               Tony   

  splitcolumnheader2  
0            Schafer  
1                Doe  
2                Doe  
'''
avergerslist = {"first": ["Tony", "Steve", "Bruce"], "last": ["Stark", "Rogers", "Banner"], "email": ["ironman@avenge.com", "cap@avenge.com", "hulk@avenge.com"]}
avengersdataframe = pd.DataFrame(avergerslist)
print(avengersdataframe)
'''
                email  first    last
0  ironman@avenge.com   Tony   Stark
1      cap@avenge.com  Steve  Rogers
2     hulk@avenge.com  Bruce  Banner
'''
combineddataframes = peopledirtylistdataframe.append(avengersdataframe, ignore_index=True)
print(combineddataframes)
'''
  combinecolumnsfirstlast                    email  first     last
0           Corey Schafer  coreymschafer@gmail.com  Corey  Schafer
1                Jane Doe        janedoe@email.com   Jane      Doe
2                John Doe        johndoe@email.com   John      Doe
3                     NaN       ironman@avenge.com   Tony    Stark
4                     NaN           cap@avenge.com  Steve   Rogers
5                     NaN          hulk@avenge.com  Bruce   Banner
'''
dropsteverogers = combineddataframes.drop(index=4)
print(dropsteverogers)
'''
  combinecolumnsfirstlast                    email  first     last
0           Corey Schafer  coreymschafer@gmail.com  Corey  Schafer
1                Jane Doe        janedoe@email.com   Jane      Doe
2                John Doe        johndoe@email.com   John      Doe
3                     NaN       ironman@avenge.com   Tony    Stark
5                     NaN          hulk@avenge.com  Bruce   Banner
'''
dropdoes = dropsteverogers.drop(index=dropsteverogers[dropsteverogers["last"] == "Doe"].index)
print(dropdoes)
'''
  combinecolumnsfirstlast                    email  first     last
0           Corey Schafer  coreymschafer@gmail.com  Corey  Schafer
3                     NaN       ironman@avenge.com   Tony    Stark
5                     NaN          hulk@avenge.com  Bruce   Banner
'''
#or
dropdoesvariable = dropsteverogers["last"] == "Doe"
dropdoes = dropsteverogers.drop(index=dropsteverogers[dropdoesvariable].index)
print(dropdoes)

'''
  combinecolumnsfirstlast                    email  first     last
0           Corey Schafer  coreymschafer@gmail.com  Corey  Schafer
3                     NaN       ironman@avenge.com   Tony    Stark
5                     NaN          hulk@avenge.com  Bruce   Banner
'''

#Python Pandas Tutorial -Part 7- Sorting Data
peopledatafreamedictionary = {"firstcolumn1": ["Corey", "Jane", "John", "row1", "Adam"], "lastcolumn2": ["Shafer", "Doe", "Doe", "row2", "Doe"], "emailcolumn3": ["coreymschafer@gmail.com", "janedoe@email.com", "johndoe@email.com", "row3", "a@email.com"]}
dataframe = pd.DataFrame(peopledatafreamedictionary)
print(dataframe)
'''
              emailcolumn3 firstcolumn1 lastcolumn2
0  coreymschafer@gmail.com        Corey      Shafer
1        janedoe@email.com         Jane         Doe
2        johndoe@email.com         John         Doe
3                     row3         row1        row2
4              a@email.com         Adam         Doe
'''
sortlastcolumn = dataframe.sort_values(by="lastcolumn2", ascending=True)
print(sortlastcolumn)
'''
              emailcolumn3 firstcolumn1 lastcolumn2
1        janedoe@email.com         Jane         Doe
2        johndoe@email.com         John         Doe
4              a@email.com         Adam         Doe
0  coreymschafer@gmail.com        Corey      Shafer
3                     row3         row1        row2
'''
sortlastfirstcolumn = dataframe.sort_values(by=["lastcolumn2", "firstcolumn1"], ascending=True)
print(sortlastfirstcolumn)
'''
              emailcolumn3 firstcolumn1 lastcolumn2
4              a@email.com         Adam         Doe
1        janedoe@email.com         Jane         Doe
2        johndoe@email.com         John         Doe
0  coreymschafer@gmail.com        Corey      Shafer
3                     row3         row1        row2
'''
sortlastfirstcolumn = dataframe.sort_values(by=["lastcolumn2", "firstcolumn1"], ascending=[False, True])
print(sortlastfirstcolumn)
'''
              emailcolumn3 firstcolumn1 lastcolumn2
3                     row3         row1        row2
0  coreymschafer@gmail.com        Corey      Shafer
4              a@email.com         Adam         Doe
1        janedoe@email.com         Jane         Doe
2        johndoe@email.com         John         Doe
'''
sortlastfirstcolumninplace = dataframe.sort_values(by=["lastcolumn2", "firstcolumn1"], ascending=[False, True], inplace=True)
print(sortlastfirstcolumninplace) #print None
print(sortlastfirstcolumn.sort_index()) #Sort the data by index number
'''
              emailcolumn3 firstcolumn1 lastcolumn2
0  coreymschafer@gmail.com        Corey      Shafer
1        janedoe@email.com         Jane         Doe
2        johndoe@email.com         John         Doe
3                     row3         row1        row2
4              a@email.com         Adam         Doe
'''
displaylastnamecolumn = dataframe["lastcolumn2"].sort_values()
print(displaylastnamecolumn)
'''
4       Doe
1       Doe
2       Doe
0    Shafer
3      row2
Name: lastcolumn2, dtype: object
'''
dataframedf = pd.read_csv("developer_survey_2019/survey_results_public.csv")
readtheschema = pd.read_csv("developer_survey_2019/survey_results_schema.csv")
pd.set_option("display.max_columns", 85) #allows number of columns to display horizontally
pd.set_option("display.max_rows", 85) #allows number of rows to display horizontally
#print(dataframedf.head())
dataframedf.sort_values(by=["Country"], inplace=True)
print(dataframedf["Country"].head(50))
'''
39018    Afghanistan
62723    Afghanistan
85185    Afghanistan
...
41344        Albania
33177        Albania
6688         Albania
Name: Country, dtype: object
'''
dataframedf.sort_values(by=["Country", "ConvertedComp"], inplace=True)
print(dataframedf[["Country", "ConvertedComp"]].head(50))
'''
          Country  ConvertedComp
28470  Afghanistan            0.0
719    Afghanistan            0.0
29560  Afghanistan         1116.0
8112   Afghanistan         1596.0
10697  Afghanistan         3996.0
48122  Afghanistan         4464.0
22327  Afghanistan         7980.0
7056   Afghanistan        14364.0
58082  Afghanistan        17556.0
39018  Afghanistan        19152.0
50172  Afghanistan       153216.0
62723  Afghanistan      1000000.0
85185  Afghanistan            NaN
50437  Afghanistan            NaN
...
25440      Albania         4416.0
78326      Albania         4968.0
33999      Albania         5496.0
'''
dataframedf.sort_values(by=["Country", "ConvertedComp"], ascending=[True, False], inplace=True)
print(dataframedf[["Country", "ConvertedComp"]].head(50))
'''
 Country  ConvertedComp
62723  Afghanistan      1000000.0
50172  Afghanistan       153216.0
39018  Afghanistan        19152.0
58082  Afghanistan        17556.0
7056   Afghanistan        14364.0
22327  Afghanistan         7980.0
48122  Afghanistan         4464.0
10697  Afghanistan         3996.0
8112   Afghanistan         1596.0
29560  Afghanistan         1116.0
28470  Afghanistan            0.0
719    Afghanistan            0.0
85185  Afghanistan            NaN
...
38075      Albania       187668.0
3771       Albania       114550.0
9230       Albania        74474.0
6688       Albania        60000.0
10257      Albania        57300.0
65859      Albania        41244.0
'''
toptensalaries = dataframedf["ConvertedComp"].nlargest(10)
print(toptensalaries)
'''
25833    2000000.0
87353    2000000.0
21895    2000000.0
28080    2000000.0
72274    2000000.0
77665    2000000.0
79701    2000000.0
51798    2000000.0
75088    2000000.0
32056    2000000.0
Name: ConvertedComp, dtype: float64
'''
toptensalariesallcolumns = dataframedf.nlargest(10, "ConvertedComp") #use nsmallest for the bottom ten salaries
print(toptensalariesallcolumns)
'''
 Respondent                                         MainBranch Hobbyist  \
25833       25983                     I am a developer by profession      Yes   
87353       87896                     I am a developer by profession      Yes   
21895       22013                     I am a developer by profession      Yes   
28080       28243                     I am a developer by profession      Yes   
72274       72732  I am not primarily a developer, but I write co...       No   
77665       78151                     I am a developer by profession      Yes   
79701       80200                     I am a developer by profession      Yes   
51798       52132                     I am a developer by profession      Yes   
75088       75561                     I am a developer by profession      Yes   
32056       32250                     I am a developer by profession      Yes   
'''

#Python Pandas Tutorial -Part 8- Grouping and Aggregating - Analyzing and Exploring Your Data
import pandas as pd

dataframedf = pd.read_csv("developer_survey_2019/survey_results_public.csv")
readtheschema = pd.read_csv("developer_survey_2019/survey_results_schema.csv")
# pd.set_option("display.max_columns", 85) #allows number of columns to display horizontally
# pd.set_option("display.max_rows", 85) #allows number of rows to display horizontally
# print(dataframedf.head())

#ConvertedComp is salary
print(dataframedf["ConvertedComp"].head(15)) #print the first 15 ConvertedComp salary or data points
print(dataframedf["ConvertedComp"].median()) #print 57287.0.  Ignores NaN values.
print(dataframedf.median()) #print all column headers which can calculate a median value
'''
Respondent       44442.0
CompTotal        62000.0
ConvertedComp    57287.0
WorkWeekHrs         40.0
CodeRevHrs           4.0
Age                 29.0
dtype: float64
'''
print(dataframedf.describe()) #RM:  instructor says a positive e for exponent means move the decimal right a number space.  Count counts non NaN rows.
'''
         Respondent     CompTotal  ConvertedComp   WorkWeekHrs    CodeRevHrs  \
count  88883.000000  5.594500e+04   5.582300e+04  64503.000000  49790.000000   
mean   44442.000000  5.519014e+11   1.271107e+05     42.127197      5.084308   
std    25658.456325  7.331926e+13   2.841523e+05     37.287610      5.513931   
min        1.000000  0.000000e+00   0.000000e+00      1.000000      0.000000   
25%    22221.500000  2.000000e+04   2.577750e+04     40.000000      2.000000   
50%    44442.000000  6.200000e+04   5.728700e+04     40.000000      4.000000   
75%    66662.500000  1.200000e+05   1.000000e+05     44.750000      6.000000   
max    88883.000000  1.000000e+16   2.000000e+06   4850.000000     99.000000   

                Age  
count  79210.000000  
mean      30.336699  
std        9.178390  
min        1.000000  
25%       24.000000  
50%       29.000000  
75%       35.000000  
max       99.000000  
'''
print(dataframedf["ConvertedComp"].count()) #print 55823
print(dataframedf["Hobbyist"].value_counts())
'''
Yes    71257
No     17626
Name: Hobbyist, dtype: int64
'''
print(dataframedf["SocialMedia"].value_counts())
'''
Reddit                      14374
YouTube                     13830
WhatsApp                    13347
Facebook                    13178
Twitter                     11398
Instagram                    6261
I don't use social media     5554
LinkedIn                     4501
WeChat 微信                     667
Snapchat                      628
VK ВКонта́кте                 603
Weibo 新浪微博                     56
Youku Tudou 优酷                 21
Hello                          19
Name: SocialMedia, dtype: int64
'''
print(dataframedf["SocialMedia"].value_counts(normalize=True))  #RM:  Show values as a percentage of total
'''
Reddit                      0.170233
YouTube                     0.163791
WhatsApp                    0.158071
Facebook                    0.156069
Twitter                     0.134988
Instagram                   0.074150
I don't use social media    0.065777
LinkedIn                    0.053306
WeChat 微信                   0.007899
Snapchat                    0.007437
VK ВКонта́кте               0.007141
Weibo 新浪微博                  0.000663
Youku Tudou 优酷              0.000249
Hello                       0.000225
Name: SocialMedia, dtype: float64
'''
print(dataframedf["Country"].value_counts())
'''
United States                            20949
India                                     9061
Germany                                   5866
United Kingdom                            5737
Canada                                    3395
France                                    2391
Brazil                                    1948
Poland                                    1922
Australia                                 1903
...
Dominica                                     1
Chad                                         1
Tonga                                        1
Name: Country, Length: 179, dtype: int64
'''
#group dataframedf["Country"].value_counts() by country
print(dataframedf.groupby(["Country"])) #print <pandas.core.groupby.DataFrameGroupBy object at 0x7f32a9ed3d68>
countrygroup = dataframedf.groupby(["Country"])
print(countrygroup.get_group("United States")) #print rows where Country is United States
'''
  Respondent                                         MainBranch Hobbyist  \
3               4                     I am a developer by profession       No   
12             13                     I am a developer by profession      Yes   
21             22                     I am a developer by profession      Yes   
22             23                     I am a developer by profession      Yes   
...
'''
filtercountry = dataframedf["Country"] == "United States"
print(dataframedf.loc[filtercountry])
'''
  Respondent                                         MainBranch Hobbyist  \
3               4                     I am a developer by profession       No   
12             13                     I am a developer by profession      Yes   
21             22                     I am a developer by profession      Yes   
22             23                     I am a developer by profession      Yes   
...
'''
print(dataframedf.loc[filtercountry]["SocialMedia"].value_counts()) #print Social Media counts in United States from filtercountry variable
'''
Reddit                      5700
Twitter                     3468
Facebook                    2844
YouTube                     2463
I don't use social media    1851
Instagram                   1652
LinkedIn                    1020
WhatsApp                     609
Snapchat                     326
WeChat 微信                     93
VK ВКонта́кте                  9
Weibo 新浪微博                     8
Hello                          2
Youku Tudou 优酷                 1
Name: SocialMedia, dtype: int64
'''
print(countrygroup["SocialMedia"].value_counts()) #print Social Media column counts by Country from countrygroup variable
'''
Country                               SocialMedia             
Afghanistan                           Facebook                     15
                                      YouTube                       9
                                      I don't use social media      6
                                      WhatsApp                      4
                                      Instagram                     1
                                      LinkedIn                      1
                                      Twitter                       1
                                                                 ... 
Zimbabwe                              WhatsApp                     20
                                      Twitter                       8
                                      Facebook                      3
                                      YouTube                       3
                                      Instagram                     2
                                      LinkedIn                      2
                                      Reddit                        1
Name: SocialMedia, Length: 1220, dtype: int64
'''
print(countrygroup["SocialMedia"].value_counts().head(21)) #print first 21 rows Social Media column counts by Country from countrygroup variable
'''
Country      SocialMedia             
Afghanistan  Facebook                    15
             YouTube                      9
             I don't use social media     6
             WhatsApp                     4
             Instagram                    1
             LinkedIn                     1
             Twitter                      1
Albania      WhatsApp                    18
             Facebook                    16
             Instagram                   13
             YouTube                     10
             Twitter                      8
             LinkedIn                     7
             Reddit                       6
             I don't use social media     4
             Snapchat                     1
             WeChat 微信                    1
Algeria      YouTube                     42
             Facebook                    41
             Twitter                     14
             LinkedIn                     9
Name: SocialMedia, dtype: int64
'''
print(countrygroup["SocialMedia"].value_counts().loc["United States"]) #print Social Media column counts United States
'''
SocialMedia
Reddit                      5700
Twitter                     3468
Facebook                    2844
YouTube                     2463
I don't use social media    1851
Instagram                   1652
LinkedIn                    1020
WhatsApp                     609
Snapchat                     326
WeChat 微信                     93
VK ВКонта́кте                  9
Weibo 新浪微博                     8
Hello                          2
Youku Tudou 优酷                 1
Name: SocialMedia, dtype: int64
'''
print(countrygroup["SocialMedia"].value_counts(normalize=True).loc["United States"]) #print Social Media column percentages United States
'''
SocialMedia
Reddit                      0.284346
Twitter                     0.173002
Facebook                    0.141874
YouTube                     0.122867
I don't use social media    0.092338
Instagram                   0.082410
LinkedIn                    0.050883
WhatsApp                    0.030380
Snapchat                    0.016263
WeChat 微信                   0.004639
VK ВКонта́кте               0.000449
Weibo 新浪微博                  0.000399
Hello                       0.000100
Youku Tudou 优酷              0.000050
Name: SocialMedia, dtype: float64
'''
print(countrygroup["ConvertedComp"].median()) #print median salary by countrygroup variable defined countrygroup = dataframedf.groupby(["Country"])
'''
Country
Afghanistan                                    6222.0
Albania                                       10818.0
Algeria                                        7878.0
                                               ...   
Yemen                                         11940.0
Zambia                                         5040.0
Zimbabwe                                      19200.0
Name: ConvertedComp, Length: 179, dtype: float64
'''
print(countrygroup["ConvertedComp"].median().loc["Germany"]) #print median salary Germany countrygroup variable defined countrygroup = dataframedf.groupby(["Country"])
'''
63016.0
'''
print(countrygroup["ConvertedComp"].agg(["median", "mean"]))
'''
                                             median           mean
Country                                                           
Afghanistan                                  6222.0  101953.333333
Albania                                     10818.0   21833.700000
Algeria                                      7878.0   34924.047619
...                                             ...            ...
Yemen                                       11940.0   16909.166667
Zambia                                       5040.0   10075.375000
Zimbabwe                                    19200.0   34046.666667

[179 rows x 2 columns]
'''
print(countrygroup["ConvertedComp"].agg(["median", "mean"]).loc["Canada"])
'''
median     68705.000000
mean      134018.564909
Name: Canada, dtype: float64
'''
filtercountry = dataframedf["Country"] == "United States"
print(dataframedf.loc[filtercountry]["LanguageWorkedWith"]) #print United States column LanguageWorkedWith
'''
3                                      C;C++;C#;Python;SQL
12       Bash/Shell/PowerShell;HTML/CSS;JavaScript;PHP;...
21       Bash/Shell/PowerShell;C++;HTML/CSS;JavaScript;...
22       Bash/Shell/PowerShell;HTML/CSS;JavaScript;Pyth...
25       Bash/Shell/PowerShell;C++;C#;HTML/CSS;JavaScri...
...
88877    Bash/Shell/PowerShell;Go;HTML/CSS;JavaScript;W...
Name: LanguageWorkedWith, Length: 20949, dtype: object
'''
print(dataframedf.loc[filtercountry]["LanguageWorkedWith"].str.contains("Python")) #print United States column LanguageWorkedWith is Python
'''
3         True
12       False
21        True
22        True
25        True
...
88877    False
Name: LanguageWorkedWith, Length: 20949, dtype: object
'''
print(dataframedf.loc[filtercountry]["LanguageWorkedWith"].str.contains("Python").sum()) #print United States column how mnay LanguageWorkedWith is Python
'''
10083
'''
print(countrygroup["LanguageWorkedWith"].apply(lambda x: x.str.contains("Python").sum())) #print count by country how mnay LanguageWorkedWith is Python
'''
Country
Afghanistan                                      8
                                             ...  
United States                                10083
Uruguay                                         36
Uzbekistan                                      14
Venezuela, Bolivarian Republic of...            28
Viet Nam                                        78
Yemen                                            3
Zambia                                           4
Zimbabwe                                        14
Name: LanguageWorkedWith, Length: 179, dtype: int64
'''
countryrespondents = dataframedf["Country"].value_counts()
print(countryrespondents)
'''
United States                       20949
India                                9061
Germany                              5866
                                    ...  
Papua New Guinea                        1
North Korea                             1
Tonga                                   1
Name: Country, Length: 179, dtype: int64
'''
countryusespython = countrygroup["LanguageWorkedWith"].apply(lambda x: x.str.contains("Python").sum())
print(countryusespython)
'''
Country
Afghanistan                                      8
Albania                                         23
Algeria                                         40
                                             ...  
Yemen                                            3
Zambia                                           4
Zimbabwe                                        14
Name: LanguageWorkedWith, Length: 179, dtype: int64
'''
pythondataframe = pd.concat([countryrespondents, countryusespython], axis="columns") #video included sort=False.  I got an error message.  Exclude sort=False
print(pythondataframe)
'''
 Country  LanguageWorkedWith
Afghanistan                                     44                   8
Albania                                         86                  23
Algeria                                        134                  40
...                                            ...                 ...
Yemen                                           19                   3
Zambia                                          12                   4
Zimbabwe                                        39                  14
[179 rows x 2 columns]
'''
print(pythondataframe.rename(columns={"Country": "Rename Number Of Respondents", "LanguageWorkedWith": "Rename Number Knows Python"}))
'''
                                      Rename Number Of Respondents  \
Afghanistan                                                           44   
Albania                                                               86   
Algeria                                                              134   
                                           Rename Number Knows Python  
Afghanistan                                                         8  
Albania                                                            23  
Algeria                                                            40  
[179 rows x 2 columns]
'''
pythondataframerenamecolumns = pythondataframe.rename(columns={"Country": "Rename Number Of Respondents", "LanguageWorkedWith": "Rename Number Knows Python"}, inplace=True) #inplace=True supposed to make rename columns permanent.  RM:  it didn't work.  I'm not sure inplace=True works in a print statement print(pythondataframe.rename(columns={"Country": "Rename Number Of Respondents", "LanguageWorkedWith": "Rename Number Knows Python"}))
print(pythondataframerenamecolumns) #print None
pythondataframe["New Column Percentage Knows Python"] = (pythondataframe["Rename Number Knows Python"] / pythondataframe["Rename Number Of Respondents"]) * 100
print(pythondataframerenamecolumns) #print None
#RM:  Reset exercise include a third column to calculate percentage by country how many know Python
countryrespondents = dataframedf["Country"].value_counts()
countryusespython = countrygroup["LanguageWorkedWith"].apply(lambda x: x.str.contains("Python").sum())
pythondataframe = pd.concat([countryrespondents, countryusespython], axis="columns") #video included sort=False.  I got an error message.  Exclude sort=False
pythondataframe["New Column Percentage Knows Python"] = (pythondataframe["LanguageWorkedWith"] / pythondataframe["Country"]) * 100
print(pythondataframe)
'''
Country  LanguageWorkedWith  \
Afghanistan                                     44                   8   
Albania                                         86                  23   
Algeria                                        134                  40   
                                           New Column Percentage Knows Python  
Afghanistan                                                         18.181818  
Albania                                                             26.744186  
Algeria                                                             29.850746  
[179 rows x 3 columns]
'''
print(pythondataframe.sort_values(by="New Column Percentage Knows Python", ascending=False))  #Sort by New Column Percentage Knows Python percentage highest to lowest
print(pythondataframe.sort_values(by="New Column Percentage Knows Python", ascending=False, inplace=True)) #inplace=True supposed to permanently modify the dataframe pythondataframe.  print None.  Didn't work.
pythondataframeinplacetrue = pythondataframe.sort_values(by="New Column Percentage Knows Python", ascending=False, inplace=True) #try assign a new variable
print(pythondataframeinplacetrue) #RM:  I didn't verify assign a new variable works
print(pythondataframe.sort_values(by="New Column Percentage Knows Python", ascending=False).loc["Japan"])
'''
Country                               391.000000
LanguageWorkedWith                    182.000000
New Column Percentage Knows Python     46.547315
Name: Japan, dtype: float64
'''

#Python Pandas Tutorial -Part 9- Cleaning Data - Casting Datatypes and Handling Missing Values
import pandas as pd
import numpy as np

people = {"first": ["Corey", "Jane", "John", "Chirs", np.nan, None, "NA"], "last": ["Schafer", "Doe", "Doe", "Schafer", np.nan, np.nan, "Missing"], "email": ["CoreyMSchafer@gmail.com", "Jane.Doe@email.com", "JohnDoe@email.com", None, np.nan, "Anonymous@email.com", "NA"], "age": ["33", "55", "63", "36", None, None, "Missing"]}
peopledataframe = pd.DataFrame(people)
print(peopledataframe)
'''
       age                    email  first     last
0       33  CoreyMSchafer@gmail.com  Corey  Schafer
1       55       Jane.Doe@email.com   Jane      Doe
2       63        JohnDoe@email.com   John      Doe
3       36                     None  Chirs  Schafer
4     None                      NaN    NaN      NaN
5     None      Anonymous@email.com   None      NaN
6  Missing                       NA     NA  Missing
'''
peopledataframedropna = peopledataframe.dropna() #remove rows with np.nan or NaN
print(peopledataframedropna)
'''
       age                    email  first     last
0       33  CoreyMSchafer@gmail.com  Corey  Schafer
1       55       Jane.Doe@email.com   Jane      Doe
2       63        JohnDoe@email.com   John      Doe
6  Missing                       NA     NA  Missing
'''
peopledataframedropna = peopledataframe.dropna(axis="index", how="any") #default dropna
print(peopledataframedropna)
'''
       age                    email  first     last
0       33  CoreyMSchafer@gmail.com  Corey  Schafer
1       55       Jane.Doe@email.com   Jane      Doe
2       63        JohnDoe@email.com   John      Doe
6  Missing                       NA     NA  Missing
'''
peopledataframedeleteentirerowNaN = peopledataframe.dropna(axis="index", how="all") #delete entire row with NaN or None
print(peopledataframedeleteentirerowNaN)
'''
       age                    email  first     last
0       33  CoreyMSchafer@gmail.com  Corey  Schafer
1       55       Jane.Doe@email.com   Jane      Doe
2       63        JohnDoe@email.com   John      Doe
3       36                     None  Chirs  Schafer
5     None      Anonymous@email.com   None      NaN
6  Missing                       NA     NA  Missing
'''
peopledataframedeleteentirecolumn = peopledataframe.dropna(axis="columns", how="all") #delete entire column with NaN or None
print(peopledataframedeleteentirecolumn)
'''
       age                    email  first     last
0       33  CoreyMSchafer@gmail.com  Corey  Schafer
1       55       Jane.Doe@email.com   Jane      Doe
2       63        JohnDoe@email.com   John      Doe
3       36                     None  Chirs  Schafer
4     None                      NaN    NaN      NaN
5     None      Anonymous@email.com   None      NaN
6  Missing                       NA     NA  Missing
'''
peopledataframedropna = peopledataframe.dropna(axis="index", how="any", subset=["email"]) #remove rows with NaN or None in email column
print(peopledataframedropna)
'''
       age                    email  first     last
0       33  CoreyMSchafer@gmail.com  Corey  Schafer
1       55       Jane.Doe@email.com   Jane      Doe
2       63        JohnDoe@email.com   John      Doe
5     None      Anonymous@email.com   None      NaN
6  Missing                       NA     NA  Missing
'''
peopledataframe.replace("NA", np.nan, inplace=True) #inplace=True makes replace permanent
peopledataframe.replace("Missing", np.nan, inplace=True) #inplace=True makes replace permanent
print(peopledataframe)
'''
    age                    email  first     last
0    33  CoreyMSchafer@gmail.com  Corey  Schafer
1    55       Jane.Doe@email.com   Jane      Doe
2    63        JohnDoe@email.com   John      Doe
3    36                     None  Chirs  Schafer
4  None                      NaN    NaN      NaN
5  None      Anonymous@email.com   None      NaN
6   NaN                      NaN    NaN      NaN
'''
print(peopledataframe.dropna())
'''
  age                    email  first     last
0  33  CoreyMSchafer@gmail.com  Corey  Schafer
1  55       Jane.Doe@email.com   Jane      Doe
2  63        JohnDoe@email.com   John      Doe
'''
peopledataframedropna = peopledataframe.dropna(axis="index", how="all", subset=["email", "last"])
print(peopledataframedropna)
'''
    age                    email  first     last
0    33  CoreyMSchafer@gmail.com  Corey  Schafer
1    55       Jane.Doe@email.com   Jane      Doe
2    63        JohnDoe@email.com   John      Doe
3    36                     None  Chirs  Schafer
5  None      Anonymous@email.com   None      NaN
'''
print(peopledataframe.isna())
'''
     age  email  first   last
0  False  False  False  False
1  False  False  False  False
2  False  False  False  False
3  False   True  False  False
4   True   True   True   True
5   True  False   True   True
6   True   True   True   True
'''
print(peopledataframe.fillna("Replace NA Values With MISSING"))
'''
                              age                           email  \
0                              33         CoreyMSchafer@gmail.com   
1                              55              Jane.Doe@email.com   
2                              63               JohnDoe@email.com   
3                              36  Replace NA Values With MISSING   
4  Replace NA Values With MISSING  Replace NA Values With MISSING   
5  Replace NA Values With MISSING             Anonymous@email.com   
6  Replace NA Values With MISSING  Replace NA Values With MISSING   

                            first                            last  
0                           Corey                         Schafer  
1                            Jane                             Doe  
2                            John                             Doe  
3                           Chirs                         Schafer  
4  Replace NA Values With MISSING  Replace NA Values With MISSING  
5  Replace NA Values With MISSING  Replace NA Values With MISSING  
6  Replace NA Values With MISSING  Replace NA Values With MISSING  
'''
print(peopledataframe.dtypes)
'''
age      object
email    object
first    object
last     object
dtype: object
'''
#print(peopledataframe["age"].mean()) #error message TypeError: must be str, not int
print(type(np.nan)) #print <class 'float'>
#peopledataframe["age"] = peopledataframe["age"].astype(int) #error message int() argument must be a string, a bytes-like object or a number, not 'NoneType'
peopledataframe["age"] = peopledataframe["age"].astype(float)
print(peopledataframe.dtypes)
'''
age      float64
email     object
first     object
last      object
dtype: object
'''
print(peopledataframe["age"].mean()) #print 46.75

replacevalueswithnan = ["NA", "Missing"] #NA and Missing are replaced with NaN
dataframedf = pd.read_csv("developer_survey_2019/survey_results_public.csv", index_col="Respondent", na_values=replacevalueswithnan)
readtheschema = pd.read_csv("developer_survey_2019/survey_results_schema.csv", index_col="Column")
pd.set_option("display.max_columns", 85) #allows number of columns to display horizontally
pd.set_option("display.max_rows", 85) #allows number of rows to display horizontally
print(dataframedf["YearsCode"].head(10))
'''
Respondent
1       4
2     NaN
3       3
4       3
5      16
6      13
7       6
8       8
9      12
10     12
Name: YearsCode, dtype: object
'''
#print(dataframedf["YearsCode"].mean()) #print TypeError: must be str, not int  Reason is NaN is a float type float.  Solution convert YearsCode column to float.
#dataframedf["YearsCode"] = dataframedf["YearsCode"].astype(float)
#print(dataframedf["YearsCode"].mean()) #print ValueError: could not convert string to float: 'Less than 1 year'
print(dataframedf["YearsCode"].unique()) #print unique values or distinct values
'''
Name: YearsCode, dtype: object
['4' nan '3' '16' '13' '6' '8' '12' '2' '5' '17' '10' '14' '35' '7'
 'Less than 1 year' '30' '9' '26' '40' '19' '15' '20' '28' '25' '1' '22'
 '11' '33' '50' '41' '18' '34' '24' '23' '42' '27' '21' '36' '32' '39'
 '38' '31' '37' 'More than 50 years' '29' '44' '45' '48' '46' '43' '47'
 '49']
'''
dataframedf["YearsCode"].replace("Less than 1 year", 0, inplace=True) #inplace=True required to make it permanent
dataframedf["YearsCode"].replace("More than 50 years", 51, inplace=True) #inplace=True required to make it permanent
dataframedf["YearsCode"] = dataframedf["YearsCode"].astype(float)
print(dataframedf["YearsCode"].unique())
'''
[ 4. nan  3. 16. 13.  6.  8. 12.  2.  5. 17. 10. 14. 35.  7.  0. 30.  9.
 26. 40. 19. 15. 20. 28. 25.  1. 22. 11. 33. 50. 41. 18. 34. 24. 23. 42.
 27. 21. 36. 32. 39. 38. 31. 37. 51. 29. 44. 45. 48. 46. 43. 47. 49.]
'''
print(dataframedf["YearsCode"].mean()) #print 11.662114216834588
print(dataframedf["YearsCode"].median()) #print 9.0

#Python Pandas Tutorial -Part 10- Working with Dates and Time Series Data
import pandas as pd
dfdataframe = pd.read_csv("ETH_1h.csv") #CSV file is a cryptocurrency file Ethereum ETH
print(dfdataframe.head()) #CSV file is a cryptocurrency file Ethereum ETH
'''
               Date  Symbol    Open    High     Low   Close      Volume
0  2020-03-13 08-PM  ETHUSD  129.94  131.82  126.87  128.71  1940673.93
1  2020-03-13 07-PM  ETHUSD  119.51  132.02  117.10  129.94  7579741.09
2  2020-03-13 06-PM  ETHUSD  124.47  124.85  115.50  119.51  4898735.81
3  2020-03-13 05-PM  ETHUSD  124.08  127.42  121.63  124.47  2753450.92
4  2020-03-13 04-PM  ETHUSD  124.85  129.51  120.17  124.08  4461424.71
'''
print(dfdataframe.loc[0, "Date"]) #print 2020-03-13 08-PM
print(type(dfdataframe.loc[0, "Date"])) #print <class 'str'>
#instructor says okay to look at strftime and strptime documentation.  Can't memorize all. docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes
dfdataframe["Date"] = pd.to_datetime(dfdataframe["Date"], format="%Y-%m-%d %I-%p")
print(dfdataframe["Date"].head())
'''
0   2020-03-13 20:00:00
1   2020-03-13 19:00:00
2   2020-03-13 18:00:00
3   2020-03-13 17:00:00
4   2020-03-13 16:00:00
Name: Date, dtype: datetime64[ns]
'''
print(dfdataframe.loc[0, "Date"]) #print 2020-03-13 20:00:00
print(type(dfdataframe.loc[0, "Date"])) #print <class 'pandas._libs.tslib.Timestamp'>

#format Date column during Panda reading .csv file
#dateparserlambda = lambda x: pd.datetime.strptime(x, "%Y-%m-%d %I-%p")
def dateparserlambda(x): return pd.datetime.strptime(x, "%Y-%m-%d %I-%p") #my Sublime Python packages edit my lambda formula.  Original lambda is above.


dfdataframeconvertstringtodatehere = pd.read_csv("ETH_1h.csv", parse_dates=["Date"], date_parser=dateparserlambda) #CSV file is a cryptocurrency file Ethereum ETH
print(dfdataframeconvertstringtodatehere.head())
'''
                 Date  Symbol    Open    High     Low   Close      Volume
0 2020-03-13 20:00:00  ETHUSD  129.94  131.82  126.87  128.71  1940673.93
1 2020-03-13 19:00:00  ETHUSD  119.51  132.02  117.10  129.94  7579741.09
2 2020-03-13 18:00:00  ETHUSD  124.47  124.85  115.50  119.51  4898735.81
3 2020-03-13 17:00:00  ETHUSD  124.08  127.42  121.63  124.47  2753450.92
4 2020-03-13 16:00:00  ETHUSD  124.85  129.51  120.17  124.08  4461424.71
'''
#dfdataframeconvertstringtodatehere["New Column Day Of Week"] = dfdataframeconvertstringtodatehere.dt.day_name() #error message AttributeError: 'DataFrame' object has no attribute 'dt'
print(dfdataframeconvertstringtodatehere["Date"].min()) #print 2017-07-01 11:00:00
print(dfdataframeconvertstringtodatehere["Date"].max()) #print 2020-03-13 20:00:00
print(dfdataframeconvertstringtodatehere["Date"].max() - dfdataframeconvertstringtodatehere["Date"].min()) #print 986 days 09:00:00
year20192000filter = (dfdataframeconvertstringtodatehere["Date"] >= "2019") & (dfdataframeconvertstringtodatehere["Date"] < "2020")
year20192000datesfilter = (dfdataframeconvertstringtodatehere["Date"] >= pd.to_datetime("2019-01-01")) & (dfdataframeconvertstringtodatehere["Date"] < pd.to_datetime("2020-01-10"))
year2000filter = dfdataframeconvertstringtodatehere["Date"] >= "2020"
print(dfdataframeconvertstringtodatehere.loc[year2000filter])
'''
Date  Symbol    Open    High     Low   Close       Volume
0    2020-03-13 20:00:00  ETHUSD  129.94  131.82  126.87  128.71   1940673.93
1    2020-03-13 19:00:00  ETHUSD  119.51  132.02  117.10  129.94   7579741.09
2    2020-03-13 18:00:00  ETHUSD  124.47  124.85  115.50  119.51   4898735.81
3    2020-03-13 17:00:00  ETHUSD  124.08  127.42  121.63  124.47   2753450.92
...
1746 2020-01-01 02:00:00  ETHUSD  130.14  130.50  129.91  130.37    396315.72
1747 2020-01-01 01:00:00  ETHUSD  128.34  130.14  128.32  130.14    635419.40
1748 2020-01-01 00:00:00  ETHUSD  128.54  128.54  128.12  128.34    245119.91
'''
indexcolumnisdate = dfdataframeconvertstringtodatehere.set_index("Date")
print(indexcolumnisdate.head())
'''
Symbol    Open    High     Low   Close      Volume
Date
2020-03-13 20:00:00  ETHUSD  129.94  131.82  126.87  128.71  1940673.93
2020-03-13 19:00:00  ETHUSD  119.51  132.02  117.10  129.94  7579741.09
2020-03-13 18:00:00  ETHUSD  124.47  124.85  115.50  119.51  4898735.81
2020-03-13 17:00:00  ETHUSD  124.08  127.42  121.63  124.47  2753450.92
2020-03-13 16:00:00  ETHUSD  124.85  129.51  120.17  124.08  4461424.71
'''
#indexcolumnisdate = dfdataframeconvertstringtodatehere.set_index("Date", inplace=True) #inplace=True makes set index permanent created an error maybe assign to another variable
dfdataframeconvertstringtodatehere.set_index("Date", inplace=True)  #inplace=True makes set index permanent
print(dfdataframeconvertstringtodatehere.head())
'''
                     Symbol    Open    High     Low   Close      Volume
Date                                                                   
2020-03-13 20:00:00  ETHUSD  129.94  131.82  126.87  128.71  1940673.93
2020-03-13 19:00:00  ETHUSD  119.51  132.02  117.10  129.94  7579741.09
2020-03-13 18:00:00  ETHUSD  124.47  124.85  115.50  119.51  4898735.81
2020-03-13 17:00:00  ETHUSD  124.08  127.42  121.63  124.47  2753450.92
2020-03-13 16:00:00  ETHUSD  124.85  129.51  120.17  124.08  4461424.71
'''
print(dfdataframeconvertstringtodatehere["2019"].head())
'''
                     Symbol    Open    High     Low   Close      Volume
Date                                                                   
2019-12-31 23:00:00  ETHUSD  128.33  128.69  128.14  128.54   440678.91
2019-12-31 22:00:00  ETHUSD  128.38  128.69  127.95  128.33   554646.02
2019-12-31 21:00:00  ETHUSD  127.86  128.43  127.72  128.38   350155.69
2019-12-31 20:00:00  ETHUSD  127.84  128.34  127.71  127.86   428183.38
2019-12-31 19:00:00  ETHUSD  128.69  128.69  127.60  127.84  1169847.84
'''
print(dfdataframeconvertstringtodatehere["2020-01-19":"2020-02-14"])
'''                  Symbol    Open    High     Low   Close      Volume
Date                                                                                                                                 
2020-02-14 23:00:00  ETHUSD  284.13  287.98  282.68  286.27  2265638.82
2020-02-14 22:00:00  ETHUSD  282.79  284.53  281.32  284.13  2552361.21
2020-02-14 21:00:00  ETHUSD  283.24  284.50  281.64  282.79  2068601.56
...                     ...     ...     ...     ...     ...         ...
2020-01-19 02:00:00  ETHUSD  175.18  176.90  174.50  176.24   972557.22
2020-01-19 01:00:00  ETHUSD  176.18  178.00  174.00  175.18  2372314.02
2020-01-19 00:00:00  ETHUSD  174.06  176.37  173.18  176.18   697611.75

[648 rows x 6 columns]
'''
print(dfdataframeconvertstringtodatehere["2020-01-19":"2020-02-14"]["Close"])  #get the Close column
'''
Date
2020-02-14 23:00:00    286.27
2020-02-14 22:00:00    284.13
2020-02-14 21:00:00    282.79
                        ...  
2020-01-19 02:00:00    176.24
2020-01-19 01:00:00    175.18
2020-01-19 00:00:00    176.18
Name: Close, Length: 648, dtype: float64
'''
print(dfdataframeconvertstringtodatehere["2020-01-19":"2020-02-14"]["Close"].mean()) #print 194.86529320987654
print(dfdataframeconvertstringtodatehere["2020-01-01"]["High"])  #get the High column for Jan 1, 2020
'''
Date
2020-01-01 23:00:00    130.27
2020-01-01 22:00:00    131.41
2020-01-01 21:00:00    131.99
2020-01-01 20:00:00    131.87
2020-01-01 19:00:00    131.72
2020-01-01 18:00:00    132.14
2020-01-01 17:00:00    132.68
2020-01-01 16:00:00    132.56
2020-01-01 15:00:00    132.15
2020-01-01 14:00:00    132.05
2020-01-01 13:00:00    132.08
2020-01-01 12:00:00    131.31
2020-01-01 11:00:00    131.42
2020-01-01 10:00:00    130.33
2020-01-01 09:00:00    130.22
2020-01-01 08:00:00    130.01
2020-01-01 07:00:00    130.25
2020-01-01 06:00:00    130.25
2020-01-01 05:00:00    129.94
2020-01-01 04:00:00    130.00
2020-01-01 03:00:00    130.44
2020-01-01 02:00:00    130.50
2020-01-01 01:00:00    130.14
2020-01-01 00:00:00    128.54
Name: High, dtype: float64
'''
print(dfdataframeconvertstringtodatehere["2020-01-01"]["High"].max())  #print 132.68
#instructor says okay to look at strftime and strptime documentation. Can't memorize all. pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#dateoffset-objects
highestamountperday = dfdataframeconvertstringtodatehere["High"].resample("D").max() #Resample at a daily basis.  Get the highest number from the High column
print(highestamountperday)
'''
Date
2017-07-01    279.99
2017-07-02    293.73
2017-07-03    285.00
2017-07-04    282.83
2017-07-05    274.97
...
2020-03-09    208.65
2020-03-10    206.28
2020-03-11    202.98
2020-03-12    195.64
2020-03-13    148.00
Freq: D, Name: High, Length: 987, dtype: float64
'''
print(highestamountperday["2020-01-01"]) #print 132.68
# import matplotlib.pyplot as plt
# plt.title("plt.title()", fontsize=20)
# plt.xlabel("plt.xlabel()")
# plt.ylabel("plt.ylabel())")
# plt.plot(highestamountperday)
# plt.show()
print(dfdataframeconvertstringtodatehere.resample("W").mean())  #mean values by week average values for each column by week
'''
Open         High          Low        Close        Volume
Date                                                                        
2017-07-02   268.066486   271.124595   264.819730   268.202162  2.185035e+06
2017-07-09   261.337024   262.872917   259.186190   261.062083  1.337349e+06
2017-07-16   196.193214   199.204405   192.722321   195.698393  2.986756e+06
2017-07-23   212.351429   215.779286   209.126310   212.783750  4.298593e+06
2017-07-30   203.496190   205.110357   201.714048   203.309524  1.581729e+06
...                 ...          ...          ...          ...           ...
2020-02-09   207.392202   208.751964   206.279762   207.633333  1.112929e+06
2020-02-16   255.021667   257.255238   252.679762   255.198452  2.329087e+06
2020-02-23   265.220833   267.263690   262.948512   265.321905  1.826094e+06
2020-03-01   236.720536   238.697500   234.208750   236.373988  2.198762e+06
2020-03-08   229.923571   231.284583   228.373810   229.817619  1.628910e+06
2020-03-15   176.937521   179.979487   172.936239   176.332821  4.259828e+06

[142 rows x 5 columns]
'''
print(dfdataframeconvertstringtodatehere.resample("W").agg({"Close": "mean", "High": "max", "Low": "min", "Volume": "sum"}))
'''
                  Close     High     Low        Volume
Date                                                  
2017-07-02   268.202162   293.73  253.23  8.084631e+07
2017-07-09   261.062083   285.00  231.25  2.246746e+08
2017-07-16   195.698393   240.33  130.26  5.017750e+08
2017-07-23   212.783750   249.40  153.25  7.221637e+08
2017-07-30   203.309524   229.99  178.03  2.657305e+08
...                 ...      ...     ...           ...
2020-02-09   207.633333   230.90  184.29  1.869721e+08
2020-02-16   255.198452   290.00  216.31  3.912867e+08
2020-02-23   265.321905   287.13  242.36  3.067838e+08
2020-03-01   236.373988   278.13  209.26  3.693920e+08
2020-03-08   229.817619   253.01  196.00  2.736569e+08
2020-03-15   176.332821   208.65   90.00  4.983998e+08

[142 rows x 4 columns]
'''

#Python Pandas Tutorial -Part 11- ReadingWriting Data to Different Sources - Excel- JSON- SQL- Etc
import pandas as pd
dataframedf = pd.read_csv("developer_survey_2019/survey_results_public.csv")
readtheschema = pd.read_csv("developer_survey_2019/survey_results_schema.csv")
pd.set_option("display.max_columns", 85) #allows number of columns to display horizontally
pd.set_option("display.max_rows", 85) #allows number of rows to display horizontally
#print(dataframedf.head())
filtercanada = dataframedf["Country"] == "Canada"
dataframedffiltercanada = dataframedf.loc[filtercanada]
#print(dataframedffiltercanada.head())
dataframedffiltercanada.to_csv("developer_survey_2019/canadacsv.csv") #export Panda dataframe in .csv
dataframedffiltercanada.to_csv("developer_survey_2019/canadatabdelimited.tsv", sep="\t") #export Panda dataframe in .tsv tab delimited
dataframedfreadtabdelimited = pd.read_csv("developer_survey_2019/canadatabdelimited.tsv", sep="\t")
dataframedffiltercanada.to_json("developer_survey_2019/canadajson.json", orient="records", lines=True)
dataframedfreadjson = pd.read_json("developer_survey_2019/canadajson.json", orient="records", lines=True)
