#Pandas YouTube channel Data School 03/03/21 https://www.youtube.com/c/dataschool/about
import pandas as pd

#How do I read a tabular data file into pandas-5_QXMwezPJE
#orders = pd.read_table("webpageurl")  #read_table can read directly from a URL.  Default must be tab separated.  First row must be header row.
orders = pd.read_table("http://bit.ly/chiporders")  #read_table can read directly from a URL.  Default must be tab separated.  First row must be header row.
print(orders)
'''
  order_id  quantity                              item_name  \
0            1         1           Chips and Fresh Tomato Salsa   
1            1         1                                   Izze   
2            1         1                       Nantucket Nectar   
3            1         1  Chips and Tomatillo-Green Chili Salsa   
4            2         2                           Chicken Bowl   
5            3         1                           Chicken Bowl   
6            3         1                          Side of Chips   
'''
print(orders.head())
'''
   order_id  quantity                              item_name  \
0         1         1           Chips and Fresh Tomato Salsa   
1         1         1                                   Izze   
2         1         1                       Nantucket Nectar   
3         1         1  Chips and Tomatillo-Green Chili Salsa   
4         2         2                           Chicken Bowl   

                                  choice_description item_price  
0                                                NaN     $2.39   
1                                       [Clementine]     $3.39   
2                                            [Apple]     $3.39   
3                                                NaN     $2.39   
4  [Tomatillo-Red Chili Salsa (Hot), [Black Beans...    $16.98   
'''
movieusers = pd.read_table("http://bit.ly/movieusers")
print(movieusers)
'''
 1|24|M|technician|85711
0              2|53|F|other|94043
1             3|23|M|writer|32067
2         4|24|M|technician|43537
3              5|33|F|other|15213
4          6|42|M|executive|98101
5      7|57|M|administrator|91344
'''
usercolumns = ["userid", "age", "gender", "occupation", "zipcode"]
movieuserschangedefaults = pd.read_table("http://bit.ly/movieusers", sep="|", header=None, names=usercolumns, skiprows=None, skipfooter=None)
print(movieuserschangedefaults)
'''
     userid  age gender     occupation zipcode
0         1   24      M     technician   85711
1         2   53      F          other   94043
2         3   23      M         writer   32067
3         4   24      M     technician   43537
4         5   33      F          other   15213
5         6   42      M      executive   98101
6         7   57      M  administrator   91344
'''

#How do I select a pandas Series from a DataFrame-zxqjeyKP2Tk
ufo = pd.read_table("http://bit.ly/uforeports", sep=",")  #online file is a .csv
uforeadcsv = pd.read_csv("http://bit.ly/uforeports") #difference between read_table and read_csv is read_csv separator default is comma
print(uforeadcsv.shape) #print (18241, 5) (rows, columns)
print(uforeadcsv.head())
'''
                   City Colors Reported Shape Reported State             Time
0                Ithaca             NaN       TRIANGLE    NY   6/1/1930 22:00
1           Willingboro             NaN          OTHER    NJ  6/30/1930 20:00
2               Holyoke             NaN           OVAL    CO  2/15/1931 14:00
3               Abilene             NaN           DISK    KS   6/1/1931 13:00
4  New York Worlds Fair             NaN          LIGHT    NY  4/18/1933 19:00
'''
ufocitycolumncasesensitive = uforeadcsv["City"]
print(ufocitycolumncasesensitive.head())
'''
0                  Ithaca
1             Willingboro
2                 Holyoke
3                 Abilene
4    New York Worlds Fair
Name: City, dtype: object
'''
print(uforeadcsv.City.head())
'''
0                  Ithaca
1             Willingboro
2                 Holyoke
3                 Abilene
4    New York Worlds Fair
Name: City, dtype: object
'''
bracketsrequiredforcolumnheaderswithspaces = uforeadcsv["Colors Reported"]
print(bracketsrequiredforcolumnheaderswithspaces.head())
'''
0    NaN
1    NaN
2    NaN
3    NaN
4    NaN
Name: Colors Reported, dtype: object
'''
combinecolumns = uforeadcsv["City"] + ", " + uforeadcsv["State"]
print(combinecolumns.head())
'''
0                  Ithaca, NY
1             Willingboro, NJ
2                 Holyoke, CO
3                 Abilene, KS
4    New York Worlds Fair, NY
dtype: object
'''
uforeadcsv["newcolumnname"] = uforeadcsv["City"] + ", " + uforeadcsv["State"]
print(uforeadcsv.head())
'''
                   City Colors Reported Shape Reported State             Time  \
0                Ithaca             NaN       TRIANGLE    NY   6/1/1930 22:00   
1           Willingboro             NaN          OTHER    NJ  6/30/1930 20:00   
2               Holyoke             NaN           OVAL    CO  2/15/1931 14:00   
3               Abilene             NaN           DISK    KS   6/1/1931 13:00   
4  New York Worlds Fair             NaN          LIGHT    NY  4/18/1933 19:00   

              newcolumnname  
0                Ithaca, NY  
1           Willingboro, NJ  
2               Holyoke, CO  
3               Abilene, KS  
4  New York Worlds Fair, NY 
'''

