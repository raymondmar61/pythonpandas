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

#How do I handle missing values in pandas-fCMrO_VzeL8
import pandas as pd
ufo = pd.read_csv("http://bit.ly/uforeports")
print(ufo.tail())
'''
              City Colors Reported Shape Reported State              Time
18236   Grant Park             NaN       TRIANGLE    IL  12/31/2000 23:00
18237  Spirit Lake             NaN           DISK    IA  12/31/2000 23:00
18238  Eagle River             NaN            NaN    WI  12/31/2000 23:45
18239  Eagle River             RED          LIGHT    WI  12/31/2000 23:45
18240         Ybor             NaN           OVAL    FL  12/31/2000 23:59
'''
nodatanull = ufo.isnull()
print(nodatanull.tail())
'''
        City  Colors Reported  Shape Reported  State   Time
18236  False             True           False  False  False
18237  False             True           False  False  False
18238  False             True            True  False  False
18239  False            False           False  False  False
18240  False             True           False  False  False
'''
yesdatanotnull = ufo.notnull()
print(yesdatanotnull.tail())
'''
       City  Colors Reported  Shape Reported  State  Time
18236  True            False            True   True  True
18237  True            False            True   True  True
18238  True            False           False   True  True
18239  True             True            True   True  True
18240  True            False            True   True  True
'''
countnullsforeachcolumn = ufo.isnull().sum()
print(countnullsforeachcolumn)  #RM:  If it's null, then True.  True is 1.  Add the true's.  Add the 1's.
'''
City                  25
Colors Reported    15359
Shape Reported      2644
State                  0
Time                   0
dtype: int64
'''
blankcitycolumn = ufo[ufo.City.isnull()]
print(blankcitycolumn)
'''
      City Colors Reported Shape Reported State              Time
21     NaN             NaN            NaN    LA    8/15/1943 0:00
22     NaN             NaN          LIGHT    LA    8/15/1943 0:00
204    NaN             NaN           DISK    CA   7/15/1952 12:30
241    NaN            BLUE           DISK    MT    7/4/1953 14:00
613    NaN             NaN           DISK    NV    7/1/1960 12:00
1877   NaN          YELLOW         CIRCLE    AZ    8/15/1969 1:00
...
'''
removerowifanyvalueismissing = ufo.dropna(how="any")
removerowifallvaluesaremissing = ufo.dropna(how="all")
removerowifcityshapereportedismissing = ufo.dropna(subset=["City", "Shape Reported"], how="any")
removerowifallcityshapereportedaremissing = ufo.dropna(subset=["City", "Shape Reported"], how="all")
countvaluesinshapereportedcolumn = ufo["Shape Reported"].value_counts()
countvaluesandnullinshapereportedcolumn = ufo["Shape Reported"].value_counts(dropna=False)
print(countvaluesandnullinshapereportedcolumn)
'''
LIGHT        2803
NaN          2644
DISK         2122
TRIANGLE     1889
OTHER        1402
CIRCLE       1365
...
'''
print("\n")
replacenullwithvarious = ufo["Shape Reported"].fillna(value="Various", inplace=False)
print(replacenullwithvarious)
'''
...
18234     TRIANGLE
18235      Various
18236     TRIANGLE
18237         DISK
18238      Various
18239        LIGHT
18240         OVAL
Name: Shape Reported, Length: 18241, dtype: object
'''
print(ufo.tail())
'''
              City Colors Reported Shape Reported State              Time
18236   Grant Park             NaN       TRIANGLE    IL  12/31/2000 23:00
18237  Spirit Lake             NaN           DISK    IA  12/31/2000 23:00
18238  Eagle River             NaN            NaN    WI  12/31/2000 23:45
18239  Eagle River             RED          LIGHT    WI  12/31/2000 23:45
18240         Ybor             NaN           OVAL    FL  12/31/2000 23:59
'''
ufo["Shape Reported"].fillna(value="Various", inplace=True) #inplace=True means make the change in the database
print(ufo.tail())
'''
              City Colors Reported Shape Reported State              Time
18236   Grant Park             NaN       TRIANGLE    IL  12/31/2000 23:00
18237  Spirit Lake             NaN           DISK    IA  12/31/2000 23:00
18238  Eagle River             NaN        Various    WI  12/31/2000 23:45
18239  Eagle River             RED          LIGHT    WI  12/31/2000 23:45
18240         Ybor             NaN           OVAL    FL  12/31/2000 23:59
'''

#What do I need to know about the pandas index (Part 1)-OYZNk7Z9s6I
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
print(drinks.index) #print RangeIndex(start=0, stop=193, step=1)
print(drinks.columns) #print Index(['country', 'beer_servings', 'spirit_servings', 'wine_servings', 'total_litres_of_pure_alcohol', 'continent'], dtype='object')
print(drinks.shape) #print (193, 6)
nocolumnheaderseperatorpipe = pd.read_table("http://bit.ly/movieusers", header=None, sep="|")
print(nocolumnheaderseperatorpipe.head())
'''
   0   1  2           3      4
0  1  24  M  technician  85711
1  2  53  F       other  94043
2  3  23  M      writer  32067
3  4  24  M  technician  43537
4  5  33  F       other  15213
'''
continentsouthamerica = drinks[drinks.continent == "South America"]
print(continentsouthamerica.head())
'''
      country  beer_servings  spirit_servings  wine_servings  \
6   Argentina            193               25            221   
20    Bolivia            167               41              8   
23     Brazil            245              145             16   
35      Chile            130              124            172   
37   Colombia            159               76              3   

    total_litres_of_pure_alcohol      continent  
6                            8.3  South America  
20                           3.8  South America  
23                           7.2  South America  
35                           7.6  South America  
37                           4.2  South America 
'''
row23columnbeerservings = drinks.loc[23, "beer_servings"]
print(row23columnbeerservings) #print 245
# indexcolumncountry = drinks.set_index("country", inplace=True)
# print(indexcolumncountry) #print None
drinks.set_index("country", inplace=True) #Use country column as the index
print(drinks.head())
'''
             beer_servings  spirit_servings  wine_servings  \
country                                                      
Afghanistan              0                0              0   
Albania                 89              132             54   
Algeria                 25                0             14   
Andorra                245              138            312   
Angola                 217               57             45   

             total_litres_of_pure_alcohol continent  
country                                              
Afghanistan                           0.0      Asia  
Albania                               4.9    Europe  
Algeria                               0.7    Africa  
Andorra                              12.4    Europe  
Angola                                5.9    Africa  
'''
print(drinks.index)
'''
Index(['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola',
       'Antigua & Barbuda', 'Argentina', 'Armenia', 'Australia', 'Austria',
       ...
       'Tanzania', 'USA', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Venezuela',
       'Vietnam', 'Yemen', 'Zambia', 'Zimbabwe'],
      dtype='object', name='country', length=193)
'''
print(drinks.columns) #print Index(['beer_servings', 'spirit_servings', 'wine_servings', 'total_litres_of_pure_alcohol', 'continent'], dtype='object').  RM:  country column is no longer a column
print(drinks.shape) #print (193, 5)
brazilbeerservings = drinks.loc["Brazil", "beer_servings"]
print(brazilbeerservings) #print 245
drinks.index.name = None #clear the index name
print(drinks.head())
'''
             beer_servings  spirit_servings  wine_servings  \
Afghanistan              0                0              0   
Albania                 89              132             54   
Algeria                 25                0             14   
Andorra                245              138            312   
Angola                 217               57             45   

             total_litres_of_pure_alcohol continent  
Afghanistan                           0.0      Asia  
Albania                               4.9    Europe  
Algeria                               0.7    Africa  
Andorra                              12.4    Europe  
Angola                                5.9    Africa  
'''
drinks.index.name = "country" #Needed to reset index name back to country from drinks.index.name = None
drinks.reset_index(inplace=True) #Set default index default
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
print(drinks.describe().index) #print Index(['count', 'mean', 'std', 'min', '25%', '50%', '75%', 'max'], dtype='object')
print(drinks.describe().columns) #print Index(['beer_servings', 'spirit_servings', 'wine_servings', 'total_litres_of_pure_alcohol'], dtype='object')
print(drinks.describe().loc["25%", "beer_servings"]) #print 20.0

