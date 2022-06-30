import os
from flask import jsonify, request, Flask,render_template, redirect
from flaskext.mysql import MySQL
import sys

app = Flask(__name__, template_folder='template')

#mysql = MySQL()

#app.config["MYSQL_DATABASE_USER"] = "root"
#app.config["MYSQL_DATABASE_PASSWORD"] = os.getenv("db_root_password")
#app.config["MYSQL_DATABASE_DB"] = os.getenv("db_name")
#app.config["MYSQL_DATABASE_HOST"] = os.getenv("MYSQL_SERVICE_HOST")
#app.config["MYSQL_DATABASE_PORT"] = int(os.getenv("MYSQL_SERVICE_PORT"))
#mysql.init_app(app)


@app.route("/", methods=['GET', 'POST'])
def index():
    #if request.method=='POST':
        #print('Entered if', file=sys.stderr)
        #ud=request.form
        #name= ud['name']
        #email=ud['email']
        #password=ud['pass']
        #print('data stored in variables', file=sys.stderr)
        #sql = "INSERT INTO users(user_name, user_email ,user_password) " \
              #"VALUES(%s, %s, %s)"
        #data = (name, email, password)
        #con = mysql.connect()
        #cur=con.cursor()
        #cur.execute(sql,data)
        #con.commit()
        #con.close()
        #cur.close()
        #return redirect('/users')
              
    #else:
    return render_template('index.html')


#@app.route('/users', methods=['GET', 'POST'])
#def users():
    #con = mysql.connect()
    #cur=con.cursor()
    #resultVal=cur.execute("SELECT * FROM users")
    #if resultVal>0:
        #ud=cur.fetchall()
        #con.close()
        #cur.close()
        #return render_template('users.html',ud=ud)


if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=5000)