#Why do some pandas commands end with parentheses (and others don't)-hSrDViyKWVk
#Methods with parenthesis and attributes without paranthesis.  Methods are actions.  Attributes are descriptions.  Methods have required and optional arguments.
moviesdataframe = pd.read_csv("http://bit.ly/imdbratings")  #RM:  YouTuber's IMDB Top 250 movies list?
print(moviesdataframe.head())
'''
   star_rating                     title content_rating   genre  duration  \
0          9.3  The Shawshank Redemption              R   Crime       142   
1          9.2             The Godfather              R   Crime       175   
2          9.1    The Godfather: Part II              R   Crime       200   
3          9.0           The Dark Knight          PG-13  Action       152   
4          8.9              Pulp Fiction              R   Crime       154   

                                         actors_list  
0  [u'Tim Robbins', u'Morgan Freeman', u'Bob Gunt...  
1    [u'Marlon Brando', u'Al Pacino', u'James Caan']  
2  [u'Al Pacino', u'Robert De Niro', u'Robert Duv...  
3  [u'Christian Bale', u'Heath Ledger', u'Aaron E...  
4  [u'John Travolta', u'Uma Thurman', u'Samuel L.... 
'''
print(moviesdataframe.describe())  #Statistics on columns with numbers
'''
       star_rating    duration
count   979.000000  979.000000
mean      7.889785  120.979571
std       0.336069   26.218010
min       7.400000   64.000000
25%       7.600000  102.000000
50%       7.800000  117.000000
75%       8.100000  134.000000
max       9.300000  242.000000
'''
print(moviesdataframe.shape) #print (979, 6) (rows, columns)
print(moviesdataframe.dtypes)
'''
star_rating       float64
title              object
content_rating     object
genre              object
duration            int64
actors_list        object
dtype: object
'''
print(type(moviesdataframe)) #print <class 'pandas.core.frame.DataFrame'>
print(moviesdataframe.describe(include=["object"]))  #Statistics on all columns
'''
          title content_rating  genre  \
count       979            976    979   
unique      975             12     16   
top     Dracula              R  Drama   
freq          2            460    278   

                                              actors_list  
count                                                 979  
unique                                                969  
top     [u'Daniel Radcliffe', u'Emma Watson', u'Rupert...  
freq                                                    6  
'''

#How do I rename columns in a pandas DataFrame-0uBirYFhizE
ufodataframe = pd.read_csv("http://bit.ly/uforeports")
print(ufodataframe.head())
'''
                   City Colors Reported Shape Reported State             Time
0                Ithaca             NaN       TRIANGLE    NY   6/1/1930 22:00
1           Willingboro             NaN          OTHER    NJ  6/30/1930 20:00
2               Holyoke             NaN           OVAL    CO  2/15/1931 14:00
3               Abilene             NaN           DISK    KS   6/1/1931 13:00
4  New York Worlds Fair             NaN          LIGHT    NY  4/18/1933 19:00
'''
print(ufodataframe.columns) #print Index(['City', 'Colors Reported', 'Shape Reported', 'State', 'Time'], dtype='object')
print(ufodataframe.columns[2]) #print Shape Reported
ufodataframe.rename(columns={"Colors Reported": "new column name ColorsReported", "Shape Reported": "ShapeReported"}, inplace=True)
print(ufodataframe.columns) #print Index(['City', 'new column name ColorsReported', 'ShapeReported', 'State', 'Time'], dtype='object')
ufonewcolumnames = ["city", "colors reported", "shape reported", "state", "time"]
ufodataframe.columns = ufonewcolumnames
print(ufodataframe.columns) #print Index(['city', 'colors reported', 'shape reported', 'state', 'time'], dtype='object')
ufonewcolumnames2 = ["city", "colors reported", "shape reported", "state", "time"]
ufodataframe2 = pd.read_csv("http://bit.ly/uforeports", names=ufonewcolumnames2, header=0)  #row zero is the column headers
print(ufodataframe2.head())
'''
                   city colors reported shape reported state             time
0                Ithaca             NaN       TRIANGLE    NY   6/1/1930 22:00
1           Willingboro             NaN          OTHER    NJ  6/30/1930 20:00
2               Holyoke             NaN           OVAL    CO  2/15/1931 14:00
3               Abilene             NaN           DISK    KS   6/1/1931 13:00
4  New York Worlds Fair             NaN          LIGHT    NY  4/18/1933 19:00
'''
#replace spaces in column headers with underscores
ufodataframe2.columns = ufodataframe2.columns.str.replace(" ", "_")
print(ufodataframe2.columns) #print Index(['city', 'colors_reported', 'shape_reported', 'state', 'time'], dtype='object')

#How do I remove columns from a pandas DataFrame?
ufodataframe = pd.read_csv("http://bit.ly/uforeports")
print(ufodataframe.head())
'''
                   City Colors Reported Shape Reported State             Time
0                Ithaca             NaN       TRIANGLE    NY   6/1/1930 22:00
1           Willingboro             NaN          OTHER    NJ  6/30/1930 20:00
2               Holyoke             NaN           OVAL    CO  2/15/1931 14:00
3               Abilene             NaN           DISK    KS   6/1/1931 13:00
4  New York Worlds Fair             NaN          LIGHT    NY  4/18/1933 19:00
'''
print(ufodataframe.shape) #print (18241, 5)
ufodataframe.drop("Colors Reported", axis=1, inplace=True)  #axis is a direction.  0 is row.  1 is column.
print(ufodataframe.head())
'''
                   City Shape Reported State             Time
0                Ithaca       TRIANGLE    NY   6/1/1930 22:00
1           Willingboro          OTHER    NJ  6/30/1930 20:00
2               Holyoke           OVAL    CO  2/15/1931 14:00
3               Abilene           DISK    KS   6/1/1931 13:00
4  New York Worlds Fair          LIGHT    NY  4/18/1933 19:00
'''
ufodataframe.drop(["City", "State"], axis=1, inplace=True)
print(ufodataframe.head())
'''
  Shape Reported             Time
0       TRIANGLE   6/1/1930 22:00
1          OTHER  6/30/1930 20:00
2           OVAL  2/15/1931 14:00
3           DISK   6/1/1931 13:00
4          LIGHT  4/18/1933 19:00
'''
#remove rows
ufodataframe.drop([0, 1], axis=0, inplace=True)  #rows are called indexes or labels
print(ufodataframe.head())
'''
  Shape Reported             Time
2           OVAL  2/15/1931 14:00
3           DISK   6/1/1931 13:00
4          LIGHT  4/18/1933 19:00
5           DISK  9/15/1934 15:30
6         CIRCLE   6/15/1935 0:00
'''
print(ufodataframe.shape) #print (18239, 2)

