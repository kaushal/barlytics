import MySQLdb as mdb
import names as names
from random import choice, randint

con = mdb.connect('localhost', 'user', 'pass', 'barlytics')
drinkers = con.cursor()
beers = con.cursor()
write = con.cursor()

drinkers.execute('Select name from drinkers;')
beers.execute('select name from beers;')
allbeers = beers.fetchall()

for i in range(drinkers.rowcount):
    drinker =  drinkers.fetchone()[0]
    for i in range(randint(0,5)):
        beer = choice(allbeers)[0]
        rating = randint(1,5)
        
        try:
            string = 'INSERT INTO likes VALUES ("' + drinker + '", "' + beer + '", "' + str(rating) + '");'
            write.execute(string)
        except mdb.IntegrityError:
            print "Integrity Error: "
            i = i - 1

con.commit()
