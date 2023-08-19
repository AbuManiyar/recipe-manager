from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://abu:AbuAneeza@cluster0.avzoqux.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

mongodb = client['recipe_manager']

 

#Sql DB
import mysql.connector as conn
db = conn.connect(host = 'localhost', user= 'root', password = 'AbuAneeza@123')
cursor = db.cursor()
cursor.execute('use recipe_manager')

sqldb= cursor