#How do I sort a pandas DataFrame or a Series?
moviesimdbdataframe = pd.read_csv("http://bit.ly/imdbratings")
print(moviesimdbdataframe.head())
'''
   star_rating                     title content_rating   genre  duration  \
0          9.3  The Shawshank Redemption              R   Crime       142   
1          9.2             The Godfather              R   Crime       175   
2          9.1    The Godfather: Part II              R   Crime       200   
3          9.0           The Dark Knight          PG-13  Action       152   
4          8.9              Pulp Fiction              R   Crime       154   

                                         actors_list  
0  [u'Tim Robbins', u'Morgan Freeman', u'Bob Gunt...  
1    [u'Marlon Brando', u'Al Pacino', u'James Caan']  
2  [u'Al Pacino', u'Robert De Niro', u'Robert Duv...  
3  [u'Christian Bale', u'Heath Ledger', u'Aaron E...  
4  [u'John Travolta', u'Uma Thurman', u'Samuel L....  
'''
print(moviesimdbdataframe.title.sort_values()) #Two versions to sort a series or a column
'''
542                   (500) Days of Summer
5                             12 Angry Men
201                       12 Years a Slave
698                              127 Hours
110                  2001: A Space Odyssey
910                                   2046
596                               21 Grams
624                              25th Hour
708                       28 Days Later...
60                                3 Idiots
225                                 3-Iron
570                                    300
...
Name: title, Length: 979, dtype: object
'''
print(moviesimdbdataframe["title"].sort_values(ascending=False)) #Two versions to sort a series or a column
'''
864                                  [Rec]
526                                   Zulu
615                             Zombieland
677                                 Zodiac
955                       Zero Dark Thirty
535                                  Zelig
280                     Young Frankenstein
96                                 Yojimbo
235                                Yip Man
403                             Ying xiong
695                      Y Tu Mama Tambien
871                                     X2
Name: title, Length: 979, dtype: object
'''
print(moviesimdbdataframe.sort_values("title", ascending=False).head()) #returns a data frame
'''
     star_rating                  title content_rating      genre  duration  \
542          7.8   (500) Days of Summer          PG-13     Comedy        95   
5            8.9           12 Angry Men      NOT RATED      Drama        96   
201          8.1       12 Years a Slave              R  Biography       134   
698          7.6              127 Hours              R  Adventure        94   
110          8.3  2001: A Space Odyssey              G    Mystery       160   

                                           actors_list  
542  [u'Zooey Deschanel', u'Joseph Gordon-Levitt', ...  
5    [u'Henry Fonda', u'Lee J. Cobb', u'Martin Bals...  
201  [u'Chiwetel Ejiofor', u'Michael Kenneth Willia...  
698  [u'James Franco', u'Amber Tamblyn', u'Kate Mara']  
110  [u'Keir Dullea', u'Gary Lockwood', u'William S...  
'''
print(moviesimdbdataframe.sort_values(["content_rating", "duration"], ascending=True).head()) #sort multiple columns
'''
     star_rating                           title content_rating      genre  \
713          7.6                 The Jungle Book       APPROVED  Animation   
513          7.8  Invasion of the Body Snatchers       APPROVED     Horror   
272          8.1                     The Killing       APPROVED      Crime   
703          7.6                         Dracula       APPROVED     Horror   
612          7.7              A Hard Day's Night       APPROVED     Comedy   

     duration                                        actors_list  
713        78  [u'Phil Harris', u'Sebastian Cabot', u'Louis P...  
513        80  [u'Kevin McCarthy', u'Dana Wynter', u'Larry Ga...  
272        85  [u'Sterling Hayden', u'Coleen Gray', u'Vince E...  
703        85  [u'Bela Lugosi', u'Helen Chandler', u'David Ma...  
612        87  [u'John Lennon', u'Paul McCartney', u'George H...  
'''

#How do I filter rows of a pandas DataFrame by column value-2AFGPdNn4FM
movies = pd.read_csv("http://bit.ly/imdbratings")
print(movies.head())
'''
   star_rating                     title content_rating   genre  duration  \
0          9.3  The Shawshank Redemption              R   Crime       142   
1          9.2             The Godfather              R   Crime       175   
2          9.1    The Godfather: Part II              R   Crime       200   
3          9.0           The Dark Knight          PG-13  Action       152   
4          8.9              Pulp Fiction              R   Crime       154   

                                         actors_list  
0  [u'Tim Robbins', u'Morgan Freeman', u'Bob Gunt...  
1    [u'Marlon Brando', u'Al Pacino', u'James Caan']  
2  [u'Al Pacino', u'Robert De Niro', u'Robert Duv...  
3  [u'Christian Bale', u'Heath Ledger', u'Aaron E...  
4  [u'John Travolta', u'Uma Thurman', u'Samuel L....  
'''
print(movies.shape) #print (979, 6)
booleanslist = []
for movieslength in movies.duration:
  if movieslength >= 200:
    booleanslist.append(True)
  else:
    booleanslist.append(False)