#What do I need to know about the pandas index (Part 1)-OYZNk7Z9s6I
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
continentsdatacolumn = drinks.continent.head()
print(continentsdatacolumn)
'''
0      Asia
1    Europe
2    Africa
3    Europe
4    Africa
Name: continent, dtype: object
'''
drinks.set_index("country", inplace=True)
print(drinks.head())
continentsdatacolumncountryindex = drinks.continent.head()
print(continentsdatacolumncountryindex)
'''
country
Afghanistan      Asia
Albania        Europe
Algeria        Africa
Andorra        Europe
Angola         Africa
Name: continent, dtype: object
'''
print(drinks.continent.value_counts())
'''
Africa           53
Europe           45
Asia             44
North America    23
Oceania          16
South America    12
Name: continent, dtype: int64
'''
print(drinks.continent.value_counts().index) #print Index(['Africa', 'Europe', 'Asia', 'North America', 'Oceania', 'South America'], dtype='object')
print(drinks.continent.value_counts().values) #print [53 45 44 23 16 12]
print(drinks.continent.value_counts()["Africa"]) #print 53
sortcontinentscount = drinks.continent.value_counts().sort_values()
print(sortcontinentscount)
'''
South America    12
Oceania          16
North America    23
Asia             44
Europe           45
Africa           53
Name: continent, dtype: int64
'''
sortcontinentindex = drinks.continent.value_counts().sort_index()
print(sortcontinentindex)
'''
Africa           53
Asia             44
Europe           45
North America    23
Oceania          16
South America    12
Name: continent, dtype: int64
'''
createpandasseries = pd.Series([3000000, 85000], index=["Albania", "Andorra"], name="population")  #RM:  it seems pd.Series good for index column and one data column
print(createpandasseries)
'''
Albania    3000000
Andorra      85000
Name: population, dtype: int64
'''
multipletwodatasetsmatchindex = drinks.beer_servings * createpandasseries
print(multipletwodatasetsmatchindex)
'''
Afghanistan                     NaN
Albania                 267000000.0
Algeria                         NaN
Andorra                  20825000.0
Angola                          NaN
Antigua & Barbuda               NaN
Argentina                       NaN
...
Zambia                          NaN
Zimbabwe                        NaN
Length: 193, dtype: float64
'''
combinetwodatasetsautomaticallymatchindex = pd.concat([drinks, createpandasseries], axis=1)
print(combinetwodatasetsautomaticallymatchindex.head())
'''
             beer_servings  spirit_servings  wine_servings  \
Afghanistan              0                0              0   
Albania                 89              132             54   
Algeria                 25                0             14   
Andorra                245              138            312   
Angola                 217               57             45   

             total_litres_of_pure_alcohol continent  population  
Afghanistan                           0.0      Asia         NaN  
Albania                               4.9    Europe   3000000.0  
Algeria                               0.7    Africa         NaN  
Andorra                              12.4    Europe     85000.0  
Angola                                5.9    Africa         NaN  
'''

#How do I select multiple rows and columns from a pandas DataFrame-xvpNA7bC8cs
ufo = pd.read_csv("http://bit.ly/uforeports")
print(ufo.head(3))
'''
          City Colors Reported Shape Reported State             Time
0       Ithaca             NaN       TRIANGLE    NY   6/1/1930 22:00
1  Willingboro             NaN          OTHER    NJ  6/30/1930 20:00
2      Holyoke             NaN           OVAL    CO  2/15/1931 14:00
'''
#Filter rows by index and filter columns by column name.  .loc(filter row, filter column)  Defualt is .loc(filter row) without comma means all columsn are returned.  loc is inclusive in range numbers.
allcolumnsinrowzero = ufo.loc[0, :]
print(allcolumnsinrowzero)
'''
City                       Ithaca
Colors Reported               NaN
Shape Reported           TRIANGLE
State                          NY
Time               6/1/1930 22:00
Name: 0, dtype: object
'''
firstthreerows = ufo.loc[0:2, :] #ufo.loc[[0, 1, 2], :] also works
print(firstthreerows)
'''
          City Colors Reported Shape Reported State             Time
0       Ithaca             NaN       TRIANGLE    NY   6/1/1930 22:00
1  Willingboro             NaN          OTHER    NJ  6/30/1930 20:00
2      Holyoke             NaN           OVAL    CO  2/15/1931 14:00
'''
citycolumn = ufo.loc[:, "City"]
print(citycolumn.head(6))
'''
0                  Ithaca
1             Willingboro
2                 Holyoke
3                 Abilene
4    New York Worlds Fair
5             Valley City
Name: City, dtype: object
'''
statecitycolumn = ufo.loc[:, ["State", "City"]]
print(statecitycolumn.head(3))
'''
  State         City
0    NY       Ithaca
1    NJ  Willingboro
2    CO      Holyoke
'''
citytostatecolumns = ufo.loc[:, "City":"State"]
print(citytostatecolumns.head(3))
'''
          City Colors Reported Shape Reported State
0       Ithaca             NaN       TRIANGLE    NY
1  Willingboro             NaN          OTHER    NJ
2      Holyoke             NaN           OVAL    CO
'''
citytostatecolumnsthreerows = ufo.loc[0:2, "City":"State"]
print(citytostatecolumnsthreerows)
'''
          City Colors Reported Shape Reported State
0       Ithaca             NaN       TRIANGLE    NY
1  Willingboro             NaN          OTHER    NJ
2      Holyoke             NaN           OVAL    CO
'''
print(ufo[ufo.City == "Oakland"].head(6))
'''
         City Colors Reported Shape Reported State              Time
1694  Oakland             NaN          CIGAR    CA   7/21/1968 14:00
2144  Oakland             NaN           DISK    CA    8/19/1971 0:00
4686  Oakland             NaN          LIGHT    MD     6/1/1982 0:00
7293  Oakland             NaN          LIGHT    CA   3/28/1994 17:00
8488  Oakland             NaN            NaN    CA   8/10/1995 21:45
8768  Oakland             NaN            NaN    CA  10/10/1995 22:40
'''
oaklandcity = ufo.loc[ufo.City == "Oakland", :]
print(oaklandcity.head(6))
'''
         City Colors Reported Shape Reported State              Time
1694  Oakland             NaN          CIGAR    CA   7/21/1968 14:00
2144  Oakland             NaN           DISK    CA    8/19/1971 0:00
4686  Oakland             NaN          LIGHT    MD     6/1/1982 0:00
7293  Oakland             NaN          LIGHT    CA   3/28/1994 17:00
8488  Oakland             NaN            NaN    CA   8/10/1995 21:45
8768  Oakland             NaN            NaN    CA  10/10/1995 22:40
'''
#The i in iloc means integer.  Integer position as index position.  iloc is exclusive for iloc ranges.
firstcolumnandthirdcolumn = ufo.iloc[:, [0, 3]]
print(firstcolumnandthirdcolumn.head(3))
'''
          City State
0       Ithaca    NY
1  Willingboro    NJ
2      Holyoke    CO
'''
firsttofourthcolumn = ufo.iloc[:, 0:4]
print(firsttofourthcolumn.head(3))
'''
          City Colors Reported Shape Reported State
0       Ithaca             NaN       TRIANGLE    NY
1  Willingboro             NaN          OTHER    NJ
2      Holyoke             NaN           OVAL    CO
'''
firsttothirdrows = ufo.iloc[0:3, :]
print(firsttothirdrows)
'''
          City Colors Reported Shape Reported State             Time
0       Ithaca             NaN       TRIANGLE    NY   6/1/1930 22:00
1  Willingboro             NaN          OTHER    NJ  6/30/1930 20:00
2      Holyoke             NaN           OVAL    CO  2/15/1931 14:00
'''
drinks = pd.read_csv("http://bit.ly/drinksbycountry", index_col="country")
print(drinks.head())
'''
             beer_servings  spirit_servings  wine_servings  \
country                                                      
Afghanistan              0                0              0   
Albania                 89              132             54   
Algeria                 25                0             14   
Andorra                245              138            312   
Angola                 217               57             45   

             total_litres_of_pure_alcohol continent  
country                                              
Afghanistan                           0.0      Asia  
Albania                               4.9    Europe  
Algeria                               0.7    Africa  
Andorra                              12.4    Europe  
Angola                                5.9    Africa
'''
#integer as index is treated as labels is inclusive.  RM:  instructor recommends ix as a last resort
albaniabeerservings = drinks.ix["Albania", 0]
print(albaniabeerservings) #print 89
albaniabeerservings = drinks.ix[1, "beer_servings"]
print(albaniabeerservings) #print 89
albaniatoandorrabeerandspirit = drinks.ix["Albania":"Andorra", 0:2]
print(albaniatoandorrabeerandspirit)
'''
         beer_servings  spirit_servings
country                                
Albania             89              132
Algeria             25                0
Andorra            245              138
'''
first3rowsfirst2columns = ufo.ix[0:2, 0:2]
print(first3rowsfirst2columns)
'''
          City Colors Reported
0       Ithaca             NaN
1  Willingboro             NaN
2      Holyoke             NaN
'''

