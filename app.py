from flask import Flask, render_template, request
import sqlite3 as sql


app = Flask(__name__)

#create home page
@app.route('/')
def home():
    return render_template('index.html')

#create about page
@app.route('/about')
def about():
    return render_template('about.html')

#create projects page
@app.route('/projects')
def projects():
    return render_template('projects.html')

#create contact page
@app.route('/contact')
def contact():
    return render_template('contact.html')


#create thanks page
@app.route('/thanks', methods=['POST', 'GET'])
def addRecords():
    if request.method == "POST":
        try:
            nm = request.form['nm']  
            sn = request.form['sn']
            email = request.form['email']
            message = request.form['message']

            with sql.connect("database.db") as con:
                cur = con.cursor()

                cur.execute("INSERT INTO customers (nm, sn, email, message) VALUES (?,?,?,?)", (nm, sn, email, message) )

                con.commit()
                msg = "Thank you for your message!"
        except:
            con.rollback()
            msg = 'oh noooooo!!!'

        finally:
            return render_template("thanks.html",msg = msg)
            con.close()

#create database page
@app.route('/list')
def list():
    con = sql.connect('database.db')
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute('select * from customers')

    rows = cur.fetchall()
    return render_template('list.html', rows = rows)
        
#save all the changes automatically    
if __name__ == '__main__':
        app.run(debug=True)