print(booleanslist[0:5]) #print [False, False, True, False, False]
print(len(booleanslist)) #print 979
long200movies = pd.Series(booleanslist)
print(long200movies.head())
'''
0    False
1    False
2     True
3    False
4    False
dtype: bool
'''
print(movies[long200movies])  #RM:  it printed the movies rows where True from long200movies
'''
     star_rating                                          title  \
2            9.1                         The Godfather: Part II   
7            8.9  The Lord of the Rings: The Return of the King   
17           8.7                                  Seven Samurai   
78           8.4                    Once Upon a Time in America   
85           8.4                             Lawrence of Arabia   
...
'''
print(movies["genre"]) #RM:  comparison to slice a pandas data frame by column
'''
0          Crime
1          Crime
2          Crime
3         Action
4          Crime
5          Drama
6        Western
7      Adventure
8      Biography
...
'''
long200moviesdirectway = movies.duration >= 200
print(long200moviesdirectway.head())
'''
0    False
1    False
2     True
3    False
4    False
Name: duration, dtype: bool
'''
print(movies[long200moviesdirectway].head())
'''
    star_rating                                          title content_rating  \
2           9.1                         The Godfather: Part II              R   
7           8.9  The Lord of the Rings: The Return of the King          PG-13   
17          8.7                                  Seven Samurai        UNRATED   
78          8.4                    Once Upon a Time in America              R   
85          8.4                             Lawrence of Arabia             PG   

        genre  duration                                        actors_list  
2       Crime       200  [u'Al Pacino', u'Robert De Niro', u'Robert Duv...  
7   Adventure       201  [u'Elijah Wood', u'Viggo Mortensen', u'Ian McK...  
17      Drama       207  [u'Toshir\xf4 Mifune', u'Takashi Shimura', u'K...  
78      Crime       229  [u'Robert De Niro', u'James Woods', u'Elizabet...  
85  Adventure       216  [u"Peter O'Toole", u'Alec Guinness', u'Anthony...  
'''
print(movies[movies.duration >= 200].head())
'''
    star_rating                                          title content_rating  \
2           9.1                         The Godfather: Part II              R   
7           8.9  The Lord of the Rings: The Return of the King          PG-13   
17          8.7                                  Seven Samurai        UNRATED   
78          8.4                    Once Upon a Time in America              R   
85          8.4                             Lawrence of Arabia             PG   

        genre  duration                                        actors_list  
2       Crime       200  [u'Al Pacino', u'Robert De Niro', u'Robert Duv...  
7   Adventure       201  [u'Elijah Wood', u'Viggo Mortensen', u'Ian McK...  
17      Drama       207  [u'Toshir\xf4 Mifune', u'Takashi Shimura', u'K...  
78      Crime       229  [u'Robert De Niro', u'James Woods', u'Elizabet...  
85  Adventure       216  [u"Peter O'Toole", u'Alec Guinness', u'Anthony... 
'''
print(movies[movies.duration >= 200].genre.head()) #print(movies[movies.duration >= 200]["genre"]head()) also works
'''
2         Crime
7     Adventure
17        Drama
78        Crime
85    Adventure
Name: genre, dtype: object
'''
print(movies.loc[movies.duration >= 200, "genre"].head()) #YouTuber says .loc best way
'''
2         Crime
7     Adventure
17        Drama
78        Crime
85    Adventure
Name: genre, dtype: object
'''

#How do I apply multiple filter criteria to a pandas DataFrame-YPItfQ87qjM
movies = pd.read_csv("http://bit.ly/imdbratings")
print(movies.head())
'''
   star_rating                     title content_rating   genre  duration  \
0          9.3  The Shawshank Redemption              R   Crime       142   
1          9.2             The Godfather              R   Crime       175   
2          9.1    The Godfather: Part II              R   Crime       200   
3          9.0           The Dark Knight          PG-13  Action       152   
4          8.9              Pulp Fiction              R   Crime       154   

                                         actors_list  
0  [u'Tim Robbins', u'Morgan Freeman', u'Bob Gunt...  
1    [u'Marlon Brando', u'Al Pacino', u'James Caan']  
2  [u'Al Pacino', u'Robert De Niro', u'Robert Duv...  
3  [u'Christian Bale', u'Heath Ledger', u'Aaron E...  
4  [u'John Travolta', u'Uma Thurman', u'Samuel L....  
'''
print(movies[movies.duration >= 200])
'''
    content_rating      genre  duration  \
2                R      Crime       200   
7            PG-13  Adventure       201   
17         UNRATED      Drama       207   
78               R      Crime       229   
85              PG  Adventure       216   
...
'''
dramamoviesover200minutes = movies[(movies.duration >= 200) & (movies.genre == "Drama")]
print(dramamoviesover200minutes)
'''
    star_rating               title content_rating  genre  duration  \
17           8.7       Seven Samurai        UNRATED  Drama       207   
157          8.2  Gone with the Wind              G  Drama       238   
476          7.8              Hamlet          PG-13  Drama       242   
...
'''
dramamovieorsover200minutes = movies[(movies.duration >= 200) | (movies.genre == "Drama")]
print(dramamovieorsover200minutes)
'''
title  \
2            9.1                          The Godfather: Part II   
5            8.9                                    12 Angry Men   
7            8.9   The Lord of the Rings: The Return of the King   
9            8.9                                      Fight Club   
13           8.8                                    Forrest Gump   
'''
print(movies[(movies.genre == "Crime") | (movies.genre == "Drama") | (movies.genre == "Action")])
'''
  star_rating                                            title  \
0            9.3                         The Shawshank Redemption   
1            9.2                                    The Godfather   
2            9.1                           The Godfather: Part II   
3            9.0                                  The Dark Knight   
4            8.9                                     Pulp Fiction   
5            8.9                                     12 Angry Men   
...
'''
betterwaymultiplefiltercolumns = movies[movies.genre.isin(["Crime", "Drama", "Action"])]
print(betterwaymultiplefiltercolumns)
'''
[538 rows x 6 columns]
star_rating                                            title  \
0            9.3                         The Shawshank Redemption   
1            9.2                                    The Godfather   
2            9.1                           The Godfather: Part II   
3            9.0                                  The Dark Knight   
4            8.9                                     Pulp Fiction   
5            8.9                                     12 Angry Men   
'''