#When should I use the 'inplace' parameter in pandas-XaCSdr7pPmY
ufo = pd.read_csv("http://bit.ly/uforeports")
print(ufo.shape) #print (18241, 5)
print(ufo.head())
'''
                   City Colors Reported Shape Reported State             Time
0                Ithaca             NaN       TRIANGLE    NY   6/1/1930 22:00
1           Willingboro             NaN          OTHER    NJ  6/30/1930 20:00
2               Holyoke             NaN           OVAL    CO  2/15/1931 14:00
3               Abilene             NaN           DISK    KS   6/1/1931 13:00
4  New York Worlds Fair             NaN          LIGHT    NY  4/18/1933 19:00
'''
print(ufo.drop("City", axis=1).head()) #delete column remove column from view.  inplace=False is False by default.
'''
  Colors Reported Shape Reported State             Time
0             NaN       TRIANGLE    NY   6/1/1930 22:00
1             NaN          OTHER    NJ  6/30/1930 20:00
2             NaN           OVAL    CO  2/15/1931 14:00
3             NaN           DISK    KS   6/1/1931 13:00
4             NaN          LIGHT    NY  4/18/1933 19:00
'''
print(ufo.head())  #RM print(ufo.drop("City", axis=1).head()) didn't delete City column permanently.  Reason is drop method inplace=False is False by default.  Method inplace=False means operation doesn't affect the underlying data or underlying source by default.  inplace=True operation does affect the underlying data or underlying source.
'''
                   City Colors Reported Shape Reported State             Time
0                Ithaca             NaN       TRIANGLE    NY   6/1/1930 22:00
1           Willingboro             NaN          OTHER    NJ  6/30/1930 20:00
2               Holyoke             NaN           OVAL    CO  2/15/1931 14:00
3               Abilene             NaN           DISK    KS   6/1/1931 13:00
4  New York Worlds Fair             NaN          LIGHT    NY  4/18/1933 19:00
'''
inplacetrue = ufo.drop("City", axis=1, inplace=True)
print(inplacetrue) #print None
#print(inplacetrue.head()) #print AttributeError: 'NoneType' object has no attribute 'head'
#RM:  I looked at past YouTube videos.  Quick search I didn't find any .drop saved to a variable.
ufodeletecitycolumn = pd.read_csv("http://bit.ly/uforeports")
ufodeletecitycolumn.drop("City", axis=1, inplace=True)
print(ufodeletecitycolumn.head())
'''
  Colors Reported Shape Reported State             Time
0             NaN       TRIANGLE    NY   6/1/1930 22:00
1             NaN          OTHER    NJ  6/30/1930 20:00
2             NaN           OVAL    CO  2/15/1931 14:00
3             NaN           DISK    KS   6/1/1931 13:00
4             NaN          LIGHT    NY  4/18/1933 19:00
'''
dropnarows = ufodeletecitycolumn.dropna(how="any") #delete rows with na value NaN value
print(dropnarows.head())
'''
   Colors Reported Shape Reported State             Time
12             RED         SPHERE    SC  6/30/1939 20:00
19             RED          OTHER    AK  4/30/1943 23:00
36             RED      FORMATION    VA   7/10/1945 1:30
44           GREEN         SPHERE    CA  6/30/1946 19:00
82            BLUE        CHEVRON    CA  7/15/1947 21:00
'''
print(ufodeletecitycolumn.dropna(how="any").shape) #print (2490, 4)  #RM:  not saving delete rows with na value NaN value to a variable.  Also inplace=False is default
print(ufodeletecitycolumn.shape) #print (18241, 4) #RM:  inplace=False is default delete rows with na value NaN value didn't permanently affect the data source
#Other Pandas with inplace=False default are .rename(), .sort_values(), .set_index()
#RM:  instructor assigns a variable or an assignment statement which is what I do.  One less worry to change inplace=False to inplace=True.  Instructor says possible bigger file size and slower performance for huge data sets.  inplace=True no guarantee more efficient performance.
assignvariablesetindextotime = ufodeletecitycolumn.set_index("Time")
print(assignvariablesetindextotime.tail())
'''
                 Colors Reported Shape Reported State
Time                                                 
12/31/2000 23:00             NaN       TRIANGLE    IL
12/31/2000 23:00             NaN           DISK    IA
12/31/2000 23:45             NaN            NaN    WI
12/31/2000 23:45             RED          LIGHT    WI
12/31/2000 23:59             NaN           OVAL    FL
'''
#Bonus tip.  Take advantage of inplace=False is default for exploring Pandas methods.  Experiment.  Trial and error.

#How do I make my pandas DataFrame smaller and faster-wDYDYGyN_cw
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
print(drinks.info())
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 193 entries, 0 to 192
Data columns (total 6 columns):
country                         193 non-null object
beer_servings                   193 non-null int64
spirit_servings                 193 non-null int64
wine_servings                   193 non-null int64
total_litres_of_pure_alcohol    193 non-null float64
continent                       193 non-null object
dtypes: float64(1), int64(3), object(2)
memory usage: 9.1+ KB
None
'''
actualmemorysize = drinks.info(memory_usage="deep")
print(actualmemorysize)
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 193 entries, 0 to 192
Data columns (total 6 columns):
country                         193 non-null object
beer_servings                   193 non-null int64
spirit_servings                 193 non-null int64
wine_servings                   193 non-null int64
total_litres_of_pure_alcohol    193 non-null float64
continent                       193 non-null object
dtypes: float64(1), int64(3), object(2)
memory usage: 30.4 KB
None
'''
print(drinks.memory_usage())
'''
Index                             80
country                         1544
beer_servings                   1544
spirit_servings                 1544
wine_servings                   1544
total_litres_of_pure_alcohol    1544
continent                       1544
dtype: int64
'''
actualmemorysizecolumns = drinks.memory_usage(deep=True)
print(actualmemorysizecolumns)
'''
Index                              80
country                         12588
beer_servings                    1544
spirit_servings                  1544
wine_servings                    1544
total_litres_of_pure_alcohol     1544
continent                       12332
dtype: int64
'''
print(actualmemorysizecolumns.sum()) #print 31176
#How do we reduce the file size?  Convert strings to integers.  Let's see the continent column.
uniquecontinents = sorted(drinks.continent.unique())
print(uniquecontinents) #print ['Africa', 'Asia', 'Europe', 'North America', 'Oceania', 'South America']
#Assign an integer to the continent.  Like  a lookup table.
drinks["continent"] = drinks.continent.astype("category") #Convert continent column datatype from object to category to reduce memeory size and assign an integer to continent values
print(drinks.dtypes)
'''
country                           object
beer_servings                      int64
spirit_servings                    int64
wine_servings                      int64
total_litres_of_pure_alcohol     float64
continent                       category
dtype: object
'''
print(drinks.continent.head())
'''
0      Asia
1    Europe
2    Africa
3    Europe
4    Africa
Name: continent, dtype: category
Categories (6, object): [Africa, Asia, Europe, North America, Oceania, South America]
'''
proofcontinentisintegers = drinks.continent.cat.codes.head()
print(proofcontinentisintegers)
'''
0    1
1    2
2    0
3    2
4    0
dtype: int8
'''
print(drinks.memory_usage(deep=True))  #continent memory size reduced from 12332 to 744
'''
Index                              80
country                         12588
beer_servings                    1544
spirit_servings                  1544
wine_servings                    1544
total_litres_of_pure_alcohol     1544
continent                         744
dtype: int64
'''
drinks["country"] = drinks.country.astype("category") #Convert country column datatype from object to category to reduce memeory size and assign an integer to country values
print(drinks.memory_usage(deep=True))  #country memory size increased from 12588 to 18094.  Reason is the category as a lookup table there are too many values in country column.
'''
Index                              80
country                         18094
beer_servings                    1544
spirit_servings                  1544
wine_servings                    1544
total_litres_of_pure_alcohol     1544
continent                         744
dtype: int64

'''
bonusdataframe = pd.DataFrame({"ID": [100, 101, 102, 103], "quality": ["good", "very good", "good", "excellent"]})
print(bonusdataframe)
'''
    ID    quality
0  100       good
1  101  very good
2  102       good
3  103  excellent
'''
sortbonusdataframequality = bonusdataframe.sort_values("quality")
print(sortbonusdataframequality)
'''
    ID    quality
3  103  excellent
0  100       good
2  102       good
1  101  very good
'''
bonusdataframe["quality"] = bonusdataframe.quality.astype("category", categories=["good", "very good", "excellent"], ordered=True) #Convert quality column datatype from object to category to custom sort
'''
yywork.py:152: FutureWarning: specifying 'categories' or 'ordered' in .astype() is deprecated; pass a CategoricalDtype instead
  bonusdataframe["quality"] = bonusdataframe.quality.astype("category", categories=["good", "very good", "excellent"], ordered=True) #Convert quality column datatype from object to category to custom sort
'''
print(bonusdataframe)
'''
    ID    quality
0  100       good
1  101  very good
2  102       good
3  103  excellent
'''
print(bonusdataframe.quality) #Confirm use comparison operators for string comparison operators
'''
0         good
1    very good
2         good
3    excellent
Name: quality, dtype: category
Categories (3, object): [good < very good < excellent]
'''
printcustomsortqualitycolumn = bonusdataframe.sort_values("quality")
print(printcustomsortqualitycolumn)
'''
    ID    quality
0  100       good
2  102       good
1  101  very good
3  103  excellent
'''
returncolumnsgreaterthangood = bonusdataframe.loc[bonusdataframe.quality > "good", :]
print(returncolumnsgreaterthangood)
'''
    ID    quality
1  101  very good
3  103  excellent
'''

