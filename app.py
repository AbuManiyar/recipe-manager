from flask import Flask,render_template, request
from sqlconn import mongodb, cursor

   
   
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/view", methods=['POST'])
def view():
    cursor.execute('create database if not exists recipe_manager')
    name = request.form['Name']
    cursor.execute('use recipe_manager')
    cursor.execute('show tables;')
    users = cursor.fetchall()
    list_user=[]
    print(users)
    for i in range(len(users[0])):
        list_user.append(users[0][i])
    if name in list_user: 
        coll = mongodb[f'{name}']
        print(coll.find())
       # coll.insert_one({'name':name})
        
    else: return 'Not a valid user'
    
    recipes = coll.find()
    for i in recipes :
        print(i)
    return render_template('view.html', obtained_name= name)


@app.route('/add', methods=['POST'])
def add():
    name = request.form['username']
    email = request.form['useremail']
    cursor.execute(f'create table if not exists {name}(email varchar(40), primary key (id));')
    cursor.execute(f"insert into {name} value('{email}')")
    return 'Successful'

@app.route('/new')
def new():
   return render_template('newuser.html') 
if __name__ == '__main__':
    app.run(debug=True)