#Your pandas questions answered!-B-r9VuK80dk
#Read from a .csv file two columns only.  Fastest method to read from a .csv file.
ufo = pd.read_csv("http://bit.ly/uforeports")
print(ufo.columns) #print Index(['City', 'Colors Reported', 'Shape Reported', 'State', 'Time'], dtype='object')
ufocitystatecolumns = pd.read_csv("http://bit.ly/uforeports", usecols=["City", "State"]) #ufocitystatecolumns = pd.read_csv("http://bit.ly/uforeports", usecols=[0, 4]) also works
print(ufocitystatecolumns)
'''
                       City State
0                    Ithaca    NY
1               Willingboro    NJ
2                   Holyoke    CO
3                   Abilene    KS
4      New York Worlds Fair    NY
5               Valley City    ND
...
'''
ufofirst3rows = pd.read_csv("http://bit.ly/uforeports", nrows=3)
print(ufofirst3rows)
'''
          City  Colors Reported Shape Reported State             Time
0       Ithaca              NaN       TRIANGLE    NY   6/1/1930 22:00
1  Willingboro              NaN          OTHER    NJ  6/30/1930 20:00
2      Holyoke              NaN           OVAL    CO  2/15/1931 14:00
'''
#How do Dataframes and Series work with regard to selecting individual entries and iteration (for x in userdata:)?  Answer is Pandas series is iterable just like a Python list.
ufofirst3rows = pd.read_csv("http://bit.ly/uforeports", nrows=3)
for cityonly in ufofirst3rows.City:
  print(cityonly)
  '''
    Ithaca
    Willingboro
    Holyoke
  '''
#Iterate a Pandas dataframe Pandas has methods.
ufofirst3rows = pd.read_csv("http://bit.ly/uforeports", nrows=3)
for index, row in ufofirst3rows.iterrows():
  print(index, row.City, row.State)
  '''
    0 Ithaca NY
    1 Willingboro NJ
    2 Holyoke CO
  '''
#Drop every non-numeric column from a DataFrame?
drinks = pd.read_csv("http://bit.ly/drinksbycountry")
print(drinks.dtypes)
'''
country                          object
beer_servings                     int64
spirit_servings                   int64
wine_servings                     int64
total_litres_of_pure_alcohol    float64
continent                        object
dtype: object
'''
import numpy as np
print(drinks.select_dtypes(include=[np.number]).dtypes)
'''
beer_servings                     int64
spirit_servings                   int64
wine_servings                     int64
total_litres_of_pure_alcohol    float64
dtype: object
'''
#describe() method
print(drinks.describe())
'''
       beer_servings  spirit_servings  wine_servings  \
count     193.000000       193.000000     193.000000   
mean      106.160622        80.994819      49.450777   
std       101.143103        88.284312      79.697598   
min         0.000000         0.000000       0.000000   
25%        20.000000         4.000000       1.000000   
50%        76.000000        56.000000       8.000000   
75%       188.000000       128.000000      59.000000   
max       376.000000       438.000000     370.000000   

       total_litres_of_pure_alcohol  
count                    193.000000  
mean                       4.717098  
std                        3.773298  
min                        0.000000  
25%                        1.300000  
50%                        4.200000  
75%                        7.200000  
max                       14.400000 
'''
print(drinks.describe(include="all"))
'''
        country  beer_servings  spirit_servings  wine_servings  \
count       193     193.000000       193.000000     193.000000   
unique      193            NaN              NaN            NaN   
top     Morocco            NaN              NaN            NaN   
freq          1            NaN              NaN            NaN   
mean        NaN     106.160622        80.994819      49.450777   
std         NaN     101.143103        88.284312      79.697598   
min         NaN       0.000000         0.000000       0.000000   
25%         NaN      20.000000         4.000000       1.000000   
50%         NaN      76.000000        56.000000       8.000000   
75%         NaN     188.000000       128.000000      59.000000   
max         NaN     376.000000       438.000000     370.000000   

        total_litres_of_pure_alcohol continent  
count                     193.000000       193  
unique                           NaN         6  
top                              NaN    Africa  
freq                             NaN        53  
mean                        4.717098       NaN  
std                         3.773298       NaN  
min                         0.000000       NaN  
25%                         1.300000       NaN  
50%                         4.200000       NaN  
75%                         7.200000       NaN  
max                        14.400000       NaN 
'''
print(drinks.describe(include=["object", "float64"]))
'''
        country  total_litres_of_pure_alcohol continent
count       193                    193.000000       193
unique      193                           NaN         6
top     Denmark                           NaN    Africa
freq          1                           NaN        53
mean        NaN                      4.717098       NaN
std         NaN                      3.773298       NaN
min         NaN                      0.000000       NaN
25%         NaN                      1.300000       NaN
50%         NaN                      4.200000       NaN
75%         NaN                      7.200000       NaN
max         NaN                     14.400000       NaN
'''
print(drinks.describe(include=["int8", "float64"]))
'''
        country  total_litres_of_pure_alcohol continent
count       193                    193.000000       193
unique      193                           NaN         6
top     Senegal                           NaN    Africa
freq          1                           NaN        53
mean        NaN                      4.717098       NaN
std         NaN                      3.773298       NaN
min         NaN                      0.000000       NaN
25%         NaN                      1.300000       NaN
50%         NaN                      4.200000       NaN
75%         NaN                      7.200000       NaN
max         NaN                     14.400000       NaN
       total_litres_of_pure_alcohol
count                    193.000000
mean                       4.717098
std                        3.773298
min                        0.000000
25%                        1.300000
50%                        4.200000
75%                        7.200000
max                       14.400000
'''