#How do I use pandas with scikit-learn to create Kaggle submissions-ylRlGCtAtiE
titanicdata = pd.read_csv("http://bit.ly/kaggletrain")
print(titanicdata.head())
'''
   PassengerId  Survived  Pclass  \
0            1         0       3   
1            2         1       1   
2            3         1       3   
3            4         1       1   
4            5         0       3   

                                                Name     Sex   Age  SibSp  \
0                            Braund, Mr. Owen Harris    male  22.0      1   
1  Cumings, Mrs. John Bradley (Florence Briggs Th...  female  38.0      1   
2                             Heikkinen, Miss. Laina  female  26.0      0   
3       Futrelle, Mrs. Jacques Heath (Lily May Peel)  female  35.0      1   
4                           Allen, Mr. William Henry    male  35.0      0   

   Parch            Ticket     Fare Cabin Embarked  
0      0         A/5 21171   7.2500   NaN        S  
1      0          PC 17599  71.2833   C85        C  
2      0  STON/O2. 3101282   7.9250   NaN        S  
3      0            113803  53.1000  C123        S  
4      0            373450   8.0500   NaN        S 
'''
featurecolumns = ["Pclass", "Parch"]
x = titanicdata.loc[:, featurecolumns]  #all rows from Pclass column and Parch column in featurecolumns list
print(x.shape) #print (891, 2)
survivors = titanicdata.Survived
print(survivors.shape) #print (891,)
# from sklearn.linear_model import LogisticRegression
# logreg = LogisticRegression()
# logreg.fit(x, survivors)
# print(logreg.fit(x, survivors))
#RM:  I don't have sklearn.linear_model

#More of your pandas questions answered!-oH3wYKvwpJ8

#How do you read the pandas documentation.  YouTuber says Google it instead of going to the Pandas documents and searching there.  Search Pandas *function* in Google; for example, pandas read_csv.  Make sure choose the function with the latest version.  If you see a function pandas.read_csv, it's a top level function.  You type pd.read_csv to run the read_csv function.  The code inside the parenthesis is the parameters.  Parameters without a default value means these parameters are required.
#Another example is search for pandas drop.  pandas.DataFrame.drop is the top Google result.  If you see a pandas.DataFrame, it means the drop is a data frame method.  For example, pandas.ufo.drop for which ufo is a data frame.  Not pd.drop.  Similarily, search pandas value_counts.  pandas.Series.value_counts is the top Google result.  value_counts is a series method.

#ufo.isnull() and pd.isnull(ufo) returns the same results.  ufo.isnull() is calling a function of ufo object.  pd.isnull(ufo) uses ufo object as an argument.  pd.isnull(obj) is a top level function which takes an object as its argument.  isnull() is also a series method as Series.isnull() for which ufo is a series ufo.isnull().  isnull() is also a data frame method as DataFrame.isnull() for which ufo is a data frame ufo.isnull().  There are different ways to use isnull() as a top level method, data frame method, or series method.
ufo = pd.read_csv("http://bit.ly/uforeports")
print(ufo.head())
'''
                   City Colors Reported Shape Reported State             Time
0                Ithaca             NaN       TRIANGLE    NY   6/1/1930 22:00
1           Willingboro             NaN          OTHER    NJ  6/30/1930 20:00
2               Holyoke             NaN           OVAL    CO  2/15/1931 14:00
3               Abilene             NaN           DISK    KS   6/1/1931 13:00
4  New York Worlds Fair             NaN          LIGHT    NY  4/18/1933 19:00
'''
print(pd.isnull(ufo).head())  #RM:  ufo is using isnull() as a top level function
'''
    City  Colors Reported  Shape Reported  State   Time
0  False             True           False  False  False
1  False             True           False  False  False
2  False             True           False  False  False
3  False             True           False  False  False
4  False             True           False  False  False
'''
print(ufo.isnull().head())  #RM:  ufo is using isnull() as a method
'''
    City  Colors Reported  Shape Reported  State   Time
0  False             True           False  False  False
1  False             True           False  False  False
2  False             True           False  False  False
3  False             True           False  False  False
4  False             True           False  False  False
'''

#Inclusive ranges and exclusive ranges.  0:4 is different in loc and iloc.
print(ufo.loc[0:4, :])  #print the first 5 rows and all columns.  Label-based indexing is inclusive.
'''
                   City Colors Reported Shape Reported State             Time
0                Ithaca             NaN       TRIANGLE    NY   6/1/1930 22:00
1           Willingboro             NaN          OTHER    NJ  6/30/1930 20:00
2               Holyoke             NaN           OVAL    CO  2/15/1931 14:00
3               Abilene             NaN           DISK    KS   6/1/1931 13:00
4  New York Worlds Fair             NaN          LIGHT    NY  4/18/1933 19:00
'''
print(ufo.iloc[0:4, :])  #print the first 4 rows and all columns.  iloc integer location.  Slicing copied from Numpy.  Positional-based indexing is exclusive.
'''
                   City Colors Reported Shape Reported State             Time
0                Ithaca             NaN       TRIANGLE    NY   6/1/1930 22:00
1           Willingboro             NaN          OTHER    NJ  6/30/1930 20:00
2               Holyoke             NaN           OVAL    CO  2/15/1931 14:00
3               Abilene             NaN           DISK    KS   6/1/1931 13:00
'''
print(ufo.loc[:, "City":"State"].head())
'''
                   City Colors Reported Shape Reported State
0                Ithaca             NaN       TRIANGLE    NY
1           Willingboro             NaN          OTHER    NJ
2               Holyoke             NaN           OVAL    CO
3               Abilene             NaN           DISK    KS
4  New York Worlds Fair             NaN          LIGHT    NY
'''
print(ufo.iloc[:, 0:4].head())  #iloc integer location.  Slicing copied from Numpy.
'''
                   City Colors Reported Shape Reported State
0                Ithaca             NaN       TRIANGLE    NY
1           Willingboro             NaN          OTHER    NJ
2               Holyoke             NaN           OVAL    CO
3               Abilene             NaN           DISK    KS
4  New York Worlds Fair             NaN          LIGHT    NY
'''

