from flask import Flask, render_template, request
import MySQLdb as mdb
app = Flask(__name__)

connection = mdb.connect('localhost', 'user', 'pass', 'beer')

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/analytics')
def analytics():
    return render_template('analytics.html')


@app.route('/results', methods = ['POST'])
def test():
    print request.form['dropdown']
    current = connection.cursor()
    current.execute('select * from drinkers')
    rows = current.fetchall()
    return render_template('results.html', results=rows)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
