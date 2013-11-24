from random import randint, choice
from time import sleep
from nltk.corpus import wordnet as wn
import MySQLdb as mdb
from faker import address, phone_number

def populateBars():

    connection = mdb.connect('localhost', 'user', 'pass', 'barlytics')

    current = connection.cursor()

    f = open('bars.txt', 'r')

    for line in f:
        name = line
        license = str(randint(1000000, 9000000))
        city = str(address.city())
        phone = str(phone_number.phone_number_format(0))
        addr = str(randint(1, 255)) + " " + address.street_name()


        query = 'insert into bars values("' + name + '", "' + license + '", "' + city + '", "' + phone + '", "' + addr + '"); '
        print query
        try:
            current.execute(query)
        except mdb.IntegrityError:
            print "integrity error:"
    print 'commit'
    connection.commit()