#Random sampling
threerandomrows = ufo.sample(n=3)
print(threerandomrows)
'''
                  City Colors Reported Shape Reported State              Time
14887  Apache Junction             NaN          OTHER    AZ  10/19/1999 22:00
12493           Novato           GREEN       FIREBALL    CA   11/4/1998 22:32
14147           Denver             NaN          OTHER    CO   8/10/1999 22:30
'''
randomstate = ufo.sample(n=3, random_state=42)  #random_state is a reproducibility.  Everytime code is run, the results are the same.  reproducibility is the ability to be reproduced or copied.
print(randomstate)
'''
            City Colors Reported Shape Reported State             Time
10201  Oceanside          ORANGE          OTHER    CA   5/2/1997 22:00
11407  Whitefish             NaN            NaN    MT  4/12/1998 23:00
10342     Renton             NaN           DISK    WA   6/8/1997 19:16
'''
fractionrows = ufo.sample(frac=0.75, random_state=99)
print(fractionrows)  #print 75% of the total rows
'''
                    City Colors Reported Shape Reported State  \
6250           Sunnyvale             NaN          OTHER    CA   
8656      Corpus Christi             NaN            NaN    TX   
2729              Mentor             NaN           DISK    OH   
7348              Wilson             NaN          LIGHT    WI   
12637             Lowell             NaN         CIRCLE    MA
...   
      Time  
6250    12/16/1989 0:00  
8656     9/13/1995 0:10  
2729     8/8/1974 10:00  
7348      6/1/1994 1:00  
12637  11/26/1998 10:00  
'''

#How do I create dummy variables in pandas-0s_1IsROgDc
#Dummy variables used in machine learning, statistics, and econometrics.  Used as indicator variables.  For example, male is 1, female is 0.  1 and 0 are dummy variables.  In machine learning, dummy variables are used for unordered categorical features.
trainingdatasettitanic = pd.read_csv("http://bit.ly/kaggletrain")
print(trainingdatasettitanic.head())
'''
   PassengerId  Survived  Pclass  \
0            1         0       3   
1            2         1       1   
2            3         1       3   
3            4         1       1   
4            5         0       3   

                                                Name     Sex   Age  SibSp  \
0                            Braund, Mr. Owen Harris    male  22.0      1   
1  Cumings, Mrs. John Bradley (Florence Briggs Th...  female  38.0      1   
2                             Heikkinen, Miss. Laina  female  26.0      0   
3       Futrelle, Mrs. Jacques Heath (Lily May Peel)  female  35.0      1   
4                           Allen, Mr. William Henry    male  35.0      0   

   Parch            Ticket     Fare Cabin Embarked  
0      0         A/5 21171   7.2500   NaN        S  
1      0          PC 17599  71.2833   C85        C  
2      0  STON/O2. 3101282   7.9250   NaN        S  
3      0            113803  53.1000  C123        S  
4      0            373450   8.0500   NaN        S 
'''
trainingdatasettitanic["Sexmale"] = trainingdatasettitanic.Sex.map({"female": 0, "male": 1})  #new column Sexmale assign or map female to 0 and male to 1
print(trainingdatasettitanic.head())
'''
   PassengerId  Survived  Pclass  \
0            1         0       3   
1            2         1       1   
2            3         1       3   
3            4         1       1   
4            5         0       3   

                                                Name     Sex   Age  SibSp  \
0                            Braund, Mr. Owen Harris    male  22.0      1   
1  Cumings, Mrs. John Bradley (Florence Briggs Th...  female  38.0      1   
2                             Heikkinen, Miss. Laina  female  26.0      0   
3       Futrelle, Mrs. Jacques Heath (Lily May Peel)  female  35.0      1   
4                           Allen, Mr. William Henry    male  35.0      0   

   Parch            Ticket     Fare Cabin Embarked  Sexmale  
0      0         A/5 21171   7.2500   NaN        S        1  
1      0          PC 17599  71.2833   C85        C        0  
2      0  STON/O2. 3101282   7.9250   NaN        S        0  
3      0            113803  53.1000  C123        S        0  
4      0            373450   8.0500   NaN        S        1  
'''
getdummiestoplevel = pd.get_dummies(trainingdatasettitanic.Sex)  #Faster method to assign or map a column of results.  Create one column for every possible value.  There are two possible values.  One column for each.  For each row, it tells you whether it was female or male putting a one in the appropriate column.
print(getdummiestoplevel)
'''
     female  male
0         0     1
1         1     0
2         1     0
3         1     0
4         0     1
...
'''
#Generally speaking, if we have k possible values for a categorial variable. we use k-1.  Want k-1 columns for pd.get_dummies or k-1 dummy variables.  Because it captures all possible information; in other words, we don't need all possible values to return.  If we get all zeroes in a row of columns, then we know the column which is one.  Drop the first column.  Don't need it.  Define the baseline.
kminusonedropfirstcolumn = pd.get_dummies(trainingdatasettitanic.Sex, prefix="Columnnameprefix").iloc[:, 1:]
print(kminusonedropfirstcolumn)
'''
   Columnnameprefix_male
0       1
1       0
2       0
3       0
4       1
...
'''
valuecountembarked = trainingdatasettitanic.Embarked.value_counts()
print(valuecountembarked)
'''
S    644
C    168
Q     77
Name: Embarked, dtype: int64
'''
assigndummyvariablestoembarked = pd.get_dummies(trainingdatasettitanic.Embarked, prefix="Embarkedcolumn")
print(assigndummyvariablestoembarked)
'''
  Embarkedcolumn_C  Embarkedcolumn_Q  Embarkedcolumn_S
0                   0                 0                 1
1                   1                 0                 0
2                   0                 0                 1
3                   0                 0                 1
4                   0                 0                 1
...
'''
kminusoneassigndummyvariablestoembarked = pd.get_dummies(trainingdatasettitanic.Embarked, prefix="Embarkedcolumn").iloc[:, 1:]  #Embarkedcolumn_C or C result is the baseline.  In other words, if Embarkedcolumn_Q and Embarkedcolumn_S are 0, then Embarkedcolumn_C is 1 like index row 1.
print(kminusoneassigndummyvariablestoembarked)
'''
    Embarkedcolumn_Q  Embarkedcolumn_S
0                   0                 1
1                   0                 0
2                   0                 1
3                   0                 1
4                   0                 1
'''
trainingdatasettitanic = pd.concat([trainingdatasettitanic, kminusoneassigndummyvariablestoembarked], axis=1)  #add column kminusoneassigndummyvariablestoembarked to trainingdatasettitanic and overwrite original trainingdatasettitanic
print(trainingdatasettitanic.head())
'''
   PassengerId  Survived  Pclass  \
0            1         0       3   
1            2         1       1   
2            3         1       3   
3            4         1       1   
4            5         0       3   

                                                Name     Sex   Age  SibSp  \
0                            Braund, Mr. Owen Harris    male  22.0      1   
1  Cumings, Mrs. John Bradley (Florence Briggs Th...  female  38.0      1   
2                             Heikkinen, Miss. Laina  female  26.0      0   
3       Futrelle, Mrs. Jacques Heath (Lily May Peel)  female  35.0      1   
4                           Allen, Mr. William Henry    male  35.0      0   

   Parch            Ticket     Fare Cabin Embarked  Sexmale  Embarkedcolumn_Q  \
0      0         A/5 21171   7.2500   NaN        S        1                 0   
1      0          PC 17599  71.2833   C85        C        0                 0   
2      0  STON/O2. 3101282   7.9250   NaN        S        0                 0   
3      0            113803  53.1000  C123        S        0                 0   
4      0            373450   8.0500   NaN        S        1                 0   

   Embarkedcolumn_S  
0                 1  
1                 0  
2                 1  
3                 1  
4                 1  
...
'''
trainingdatasettitanic = pd.read_csv("http://bit.ly/kaggletrain")
print(trainingdatasettitanic.head())
passdataframetogetdummies = pd.get_dummies(trainingdatasettitanic, columns=["Sex", "Embarked"])
print(passdataframetogetdummies.head())
'''
   PassengerId  Survived  Pclass  \
0            1         0       3   
1            2         1       1   
2            3         1       3   
3            4         1       1   
4            5         0       3   

                                                Name   Age  SibSp  Parch  \
0                            Braund, Mr. Owen Harris  22.0      1      0   
1  Cumings, Mrs. John Bradley (Florence Briggs Th...  38.0      1      0   
2                             Heikkinen, Miss. Laina  26.0      0      0   
3       Futrelle, Mrs. Jacques Heath (Lily May Peel)  35.0      1      0   
4                           Allen, Mr. William Henry  35.0      0      0   

             Ticket     Fare Cabin  Sex_female  Sex_male  Embarked_C  \
0         A/5 21171   7.2500   NaN           0         1           0   
1          PC 17599  71.2833   C85           1         0           1   
2  STON/O2. 3101282   7.9250   NaN           1         0           0   
3            113803  53.1000  C123           1         0           0   
4            373450   8.0500   NaN           0         1           0   

   Embarked_Q  Embarked_S  
0           0           1  
1           0           0  
2           0           1  
3           0           1  
4           0           1
...
'''
kminusonepassdataframetogetdummies = pd.get_dummies(trainingdatasettitanic, columns=["Sex", "Embarked"], drop_first=True)
print(kminusonepassdataframetogetdummies.head())
'''
   PassengerId  Survived  Pclass  \
0            1         0       3   
1            2         1       1   
2            3         1       3   
3            4         1       1   
4            5         0       3   

                                                Name   Age  SibSp  Parch  \
0                            Braund, Mr. Owen Harris  22.0      1      0   
1  Cumings, Mrs. John Bradley (Florence Briggs Th...  38.0      1      0   
2                             Heikkinen, Miss. Laina  26.0      0      0   
3       Futrelle, Mrs. Jacques Heath (Lily May Peel)  35.0      1      0   
4                           Allen, Mr. William Henry  35.0      0      0   

             Ticket     Fare Cabin  Sex_male  Embarked_Q  Embarked_S  
0         A/5 21171   7.2500   NaN         1           0           1  
1          PC 17599  71.2833   C85         0           0           0  
2  STON/O2. 3101282   7.9250   NaN         0           0           1  
3            113803  53.1000  C123         0           0           1  
4            373450   8.0500   NaN         1           0           1 
...
'''

