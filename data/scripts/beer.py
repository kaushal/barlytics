import MySQLdb as mdb

def populateBeers():

    connection = mdb.connect('localhost', 'user', 'pass', 'barlytics')

    current = connection.cursor()

    f = open('beer.txt', 'r')

    for line in f:
        first = 0
        brewery = ''
        beer = ''
        for item in line.split('|'):
            if first == 0:
                first = 1
                brewery = item.strip()
            else:
                beer = item.strip()
        string = 'insert into beers values ("' + beer + '", "' + brewery + '");'
        print string
        if beer != '' and brewery != '' and first != 0:
            print "got here"
            try:
                current.execute(string)
            except mdb.IntegrityError:
                print "didn't insert " + string
    connection.commit()
