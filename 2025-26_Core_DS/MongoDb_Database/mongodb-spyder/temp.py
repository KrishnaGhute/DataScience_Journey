import pymongo

client=pymongo.MongoClient('mongodb://127.0.0.1:27017/')

mydb=client['Employee']

information=mydb.empinfo

# for inserting one information use dictionary
records={
    'firstname':'Krishna',
    'lastname':'Ghute',
    'department':'Data Science'
    }

information.insert_one(records)

# for inserting multiple information use list with dictionary

records=[
    {
    'firstname':'Sharad',
    'lastname':'Pawar',
    'department':'IT'
    },
    {
    'firstname':'Rana',
    'lastname':'Pratap',
    'department':'Data Science'
    },{
    'firstname':'Nayan',
    'lastname':'Pinjare',
    'department':'Data Science'
    },{
    'firstname':'Rudra',
    'lastname':'Patil',
    'department':'IT'
    }
    ]
       
information.insert_many(records)