#How do I work with dates and times in pandas-yCgJGsg0Xa4
ufo = pd.read_csv("http://bit.ly/uforeports")
print(ufo.head())
'''
                   City Colors Reported Shape Reported State             Time
0                Ithaca             NaN       TRIANGLE    NY   6/1/1930 22:00
1           Willingboro             NaN          OTHER    NJ  6/30/1930 20:00
2               Holyoke             NaN           OVAL    CO  2/15/1931 14:00
3               Abilene             NaN           DISK    KS   6/1/1931 13:00
4  New York Worlds Fair             NaN          LIGHT    NY  4/18/1933 19:00
...
'''
print(ufo.dtypes)
'''
City               object
Colors Reported    object
Shape Reported     object
State              object
Time               object
dtype: object
'''
print(ufo.Time.str.slice(-5, -3).head())
'''
0    22
1    20
2    14
3    13
4    19
Name: Time, dtype: object
'''
print(ufo.Time.str.slice(-5, -3).astype(int).head())
'''
0    22
1    20
2    14
3    13
4    19
Name: Time, dtype: int64
'''
uforeplacetimecolumnnewnewnametimecolumn = pd.read_csv("http://bit.ly/uforeports")
uforeplacetimecolumnnewnewnametimecolumn["Newnametimecolumn"] = uforeplacetimecolumnnewnewnametimecolumn["Time"]
uforeplacetimecolumnnewnewnametimecolumn["Newnametimecolumn"] = pd.to_datetime(uforeplacetimecolumnnewnewnametimecolumn.Newnametimecolumn)
print(uforeplacetimecolumnnewnewnametimecolumn.head())
'''
                   City Colors Reported Shape Reported State  \
0                Ithaca             NaN       TRIANGLE    NY   
1           Willingboro             NaN          OTHER    NJ   
2               Holyoke             NaN           OVAL    CO   
3               Abilene             NaN           DISK    KS   
4  New York Worlds Fair             NaN          LIGHT    NY   

                 Newnametimecolumn  
0 1930-06-01 22:00:00  
1 1930-06-30 20:00:00  
2 1931-02-15 14:00:00  
3 1931-06-01 13:00:00  
4 1933-04-18 19:00:00  
...
'''
print(uforeplacetimecolumnnewnewnametimecolumn.dtypes)
'''
City                       object
Colors Reported            object
Shape Reported             object
State                      object
Newnametimecolumn          datetime64[ns]
dtype: object
'''
extracthour = uforeplacetimecolumnnewnewnametimecolumn.Newnametimecolumn.dt.hour
print(extracthour.head())
'''
0    22
1    20
2    14
3    13
4    19
Name: Newnametimecolumn, dtype: int64
'''
extractweekdayasname = uforeplacetimecolumnnewnewnametimecolumn.Newnametimecolumn.dt.weekday_name
print(extractweekdayasname.head())
'''
0     Sunday
1     Monday
2     Sunday
3     Monday
4    Tuesday
Name: Newnametimecolumn, dtype: int64
'''
extractdaynumberoftheyear = uforeplacetimecolumnnewnewnametimecolumn.Newnametimecolumn.dt.dayofyear
print(extractdaynumberoftheyear.head())
'''
0    152
1    181
2     46
3    152
4    108
Name: Newnametimecolumn, dtype: int64
'''
print(pd.to_datetime("1/1/1999")) #print 1999-01-01 00:00:00
print(type(pd.to_datetime("1/1/1999"))) #print <class 'pandas._libs.tslib.Timestamp'>
timestamps = pd.to_datetime("1/1/1999")
returnrowsdatelaterthantimestamps = uforeplacetimecolumnnewnewnametimecolumn.loc[uforeplacetimecolumnnewnewnametimecolumn.Newnametimecolumn >= timestamps, :]
print(returnrowsdatelaterthantimestamps.head())
'''
                    City Colors Reported Shape Reported State            Time  \
12832          Loma Rica             NaN          LIGHT    CA   1/1/1999 2:30   
12833            Bauxite             NaN            NaN    AR   1/1/1999 3:00   
12834           Florence             NaN       CYLINDER    SC  1/1/1999 14:00   
12835       Lake Henshaw             NaN          CIGAR    CA  1/1/1999 15:00   
12836  Wilmington Island             NaN          LIGHT    GA  1/1/1999 17:15   

        Newnametimecolumn  
12832 1999-01-01 02:30:00  
12833 1999-01-01 03:00:00  
12834 1999-01-01 14:00:00  
12835 1999-01-01 15:00:00  
12836 1999-01-01 17:15:00
...
'''
latesttimestamp = uforeplacetimecolumnnewnewnametimecolumn.Newnametimecolumn.max()
print(latesttimestamp) #print 2000-12-31 23:59:00
mathtimestamp = uforeplacetimecolumnnewnewnametimecolumn.Newnametimecolumn.max() - uforeplacetimecolumnnewnewnametimecolumn.Newnametimecolumn.min()
print(mathtimestamp) #print 25781 days 01:59:00
print(mathtimestamp.days) #print 25781

#How do I find and remove duplicate rows in pandas-ht5buXUMqkQ
#dataset of movie reviewers modifying the default parameter values for read_table
usercolumns = ["userid", "age", "gender", "occupation", "zipcode"]
users = pd.read_table("http://bit.ly/movieusers", sep="|", header=None, names=usercolumns, index_col="userid")
print(users.head())
'''
        age gender  occupation zipcode
userid                                
1        24      M  technician   85711
2        53      F       other   94043
3        23      M      writer   32067
4        24      M  technician   43537
5        33      F       other   15213

'''
print(users.shape) #print (943,4)
identifyduplicatezipcodes = users.zipcode.duplicated()
print(identifyduplicatezipcodes.head())
'''
userid
1    False
2    False
3    False
4    False
5    False
Name: zipcode, dtype: bool
'''
sumduplicatezipcodes = users.zipcode.duplicated().sum()
print(sumduplicatezipcodes) #print 148
identifyduplicaterowdataframe = users.duplicated()
print(identifyduplicaterowdataframe.head())
'''
userid
1    False
2    False
3    False
4    False
5    False
dtype: bool
'''
print(identifyduplicaterowdataframe.sum()) #print 7
returnduplicaterowsprintlastduplicates = users.loc[users.duplicated(keep="first"), :]
print(returnduplicaterowsprintlastduplicates)
'''
        age gender occupation zipcode
userid                               
496      21      F    student   55414
572      51      M   educator   20003
621      17      M    student   60402
684      28      M    student   55414
733      44      F      other   60630
805      27      F      other   20009
890      32      M    student   97301
'''
returnduplicaterowsprintfirstduplicates = users.loc[users.duplicated(keep="last"), :]
print(returnduplicaterowsprintfirstduplicates)
'''
        age gender occupation zipcode
userid                               
67       17      M    student   60402
85       51      M   educator   20003
198      21      F    student   55414
350      32      M    student   97301
428      28      M    student   55414
437      27      F      other   20009
460      44      F      other   60630
'''
returnduplicaterowsprintallduplicates = users.loc[users.duplicated(keep=False), :]
print(returnduplicaterowsprintallduplicates)
'''
        age gender occupation zipcode
userid                               
67       17      M    student   60402
85       51      M   educator   20003
198      21      F    student   55414
350      32      M    student   97301
428      28      M    student   55414
437      27      F      other   20009
460      44      F      other   60630
496      21      F    student   55414
572      51      M   educator   20003
621      17      M    student   60402
684      28      M    student   55414
733      44      F      other   60630
805      27      F      other   20009
890      32      M    student   97301
'''
deleteduplicates = users.drop_duplicates(keep="first")  #keep="first" is defeault
print(deleteduplicates.shape) #print (936, 4)
deleteallduplicates = users.drop_duplicates(keep=False)  #keep="first" is defeault
print(deleteallduplicates.shape) #print (929, 4)

