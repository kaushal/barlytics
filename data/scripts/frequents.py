import MySQLdb as mdb
import names as names
from random import choice, randint

def populateFrequents():

    con = mdb.connect('localhost', 'user', 'pass', 'barlytics')
    drinkers = con.cursor()
    bars = con.cursor()
    write = con.cursor()

    drinkers.execute('Select name from drinkers;')
    bars.execute('select name from bars;')
    allbars = bars.fetchall()

    for i in range(drinkers.rowcount):
        drinker =  drinkers.fetchone()[0]
        for i in range(randint(0,15)):
            bar = choice(allbars)[0]

            try:
                string = 'INSERT INTO frequents VALUES ("' + drinker + '", "' + bar + '");'
                write.execute(string)
            except mdb.IntegrityError:
                print "Integrity Error: "
                i = i - 1

    con.commit()
