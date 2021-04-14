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