import pandas as pd

#How do I avoid a SettingWithCopyWarning in pandas-4R4WsDJ-KVc
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
countmissingcontentrating = movies.content_rating.isnull().sum()
print(countmissingcontentrating) #print 3
booleanisnull = movies.content_rating.isnull()
print(booleanisnull.head())
'''
0    False
1    False
2    False
3    False
4    False
Name: content_rating, dtype: bool
'''
print(movies[booleanisnull])  #generate a boolean series to pass to the data frame movies.  content_rating is NaN
'''
     star_rating                               title content_rating  \
187          8.2  Butch Cassidy and the Sundance Kid            NaN   
649          7.7                   Where Eagles Dare            NaN   
936          7.4                           True Grit            NaN   

         genre  duration                                        actors_list  
187  Biography       110  [u'Paul Newman', u'Robert Redford', u'Katharin...  
649     Action       158  [u'Richard Burton', u'Clint Eastwood', u'Mary ...  
936  Adventure       128    [u'John Wayne', u'Kim Darby', u'Glen Campbell'] 
'''
uniquevaluecountscontentraitng = movies.content_rating.value_counts()
print(uniquevaluecountscontentraitng)
'''
R            460
PG-13        189
PG           123
NOT RATED     65
APPROVED      47
UNRATED       38
G             32
NC-17          7
PASSED         7
X              4
GP             3
TV-MA          1
Name: content_rating, dtype: int64
'''
notratedcontentrating = movies[movies.content_rating == "NOT RATED"]
print(notratedcontentrating.head())
'''
    star_rating                           title content_rating    genre  \
5           8.9                    12 Angry Men      NOT RATED    Drama   
6           8.9  The Good, the Bad and the Ugly      NOT RATED  Western   
41          8.5                    Sunset Blvd.      NOT RATED    Drama   
63          8.4                               M      NOT RATED    Crime   
66          8.4             Munna Bhai M.B.B.S.      NOT RATED   Comedy   

    duration                                        actors_list  
5         96  [u'Henry Fonda', u'Lee J. Cobb', u'Martin Bals...  
6        161  [u'Clint Eastwood', u'Eli Wallach', u'Lee Van ...  
41       110  [u'William Holden', u'Gloria Swanson', u'Erich...  
63        99  [u'Peter Lorre', u'Ellen Widmann', u'Inge Land...  
66       156   [u'Sunil Dutt', u'Sanjay Dutt', u'Arshad Warsi']  
'''
notratedcontentratingonly = movies[movies.content_rating == "NOT RATED"].content_rating
print(notratedcontentratingonly.head())
'''
5     NOT RATED
6     NOT RATED
41    NOT RATED
63    NOT RATED
66    NOT RATED
Name: content_rating, dtype: object
'''
#Overwrite or replace data.  In this case, NOT RATED is np.nan.  Error message.
import numpy as np
movies[movies.content_rating == "NOT RATED"].content_rating = np.nan
'''
/usr/lib/python3/dist-packages/pandas/core/generic.py:3643: SettingWithCopyWarning: 
A value is trying to be set on a copy of a slice from a DataFrame.
Try using .loc[row_indexer,col_indexer] = value instead

See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
  self[name] = value
#RM:  movies[movies.content_rating == "NOT RATED"] and .content_rating = np.nan are two operations.  movies[movies.content_rating == "NOT RATED"] is either a view or a copy.
'''
countmissingcontentrating = movies.content_rating.isnull().sum()
print(countmissingcontentrating) #print 3
#Overwrite or replace data.  In this case, NOT RATED is np.nan.  No error message.
movies.loc[movies.content_rating == "NOT RATED", "content_rating"] = np.nan
countmissingcontentrating = movies.content_rating.isnull().sum()
print(countmissingcontentrating) #print 68
contentratingnotratedtonan = movies.content_rating.isnull()
print(movies[contentratingnotratedtonan].head())
'''
    star_rating                           title content_rating    genre  \
5           8.9                    12 Angry Men            NaN    Drama   
6           8.9  The Good, the Bad and the Ugly            NaN  Western   
41          8.5                    Sunset Blvd.            NaN    Drama   
63          8.4                               M            NaN    Crime   
66          8.4             Munna Bhai M.B.B.S.            NaN   Comedy   

    duration                                        actors_list  
5         96  [u'Henry Fonda', u'Lee J. Cobb', u'Martin Bals...  
6        161  [u'Clint Eastwood', u'Eli Wallach', u'Lee Van ...  
41       110  [u'William Holden', u'Gloria Swanson', u'Erich...  
63        99  [u'Peter Lorre', u'Ellen Widmann', u'Inge Land...  
66       156   [u'Sunil Dutt', u'Sanjay Dutt', u'Arshad Warsi']  
'''
allninestarratingmovies = movies.loc[movies.star_rating >= 9, :]
print(allninestarratingmovies)
'''
   star_rating                     title content_rating   genre  duration  \
0          9.3  The Shawshank Redemption              R   Crime       142   
1          9.2             The Godfather              R   Crime       175   
2          9.1    The Godfather: Part II              R   Crime       200   
3          9.0           The Dark Knight          PG-13  Action       152   

                                         actors_list  
0  [u'Tim Robbins', u'Morgan Freeman', u'Bob Gunt...  
1    [u'Marlon Brando', u'Al Pacino', u'James Caan']  
2  [u'Al Pacino', u'Robert De Niro', u'Robert Duv...  
3  [u'Christian Bale', u'Heath Ledger', u'Aaron E... 
'''
#Pretend The Shawshank Redemption duration is incorrect.  Change from 142 to 150.
allninestarratingmovies.loc[0, "duration"] = 150
'''
/usr/lib/python3/dist-packages/pandas/core/indexing.py:537: SettingWithCopyWarning: 
A value is trying to be set on a copy of a slice from a DataFrame.
Try using .loc[row_indexer,col_indexer] = value instead

See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
  self.obj[item] = s
'''
print(allninestarratingmovies) #RM:  Warning SettingWithCopyWarning incorrect.  The Shawshank Redemption duration pretended correction worked.  Changed from 142 to 150.  Avoid the error message, add .copy().  allninestarratingmovies = movies.loc[movies.star_rating >= 9, :].copy()
'''
   star_rating                     title content_rating   genre  duration  \
0          9.3  The Shawshank Redemption              R   Crime       150   
1          9.2             The Godfather              R   Crime       175   
2          9.1    The Godfather: Part II              R   Crime       200   
3          9.0           The Dark Knight          PG-13  Action       152   

                                         actors_list  
0  [u'Tim Robbins', u'Morgan Freeman', u'Bob Gunt...  
1    [u'Marlon Brando', u'Al Pacino', u'James Caan']  
2  [u'Al Pacino', u'Robert De Niro', u'Robert Duv...  
3  [u'Christian Bale', u'Heath Ledger', u'Aaron E...  
'''
#Correction no error message
allninestarratingmoviesnoerrormessage = movies.loc[movies.star_rating >= 9, :].copy()
allninestarratingmoviesnoerrormessage.loc[0, "duration"] = 555
print(allninestarratingmoviesnoerrormessage.loc[allninestarratingmoviesnoerrormessage.title == "The Shawshank Redemption"])
'''
   star_rating                     title content_rating  genre  duration  \
0          9.3  The Shawshank Redemption              R  Crime       555   

                                         actors_list  
0  [u'Tim Robbins', u'Morgan Freeman', u'Bob Gunt...  
'''

