import MySQLdb as mdb
import names as names
from faker import address, phone_number
from random import choice, randint

def populateDrinkers():

    con = mdb.connect('localhost', 'user', 'pass', 'barlytics')
    curr = con.cursor()

    professions = [['doctor', 2], ['lawyer',2],  ['engineer',2], ['teacher',1], ['contruction worker', 1], ['dentist', 1], ['nurse',1], ['cashier',0], ['janitor',0], ['garbage man', 0], ['driver', 0]]

    for i in range(0, 9002):
        name = names.get_full_name()
        rand = choice(professions)
        profession = rand[0]
        income = rand[1];
        age = choice([randint(18,21), randint(21, 35), randint(21,35), randint(21,35), randint(35, 55), randint (35, 55), randint(55,100)])
        phone = phone_number.phone_number()
        city = address.city()
        addr = str(randint(1,255)) + address.street_name()
        try:
            curr.execute('INSERT INTO drinkers VALUES ("' + str(name) + '", "' + city +  '", "' + str(phone) +  '", "' + str(addr) +  '", "' + profession +  '", "' + str(age) +  '", "' + str(income) + '");')
        except mdb.IntegrityError:
            print "Integrity Error: "
            i = i - 1
        # print 'INSERT INTO drinkers VALUES ("' + name + '", "' + city +  '", "' + phone +  '", "' + addr +  '", "' + profession +  '", "' + str(age) +  '", "' + str(income) + '");'

    con.commit()
