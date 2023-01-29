import pymysql

vals1 = [
    [482, "Ryan,premium customer,AlexanderPlatz,Berlin,Customer" ],
    [482, "Ali,pensioner,München,Bayern,Orders" ],
    [482, "Anna,student,Dresden,Saxony,School" ],
    [482, "Anje,customer,Stuttgart,Baden-Württemberg,SuperMarkt" ],
    [482, "Katya,employee,Mainz,Rheinland-Pfalz,Railwaystation" ],
    [482, "Tomas,tramdriver,Erfurt,Thüringen,Trams" ],
    [482, "Jacob,pilot,Düsseldorf,Nordrhein-Westfalen,Airport" ],
    [482, "Oliver,professor,Magdeburg,Sachsen-Anhalt,University" ],
    [482, "youngest,player,Potsdam,Brandenburg,Teams" ],
    [482, "triwizard,champion,Hanover,Niedersachsen,Tournaments" ],
    [482, "cinemaxx,imax,Schwerin,Mecklenburg-Vorpommern,Cinemas" ],
    [482, "Regel,dramastudio,Winterhude,Hamburg,Theaters" ],
    [482, "Alex,founder,Kiel,Schleswig-Holstein,Companies" ],
    [482, "Empire,branch,Saarbrücken,Saarland,Hotels" ],
    [482, "Fabian,chef,alle,Bremen,Restaurents" ]
]

vals2 = [
    [487, "Baseball,Pitcher,Catcher,Outfielder,Infielder,Teams" ],
    [487, "Softball,First Baseman,Second Baseman,Left Fielder,Shortstop,Contestants" ],
    [487, "Soccer,Sweeper,Winger,Striker,Backs,Sports" ],
    [487, "Rugby,Hooker,Locks,Quarterbacks,Flankers,Participants" ],
    [487, "Cricket,Wicketkeeper,Third Man,Point,Bowler,Tournament" ],
]

#database connection
connection = pymysql.connect(host="localhost", user="root", passwd="", database="dbse_project")

cursor = connection.cursor()
cursor.executemany("insert into bag_of_words (task_id,bow ) values (%s, %s)", vals2)


#commiting the connection then closing it.
connection.commit()
connection.close()