from sqlconn import mongodb

coll= mongodb['Daaku']
ld= [{'name':'daaku mangal', 'age': 18, 'location': 'jungle'},
    {'name':'Veerappan', 'age': 28, 'location': 'Amazon', 'cases': 32}]
print()
print()
print()
#name=input("Write name")
record = coll.find({'name': 'daaku mangal'})
print()
print()
print()

for i in record: 
    print('name = ' + i['name'])
    print('age = ' + str(i['age']))
    print('location = ' + i['location'])
   # print('cases = ' + str(i['cases']))