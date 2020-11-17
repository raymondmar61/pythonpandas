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