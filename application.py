from flask import Flask,render_template, request
from sqlconn import mongodb
import logging
logging.basicConfig(filename='recipe.log', level=logging.DEBUG)
   
   
app = Flask(__name__)
application = app
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/view", methods=['POST'])
def view():

    query = """create table if not exists users
            (username varchar(40),
            name varchar(40), 
            email varchar(40), 
            gender char, 
            state varchar(25), 
            city varchar(30),      
            primary key (username), unique(email) );"""
    
    name = request.form['username']    
    coll = mongodb[f'{name}']
    records = coll.find()
    return render_template('view.html', details = records, user= name )


@app.route('/add', methods=['POST'])
def add():
    username = request.form['username']
    name = request.form['naam']
    email = request.form['useremail']
    gender = request.form['gender']
    state = request.form['state']
    city = request.form['city']    
    query = """create table if not exists users
            (username varchar(40),
            name varchar(40), 
            email varchar(40), 
            gender char, 
            state varchar(25), 
            city varchar(30),      
            primary key (username), unique(email) );"""
    
    coll = mongodb[f'{username}']
    coll.insert_one({"name":name, "email": email, 'sex' : gender, 'city': city, 'state': state})
    for i in coll.find() :
        print(i['name'])
    
    return render_template('index.html', msg = 'Your account created!')

@app.route('/new')
def new():
   return render_template('newuser.html') 


@app.route('/newrecipe/<user>')
def newrecipe(user):
    return render_template('newrecipe.html', username = user)
        
@app.route('/addrecipe/<username>',methods=['POST'])
def addrecipe(username):
    coll = mongodb[f'{username}']
    entries={}
    entries['rname']= request.form["title"]
    entries['description']= request.form["description"]
    coll.insert_one(entries)
    return 'Added Successfull, <a href="/">return</a>'
        
        
if __name__ == '__main__':
    app.run()