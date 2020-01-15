from flask import Flask, url_for, render_template, request,session,redirect
from flaskext.mysql import MySQL

app=Flask(__name__)

app = Flask(__name__)
mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Bishnupada'
app.config['MYSQL_DATABASE_DB'] = 'Test'
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
def login():                                                               
    if request.method == 'POST':
        cursor = get_cursor()
         = request.form['username']
        password = request.form['password']
        cursor.execute('SELECT * from Users')
        users = cursor.fetchall()
        cursor.close()
        return "<h3>submit succesfully</h3>"
    return render_template('index.html')

@app.route('/update', methods=['GET','POST'])
def update():
    if request.method == 'POST':
        cursor = get_cursor()
        firstname = request.form['first_name']
        middlename = request.form['middle_name']
        lastname = request.form['last_name']
        fathername = request.form['father']
        email = request.form['email']
        contactno = request.form['contact_no']
        DOB = request.form['date_of_birth']
        Gender = request.form['Gender']
        Locality = request.form['Loclity']
        city= request.form['city']
        district = request.form['district']
        state= request.form['state']
        pin = request.form['pin']
        applicationfor = request.form['application_for']
        score = request.form['score']
        marksheet = request.form['marksheet']
        cursor.execute("UPDATE Users SET fullname = %s, fathersname = %s, contactno = %s where username = %s",(, fathersname, contactno, session['username']))
        connection.commit()
        cursor.close()
        return redirect(url_for('data'))
    return render_template('update.html')

@app.route('/logout')
def logout():
    session.pop('id', None)
    return redirect(url_for('login'))

@app.route('/data')
def data():
    cursor = get_cursor()
    cursor.execute("SELECT * from Users where username = %s", (session['username']))
    userdata = cursor.fetchone()
    return render_template('data.html', userdata = userdata)

def get_cursor():
    global connection 
    return connection.cursor()



if __name__=='__main__':
    app.run( port=8000,debug=True)