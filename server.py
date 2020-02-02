from flask import Flask, url_for, render_template, request,session,redirect
from flaskext.mysql import MySQL

app=Flask(__name__)

mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Bishnupada'
app.config['MYSQL_DATABASE_DB'] = 'test'
app.config['MYSQL_DATABASE_HOST'] = '127.0.0.1'
app.config['MYSQL_DATABASE_PORT'] = 3306
app.secret_key = 'aks64_hsc'

mysql.init_app(app)
connection = mysql.connect()


@app.route('/')
@app.route('/page')
def page():
    return render_template('page.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/index', methods=['GET','POST'])
def complain():
    if request.method == 'POST':
        cursor = get_cursor()
        first_name = request.form['first_name']
        middle_name = request.form['middle_name']
        last_name = request.form['last_name']
        father = request.form['father']
        email = request.form['email']
        contact_no = request.form['contact_no']
        date_of_birth = request.form['date_of_birth']
        Gender = request.form['Gender']
        Loclity = request.form['Loclity']
        city= request.form['city']
        district = request.form['district']
        state= request.form['state']
        pin = request.form['pin']
        application_for = request.form['application_for']
        score = request.form['score']
        marksheet = request.form['marksheet']
        cursor.execute("INSERT INTO register(first_name,middle_name,last_name,father ,email, contact_no, date_of_birth, Gender, Loclity, city, district, state, pin, application_for, score, marksheet)VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",(first_name,middle_name,last_name,father,email, contact_no, date_of_birth, Gender, Loclity, city, district, state, pin, application_for, score, marksheet))
        connection.commit()
        cursor.close()
        return redirect(url_for('data'))
    return render_template('index.html')


@app.route('/data')
def data():
    cursor = get_cursor()
    cursor.execute("SELECT * from register")
    data = cursor.fetchall()
    return render_template('data.html', data = data)

def get_cursor():
    global connection 
    return connection.cursor()


if __name__=='__main__':
    app.run( port=8000,debug=True)