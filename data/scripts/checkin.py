import MySQLdb as mdb
from random import randint

def populateCheckin():

    connection = mdb.connect('localhost', 'user', 'pass', 'barlytics')

    current = connection.cursor()


    current.execute("select * from drinkers")
    drinkers = current.fetchall()

    current.execute("select * from bars")
    bars = current.fetchall()

    baseDates = ['2013-11-21', '2013-11-22', '2013-11-23']
    checkinTimes = ['20', '21', '22', '23', '00', '01', '02']

    drinkerCount = 0
    barCount = 0

    for drinker in drinkers:
        drinkerCount = drinkerCount + 1

    for bar in bars:
        barCount = barCount + 1
    total = 0
    for drinker in drinkers:
        for i in range(randint(0, 10)):
            total = total + 1
            string = 'insert into checkin values ("' + str(bars[randint(0, barCount - 1)][0]) + '", "' + str(drinker[0]) + '", "' + baseDates[randint(0, 2)] + " " + str(checkinTimes[randint(0, 6)]) + ":" + str(randint(10, 59)) + ":"  + str(randint(10, 59)) + '");'
            current.execute(string)

    connection.commit()

    print total
