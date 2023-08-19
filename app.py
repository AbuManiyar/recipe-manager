from flask import Flask,render_template, request
from sqlconn import mongodb, cursor

   
   
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/view", methods=['POST'])
def view():
    name = request.form['Name']
    cursor.execute('use recipe_manager')
    cursor.execute('create table if not exists iamuser(id int);')
    cursor.execute('show tables;')
    users = cursor.fetchall()
    list_user=[]
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


if __name__ == '__main__':
    app.run(debug=True)