#How do I use the "axis" parameter in pandas?
#Axis 0 is the row axis.  Axis 1 is the column axis.
drinks = pd.read_csv("http://bit.ly/drinksbycountry")
print(drinks.head())
'''
       country  beer_servings  spirit_servings  wine_servings  \
0  Afghanistan              0                0              0   
1      Albania             89              132             54   
2      Algeria             25                0             14   
3      Andorra            245              138            312   
4       Angola            217               57             45   

   total_litres_of_pure_alcohol continent  
0                           0.0      Asia  
1                           4.9    Europe  
2                           0.7    Africa  
3                          12.4    Europe  
4                           5.9    Africa  
'''
removecontinentcolumn = drinks.drop("continent", axis=1)
print(removecontinentcolumn.head())
'''
       country  beer_servings  spirit_servings  wine_servings  \
0  Afghanistan              0                0              0   
1      Albania             89              132             54   
2      Algeria             25                0             14   
3      Andorra            245              138            312   
4       Angola            217               57             45   

   total_litres_of_pure_alcohol  
0                           0.0  
1                           4.9  
2                           0.7  
3                          12.4  
4                           5.9  
'''
removerowtwo = drinks.drop(2, axis=0)
print(removerowtwo.head())
'''
             country  beer_servings  spirit_servings  wine_servings  \
0        Afghanistan              0                0              0   
1            Albania             89              132             54   
3            Andorra            245              138            312   
4             Angola            217               57             45   
5  Antigua & Barbuda            102              128             45   

   total_litres_of_pure_alcohol      continent  
0                           0.0           Asia  
1                           4.9         Europe  
3                          12.4         Europe  
4                           5.9         Africa  
5                           4.9  North America  
'''
print(drinks.mean(axis=0))  #RM:  confusing Axis 0 is row for removing which is default.  Axis 0 is the column for calculation.  Calculating the mean by column for numerical columns.  axis="index" is valid.
'''
beer_servings                   106.160622
spirit_servings                  80.994819
wine_servings                    49.450777
total_litres_of_pure_alcohol      4.717098
dtype: float64
'''
print(drinks.mean(axis=1)) #RM:  confusing Axis 1 is column for removing.  Axis 1 is the row for calculation.  Calculating the mean by column for numerical columns.  axis="columns" is valid.
'''
0        0.000
1       69.975
2        9.925
3      176.850
4       81.225
5       69.975
'''

#How do I use string methods in pandas-bofaC0IckHo
import pandas as pd
orders = pd.read_table("http://bit.ly/chiporders") #Chipotle orders
print(orders.head())
'''
   order_id  quantity                              item_name  \
0         1         1           Chips and Fresh Tomato Salsa   
1         1         1                                   Izze   
2         1         1                       Nantucket Nectar   
3         1         1  Chips and Tomatillo-Green Chili Salsa   
4         2         2                           Chicken Bowl   

                                  choice_description item_price  
0                                                NaN     $2.39   
1                                       [Clementine]     $3.39   
2                                            [Apple]     $3.39   
3                                                NaN     $2.39   
4  [Tomatillo-Red Chili Salsa (Hot), [Black Beans...    $16.98  
'''
print(orders.item_name.str.upper().head())
'''
0             CHIPS AND FRESH TOMATO SALSA
1                                     IZZE
2                         NANTUCKET NECTAR
3    CHIPS AND TOMATILLO-GREEN CHILI SALSA
4                             CHICKEN BOWL
Name: item_name, dtype: object
'''
print(orders.item_name.str.contains("Chicken").head())
'''
0    False
1    False
2    False
3    False
4     True
Name: item_name, dtype: bool
'''
print(orders[orders.item_name.str.contains("Chicken")]) #Filter orders data frame Chicken in item_name column
'''
     order_id  quantity             item_name  \
4            2         2          Chicken Bowl   
5            3         1          Chicken Bowl   
11           6         1  Chicken Crispy Tacos   
12           6         1    Chicken Soft Tacos   
13           7         1          Chicken Bowl   
...
'''
#https://pandas.pydata.org/pandas-docs/stable/reference/index.html API Reference Guide https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.str.html?highlight=series%20str#

