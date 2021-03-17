# Python MongoDB

# import datetime module
import datetime
# import pymongo module
import pymongo
myclient = pymongo.MongoClient("mongodb+srv://Chisoft:9thMileCorner@chisoftcluster.tnc8g.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

mydb = myclient["ChisoftDB"]
print(myclient.list_database_names())
print()
dblist = myclient.list_database_names()
if "ChisoftDB" in dblist:
  print("The database exists.")

# Python MongoDB Insert Document
mycol = mydb["customers"]

mydict = { "name": "John", "address": "Highway 37" }

x = mycol.insert_one(mydict)

print(x)

# sample data
document = {"company":"Capital One",
"city":"McLean",
"state":"VA",
"country":"US"}
# insert document into collection
id = mycol.insert_one(document).inserted_id
print("id")
print(id)

print(x.inserted_id)

# Insert Multiple Documents
mylist = [
  { "name": "Amy", "address": "Apple st 652"},
  { "name": "Hannah", "address": "Mountain 21"},
  { "name": "Michael", "address": "Valley 345"},
  { "name": "Sandy", "address": "Ocean blvd 2"},
  { "name": "Betty", "address": "Green Grass 1"},
  { "name": "Richard", "address": "Sky st 331"},
  { "name": "Susan", "address": "One way 98"},
  { "name": "Vicky", "address": "Yellow Garden 2"},
  { "name": "Ben", "address": "Park Lane 38"},
  { "name": "William", "address": "Central st 954"},
  { "name": "Chuck", "address": "Main Road 989"},
  { "name": "Viola", "address": "Sideway 1633"}
]

x = mycol.insert_many(mylist)

print(x.inserted_ids)


# Insert Multiple Documents, with Specified IDs
myEmp = mydb["Employees"]

mylist2 = [
  { "_id": 1, "name": "John P", "address": "Highway 37"},
  { "_id": 2, "name": "Peter A", "address": "Lowstreet 27"},
  { "_id": 3, "name": "Amy", "address": "Apple st 652"},
  { "_id": 4, "name": "Hannah", "address": "Mountain 21"},
  { "_id": 5, "name": "Michael", "address": "Valley 345"},
  { "_id": 6, "name": "Sandy", "address": "Ocean blvd 2"},
  { "_id": 7, "name": "Betty", "address": "Green Grass 1"},
  { "_id": 8, "name": "Richard", "address": "Sky st 331"},
  { "_id": 9, "name": "Susan", "address": "One way 98"},
  { "_id": 10, "name": "Vicky", "address": "Yellow Garden 2"},
  { "_id": 11, "name": "Ben", "address": "Park Lane 38"},
  { "_id": 12, "name": "William", "address": "Central st 954"},
  { "_id": 13, "name": "Chuck", "address": "Main Road 989"},
  { "_id": 14, "name": "Viola", "address": "Sideway 1633"},
  { "_id": 15, "name": "John P", "address": "Highway 37"},
  { "_id": 16, "name": "Peter A", "address": "Lowstreet 27"},
  { "_id": 17, "name": "Amy", "address": "Apple st 652"},
  { "_id": 18, "name": "Hannah", "address": "Mountain 21"},
  { "_id": 19, "name": "Michael", "address": "Valley 345"},
  { "_id": 20, "name": "Sandy", "address": "Ocean blvd 2"},
  { "_id": 21, "name": "Betty", "address": "Green Grass 1"},
  { "_id": 22, "name": "Richard", "address": "Sky st 331"},
  { "_id": 23, "name": "Susan", "address": "One way 98"},
  { "_id": 24, "name": "Vicky", "address": "Yellow Garden 2"},
  { "_id": 25, "name": "Ben", "address": "Park Lane 38"},
  { "_id": 26, "name": "William", "address": "Central st 954"},
  { "_id": 27, "name": "Chuck", "address": "Main Road 989"},
  { "_id": 28, "name": "Viola", "address": "Sideway 1633"}
]

y = myEmp.insert_many(mylist2)
print(x.inserted_ids)

# Python MongoDB Find
# Find One

x = mycol.find_one()
print(x)
print()
y = myEmp.find_one()
print(y)
print()

# Find All
for x in mycol.find():
    print(x)
print()

for y in myEmp.find():
    print(y)
print()

# Return Only Some Fields
for x in myEmp.find({},{ "_id": 0, "name": 1, "address": 1 }):
  print(x)
print()

# Python MongoDB Query
# Filter the Result
myquery = {"address" : "Park Lane 38"}
mydoc = myEmp.find(myquery)
for x in mydoc:
    print(x)
print()

# Advanced Query
myquery = { "address": { "$gt": "S" } }

mydoc = myEmp.find(myquery)

for x in mydoc:
  print(x)
print()

# Filter With Regular Expressions
myquery = { "address": { "$regex": "^S" } }

mydoc = myEmp.find(myquery)

for x in mydoc:
  print(x)
print()
# Python MongoDB Sort
mydoc = myEmp.find().sort("name")

for x in mydoc:
  print(x)
print()

# Sort Descending
mydoc = myEmp.find().sort("name", -1)

for x in mydoc:
  print(x)
print()

# Python MongoDB Delete Document
myquery = {"address": "Yellow Garden 2"}

myEmp.delete_one(myquery)

mydoc = myEmp.find().sort("name", -1)

for x in mydoc:
  print(x)
print()


# Delete Many Documents
myquery1 = { "address": {"$regex": "^M"} }
x = myEmp.delete_many(myquery1)
print(x.deleted_count, " documents deleted.")
print()

# Delete All Documents in a Collection
# x = myEmp.delete_many({})
print(x.deleted_count, " documents deleted.")