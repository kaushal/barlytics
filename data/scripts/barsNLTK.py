from random import randint, choice
from time import sleep
from nltk.corpus import wordnet as wn
import MySQLdb as mdb
from faker import address, phone_number

def populateBars():

    connection = mdb.connect('localhost', 'user', 'pass', 'barlytics')

    current = connection.cursor()

    nounsList = []
    adjectiveList = []
    cityList = ['San Francisco', 'Chicago', 'New York', 'Austin', 'Seattle']

    print "here"
    count = 0
    for synset in list(wn.all_synsets('n')):
        nounsList.append(str(synset.name).split('.')[0])
        count = count + 1
        if count >= 50000:
            break

    count= 0
    print "here"
    for synset in list(wn.all_synsets('a')):
        adjectiveList.append(str(synset.name).split('.')[0])
        count = count + 1
        if count >= 50000:
            break
    print "here"
    finalList = []
    for i in range(10000):
        string = ''
        string = "The " + adjectiveList[randint(0, len(adjectiveList) - 1)].capitalize()

        string = string + " " + nounsList[randint(0, len(nounsList) - 1)].capitalize()
        finalList.append(string)

        name = string
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