print(orders.choice_description.str.replace("[", "").str.replace("]", "")) #remove brackets in choice_description column
'''
0                                                     NaN
1                                              Clementine
2                                                   Apple
3                                                     NaN
4       Tomatillo-Red Chili Salsa (Hot), Black Beans, ...
'''

#How do I change the data type of a pandas Series-V0AWyzVMf54
import pandas as pd
drinks = pd.read_csv("http://bit.ly/drinksbycountry")
print(drinks.head())
'''
       country  beer_servings  spirit_servings  wine_servings  \
0  Afghanistan              0                0              0   
1      Albania             89              132             54   
2      Algeria             25                0             14   
3      Andorra            245              138            312   
4       Angola            217               57             45   

   total_litres_of_pure_alcohol continent  
0                           0.0      Asia  
1                           4.9    Europe  
2                           0.7    Africa  
3                          12.4    Europe  
4                           5.9    Africa  
'''
print(drinks.dtypes)
'''
country                          object
beer_servings                     int64
spirit_servings                   int64
wine_servings                     int64
total_litres_of_pure_alcohol    float64
continent                        object
dtype: object
'''
drinks["beer_servings"] = drinks.beer_servings.astype(float)  #change data type beer_servings column from int64 to float
print(drinks.dtypes)
'''
country                          object
beer_servings                   float64
spirit_servings                   int64
wine_servings                     int64
total_litres_of_pure_alcohol    float64
continent                        object
dtype: object
'''
drinkschangedatatype = pd.read_csv("http://bit.ly/drinksbycountry", dtype={"beer_servings": float})
print(drinkschangedatatype.dtypes)
'''
country                          object
beer_servings                   float64
spirit_servings                   int64
wine_servings                     int64
total_litres_of_pure_alcohol    float64
continent                        object
dtype: object
'''
orders = pd.read_table("http://bit.ly/chiporders")
print(orders.head())
'''
   order_id  quantity                              item_name  \
0         1         1           Chips and Fresh Tomato Salsa   
1         1         1                                   Izze   
2         1         1                       Nantucket Nectar   
3         1         1  Chips and Tomatillo-Green Chili Salsa   
4         2         2                           Chicken Bowl   

                                  choice_description item_price  
0                                                NaN     $2.39   
1                                       [Clementine]     $3.39   
2                                            [Apple]     $3.39   
3                                                NaN     $2.39   
4  [Tomatillo-Red Chili Salsa (Hot), [Black Beans...    $16.98  
'''
print(orders.dtypes)
'''
order_id               int64
quantity               int64
item_name             object
choice_description    object
item_price            object
dtype: object
'''
orders["item_price"] = orders.item_price.str.replace("$", "")
print(orders.head())
'''
   order_id  quantity                              item_name  \
0         1         1           Chips and Fresh Tomato Salsa   
1         1         1                                   Izze   
2         1         1                       Nantucket Nectar   
3         1         1  Chips and Tomatillo-Green Chili Salsa   
4         2         2                           Chicken Bowl   

                                  choice_description item_price  
0                                                NaN      2.39   
1                                       [Clementine]      3.39   
2                                            [Apple]      3.39   
3                                                NaN      2.39   
4  [Tomatillo-Red Chili Salsa (Hot), [Black Beans...     16.98  
'''
print(orders.dtypes)
'''
order_id               int64
quantity               int64
item_name             object
choice_description    object
item_price            object
dtype: object
'''
orders["item_price"] = orders.item_price.astype(float)
print(orders.dtypes)
'''
order_id                int64
quantity                int64
item_name              object
choice_description     object
item_price            float64
dtype: object
'''
print(orders.item_price.mean()) #print 7.464335785374297
print(orders.item_name.str.contains("Chicken").head())
'''
0    False
1    False
2    False
3    False
4     True
Name: item_name, dtype: bool
'''
print(orders.item_name.str.contains("Chicken").astype(int).head())
'''
0    0
1    0
2    0
3    0
4    1
Name: item_name, dtype: int64
'''

