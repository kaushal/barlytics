from flask import Flask, render_template, request
import MySQLdb as mdb
app = Flask(__name__)

connection = mdb.connect('localhost', 'user', 'pass', 'barlytics')
current = connection.cursor()

age_query = 'SELECT AVG(age) from frequents, drinkers where drinkers.name = frequents.drinker and frequents.bar = %s;'
beer_query = 'SELECT l.beer, avg(rating) as sa from likes as l group by l.beer order by sa desc limit 1;'
bar_rating_query = 'SELECT AVG(rating) from checkin where bar = %s;'
profession_query = 'SELECT profession, count(*) from frequents, drinkers where bar = %s and drinkers.name = drinker group by drinkers.profession;'
income_query = 'SELECT income, count(*) from frequents, drinkers where bar = %s and drinkers.name = drinker group by drinkers.income;'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/analytics')
def analytics():
    current.execute('select * from bars; ' )
    names = current.fetchall()
    namesList = []
    for row in names:
        namesList.append(row[0])
    return render_template('analytics.html', barNames=namesList)


@app.route('/results', methods=['POST'])
def test():
    returnObject = {}
    print request.form['bar']
    bar = request.form['bar']
    print request.form['demographic']
    if request.form['demographic'] == 'Average Age':
        current.execute(age_query, bar)
        returnObject['query'] = age_query
        returnObject['purpose'] = 'This is the average age of the people that visit your bar'
    elif request.form['demographic']== 'Average Income':
        returnObject['purpose'] = 'Average income bracket that your patrons are in. {0:low, 1:middle, 2:high}'
        current.execute(income_query, (bar,))
        returnObject['query'] = income_query
    elif request.form['demographic'] == 'Beer Rating':
        current.execute(beer_query)
        returnObject['query'] = beer_query
        returnObject['purpose'] = 'This is your highest rated beer!'
    elif request.form['demographic']== 'Bar Rating':
        current.execute(bar_rating_query, bar)
        returnObject['purpose'] = 'Average customer review of your bar.'
        returnObject['query'] = bar_rating_query
    elif request.form['demographic']== 'Customer Occupation':
        current.execute(profession_query, bar)
        returnObject['query'] = profession_query
        returnObject['purpose'] = 'List of professions that your patrons are.'

    returnObject['returnRows'] = current.fetchall()

    return render_template('results.html', results=returnObject)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