#How do I change display options in pandas-yiO43TQ4xvc
drinks = pd.read_csv("http://bit.ly/drinksbycountry")
howmanyrowsdisplay = pd.get_option("display.max_rows")
print(howmanyrowsdisplay) #print 60  RM:  run print(drinks) returns 60 rows.  Top 30 rows and bottom 30 rows.
pd.set_option("display.max_rows", None) #Set how many rows displayed.  None means show all rows
#print(drinks) #prints all rows
pd.reset_option("display.max_rows") #Reset number of rows displayed.
#print(drinks) #prints 60 rows.  Top 30 rows and bottom 30 rows.
howmanycolumnsdisplayed = pd.get_option("display.max_columns")
print(howmanycolumnsdisplayed) #print 20
train = pd.read_csv("http://bit.ly/kaggletrain")
print(train.head())
'''
   PassengerId  Survived  Pclass  \
0            1         0       3   
1            2         1       1   
2            3         1       3   
3            4         1       1   
4            5         0       3   

                                                Name     Sex   Age  SibSp  \
0                            Braund, Mr. Owen Harris    male  22.0      1   
1  Cumings, Mrs. John Bradley (Florence Briggs Th...  female  38.0      1   
2                             Heikkinen, Miss. Laina  female  26.0      0   
3       Futrelle, Mrs. Jacques Heath (Lily May Peel)  female  35.0      1   
4                           Allen, Mr. William Henry    male  35.0      0   

   Parch            Ticket     Fare Cabin Embarked  
0      0         A/5 21171   7.2500   NaN        S  
1      0          PC 17599  71.2833   C85        C  
2      0  STON/O2. 3101282   7.9250   NaN        S  
3      0            113803  53.1000  C123        S  
4      0            373450   8.0500   NaN        S  
'''
howlongcolumnwidthdisplay = pd.get_option("display.max_colwidth")
print(howlongcolumnwidthdisplay) #print 50
pd.set_option("display.max_colwidth", 1000) #set max width all columns to 1000 characters
print(train.head())
'''
   PassengerId  Survived  Pclass  \
0            1         0       3   
1            2         1       1   
2            3         1       3   
3            4         1       1   
4            5         0       3   

                                                  Name     Sex   Age  SibSp  \
0                              Braund, Mr. Owen Harris    male  22.0      1   
1  Cumings, Mrs. John Bradley (Florence Briggs Thayer)  female  38.0      1   
2                               Heikkinen, Miss. Laina  female  26.0      0   
3         Futrelle, Mrs. Jacques Heath (Lily May Peel)  female  35.0      1   
4                             Allen, Mr. William Henry    male  35.0      0   

   Parch            Ticket     Fare Cabin Embarked  
0      0         A/5 21171   7.2500   NaN        S  
1      0          PC 17599  71.2833   C85        C  
2      0  STON/O2. 3101282   7.9250   NaN        S  
3      0            113803  53.1000  C123        S  
4      0            373450   8.0500   NaN        S  
'''
numberofdecimalsdisplay = pd.get_option("display.precision")
print(numberofdecimalsdisplay) #print 6
pd.set_option("display.precision", 2) #set decimal places to two
print(train.head())
'''
   PassengerId  Survived  Pclass  \
0            1         0       3   
1            2         1       1   
2            3         1       3   
3            4         1       1   
4            5         0       3   

                                                  Name     Sex   Age  SibSp  \
0                              Braund, Mr. Owen Harris    male  22.0      1   
1  Cumings, Mrs. John Bradley (Florence Briggs Thayer)  female  38.0      1   
2                               Heikkinen, Miss. Laina  female  26.0      0   
3         Futrelle, Mrs. Jacques Heath (Lily May Peel)  female  35.0      1   
4                             Allen, Mr. William Henry    male  35.0      0   

   Parch            Ticket   Fare Cabin Embarked  
0      0         A/5 21171   7.25   NaN        S  
1      0          PC 17599  71.28   C85        C  
2      0  STON/O2. 3101282   7.92   NaN        S  
3      0            113803  53.10  C123        S  
4      0            373450   8.05   NaN        S 
'''
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
drinks["newcolumnmultiplywineservings"] = drinks.wine_servings * 1000
drinks["newcolumnmultiplytotallitrespurealcohol"] = drinks.total_litres_of_pure_alcohol * 1000
print(drinks.head())
'''
       country  beer_servings  spirit_servings  wine_servings  \
0  Afghanistan              0                0              0   
1      Albania             89              132             54   
2      Algeria             25                0             14   
3      Andorra            245              138            312   
4       Angola            217               57             45   

   total_litres_of_pure_alcohol continent  newcolumnmultiplywineservings  
0                           0.0      Asia                              0  
1                           4.9    Europe                          54000  
2                           0.7    Africa                          14000  
3                          12.4    Europe                         312000  
4                           5.9    Africa                          45000  
'''
pd.set_option("display.float_format", "{:,}".format)
print(drinks.head())  #RM:  notice newcolumnmultiplytotallitrespurealcohol includes commas only.  Reason is wine_servings is integer.  total_litres_of_pure_alcohol is float.  Instructor says no easy to to add commas to integers.
'''
   total_litres_of_pure_alcohol continent  newcolumnmultiplywineservings  \
0                           0.0      Asia                              0   
1                           4.9    Europe                          54000   
2                           0.7    Africa                          14000   
3                          12.4    Europe                         312000   
4                           5.9    Africa                          45000   

   newcolumnmultiplytotallitrespurealcohol  
0                                      0.0  
1                                  4,900.0  
2                                    700.0  
3                                 12,400.0  
4                                  5,900.0  
'''
helppandasoptions = pd.describe_option()
print(helppandasoptions)
helppandasoptionssearchrows = pd.describe_option("rows")
print(helppandasoptionssearchrows)
pd.reset_option("all") #reset all options to default.  Okay to ignore warnings.

#How do I create a pandas DataFrame from another object--Ov1N1_FbP8
newdataframe = pd.DataFrame({"id": [100, 101, 102], "color": ["red", "blue", "red"], "columnname": ["row1", "row2", "row3"]}, columns=["id", "color", "columnname"], index=["labelindexa", "labelindexb", "labelindexc"])
print(newdataframe)
'''
              id color columnname
labelindexa  100   red       row1
labelindexb  101  blue       row2
labelindexc  102   red       row3
'''
passalistdataframe = pd.DataFrame([[100, "red"], [101, "blue"], [102, "red"]])
print(passalistdataframe)
'''
     0     1
0  100   red
1  101  blue
2  102   red
'''
passalistdataframewithcolumns = pd.DataFrame([[100, "red"], [101, "blue"], [102, "red"]], columns={"id", "color"})
print(passalistdataframewithcolumns)
'''
    id color
0  100   red
1  101  blue
2  102   red
'''
import numpy as np
randomnumbers = np.random.rand(4, 2) #create a uniform distribution random numbers between 0 and 1 four rows and two columns
convertnumpytopandasdataframe = pd.DataFrame(randomnumbers, columns=["columnone", "columntwo"])
print(convertnumpytopandasdataframe)
'''
   columnone  columntwo
0   0.787451   0.756757
1   0.975423   0.471959
2   0.262481   0.132679
3   0.609112   0.781030
'''
numpyrandomdataframe = pd.DataFrame({"ten student ids": np.arange(100, 110), "ten test scores": np.random.randint(60, 101, 10)})
print(numpyrandomdataframe)
'''
   ten student ids  ten test scores
0              100               97
1              101               81
2              102               99
3              103               89
4              104               71
5              105               93
6              106               92
7              107               61
8              108               81
9              109               76
'''
numpyrandomdataframesetstudentidsasindex = pd.DataFrame({"ten student ids": np.arange(100, 110), "ten test scores": np.random.randint(60, 101, 10)}).set_index("ten student ids")
print(numpyrandomdataframesetstudentidsasindex)
'''
                 ten test scores
ten student ids                 
100                          100
101                           75
102                           83
103                           81
104                           90
105                           67
106                           82
107                           63
108                           64
109                           97
'''
shapeseries = pd.Series(["round", "square"], index=["labelindexc", "labelindexb"], name="series identifier shape")
print(shapeseries)
'''
labelindexc     round
labelindexb    square
Name: series identifier shape, dtype: object
'''
combinedatframeandseries = pd.concat([newdataframe, shapeseries], axis=1)
print(combinedatframeandseries)
'''
              id color columnname series identifier shape
labelindexa  100   red       row1                     NaN
labelindexb  101  blue       row2                  square
labelindexc  102   red       row3                   round
'''