#When should I use a 'groupby' in pandas-qy0fDqoMJx8
import pandas as pd
drinks = pd.read_csv("http://bit.ly/drinksbycountry")
print(drinks.head())
'''
       country  beer_servings  spirit_servings  wine_servings  \
0  Afghanistan              0                0              0   
1      Albania             89              132             54   
2      Algeria             25                0             14   
3      Andorra            245              138            312   
4       Angola            217               57             45   

   total_litres_of_pure_alcohol continent  
0                           0.0      Asia  
1                           4.9    Europe  
2                           0.7    Africa  
3                          12.4    Europe  
4                           5.9    Africa 
'''
averagebeerservings = drinks.beer_servings.mean()
print(averagebeerservings) #print 106.16062176165804
groupbycontinent = drinks.groupby("continent")
print(groupbycontinent.beer_servings.mean())
'''
continent
Africa            61.471698
Asia              37.045455
Europe           193.777778
North America    145.434783
Oceania           89.687500
South America    175.083333
Name: beer_servings, dtype: float64
'''
#print(groupbycontinent.beer_servings.max())
print(groupbycontinent.beer_servings.agg(["count", "min", "max", "mean"]))
'''
               count  min  max        mean
continent                                 
Africa            53    0  376   61.471698
Asia              44    0  247   37.045455
Europe            45    0  361  193.777778
North America     23    1  285  145.434783
Oceania           16    0  306   89.687500
South America     12   93  333  175.083333
'''
print(drinks[drinks.continent == "Africa"])
'''
                      country  beer_servings  spirit_servings  wine_servings  \
2                     Algeria             25                0             14   
4                      Angola            217               57             45   
18                      Benin             34                4             13   
22                   Botswana            173               35             35   
26               Burkina Faso             25                7              7   
27                    Burundi             88                0              0   
28              Cote d'Ivoire             37                1              7   
...
'''
print(drinks[drinks.continent == "Africa"].beer_servings.mean()) #print 61.471698113207545
print(drinks[drinks.continent == "Europe"].beer_servings.mean()) #print 193.77777777777777
groupbycontinentallcolumns = drinks.groupby("continent")
print(groupbycontinentallcolumns.mean())
'''
               beer_servings  spirit_servings  wine_servings  \
continent                                                      
Africa             61.471698        16.339623      16.264151   
Asia               37.045455        60.840909       9.068182   
Europe            193.777778       132.555556     142.222222   
North America     145.434783       165.739130      24.521739   
Oceania            89.687500        58.437500      35.625000   
South America     175.083333       114.750000      62.416667   

               total_litres_of_pure_alcohol  
continent                                    
Africa                             3.007547  
Asia                               2.170455  
Europe                             8.617778  
North America                      5.995652  
Oceania                            3.381250  
South America                      6.308333 
'''

#How do I explore a pandas Series-QTVTq8SPzxM
import pandas as pd
movies = pd.read_csv("http://bit.ly/imdbratings")
print(movies.head())
'''
   star_rating                     title content_rating   genre  duration  \
0          9.3  The Shawshank Redemption              R   Crime       142   
1          9.2             The Godfather              R   Crime       175   
2          9.1    The Godfather: Part II              R   Crime       200   
3          9.0           The Dark Knight          PG-13  Action       152   
4          8.9              Pulp Fiction              R   Crime       154   

                                         actors_list  
0  [u'Tim Robbins', u'Morgan Freeman', u'Bob Gunt...  
1    [u'Marlon Brando', u'Al Pacino', u'James Caan']  
2  [u'Al Pacino', u'Robert De Niro', u'Robert Duv...  
3  [u'Christian Bale', u'Heath Ledger', u'Aaron E...  
4  [u'John Travolta', u'Uma Thurman', u'Samuel L.... 
'''
print(movies.dtypes)
'''
star_rating       float64
title              object
content_rating     object
genre              object
duration            int64
actors_list        object
dtype: object
'''
describecolumninformation = movies.genre.describe()
print(describecolumninformation)
'''
count       979
unique       16
top       Drama
freq        278
Name: genre, dtype: object
'''
valuecountscolumninformation = movies.genre.value_counts()
print(valuecountscolumninformation)
'''
Drama        278
Comedy       156
Action       136
Crime        124
Biography     77
Adventure     75
Animation     62
Horror        29
Mystery       16
Western        9
Sci-Fi         5
Thriller       5
Film-Noir      3
Family         2
History        1
Fantasy        1
Name: genre, dtype: int64
'''
valuecountscolumninformationpercentage = movies.genre.value_counts(normalize=True)
print(valuecountscolumninformationpercentage)
'''
Drama        0.283963
Comedy       0.159346
Action       0.138917
Crime        0.126660
Biography    0.078652
Adventure    0.076609
Animation    0.063330
Horror       0.029622
Mystery      0.016343
Western      0.009193
Sci-Fi       0.005107
Thriller     0.005107
Film-Noir    0.003064
Family       0.002043
History      0.001021
Fantasy      0.001021
Name: genre, dtype: float64
'''
print(type(movies.genre.value_counts(normalize=True))) #print <class 'pandas.core.series.Series'>
print(movies.genre.value_counts(normalize=True).head())
'''
Drama        0.283963
Comedy       0.159346
Action       0.138917
Crime        0.126660
Biography    0.078652
Name: genre, dtype: float64
'''
print(movies.genre.unique()) #print ['Crime' 'Action' 'Drama' 'Western' 'Adventure' 'Biography' 'Comedy''Animation' 'Mystery' 'Horror' 'Film-Noir' 'Sci-Fi' 'History' 'Thriller''Family' 'Fantasy']
print(movies.genre.nunique()) #print 16
pivottablerowcolumncount = pd.crosstab(movies.genre, movies.content_rating)
print(pivottablerowcolumncount)
'''
content_rating  APPROVED   G  GP  NC-17  NOT RATED  PASSED  PG  PG-13    R  \
genre                                                                        
Action                 3   1   1      0          4       1  11     44   67   
Adventure              3   2   0      0          5       1  21     23   17   
Animation              3  20   0      0          3       0  25      5    5   
Biography              1   2   1      0          1       0   6     29   36   
Comedy                 9   2   1      1         16       3  23     23   73   
...
'''
print(movies.duration.describe())
'''
count    979.000000
mean     120.979571
std       26.218010
min       64.000000
25%      102.000000
50%      117.000000
75%      134.000000
max      242.000000
Name: duration, dtype: float64
'''
print(movies.duration.mean()) #print 120.97957099080695
countdurationcolumnvalues = movies.duration.value_counts()
print(countdurationcolumnvalues)
'''
112    23
113    22
102    20
101    20
129    19
120    18
...
'''
