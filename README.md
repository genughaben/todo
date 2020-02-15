Dockerized Flask + PostgreSQL Starter Code.

# Requirements:
* MacOS or Ubuntu
* Docker deamon installed and running

# How to start:

```
>mkdir db # create db folder
>docker-compose build # build project
>docker-compose up # starting project
```


Services is going to be accessable in browser via: localhost:7000/


# Interactive Session for testing and inspecting:

```
> docker-compose run app python3 # opens interactive session in container
> from app.app import app # or more: (, db, Person) helps you interact with the system
```

You can do queries on Person table:

```
Person.query.all() # get all
Person.query.first() # get first record
Person.query.count() # get total count of all rows
Person.query.filter_by(name="Frank") # select person by name
person = Person(name="Bob")
db.session.add(person) # or db.session.add_all([person1, person2, ...]) for arrays to add person; pending changes
db.session.commit() # finally executes adding persons; commits transaction
```

# Explanation so Models:

## Common Model.query-examples
Model.query => provides all SELECT queries
Model.query.filter_by(..) => select * where (...)
Model.query.count => select count(*)
Model.query.filter(Model.attribute = 'value') => select * from xy where (..)
Model.query.filter(Model.attribute = 'value', Model2.attribute == 'value') => select * from xy, ab where (conditions on multiple tables)
Model.query.get(1) => get by primary key

Alternative: db.session.query(Model).join(Team)

## Bulk operations:
Model.query.filter(..).delete()

## Method chaining:
Model.query.filter(...).first() => like chaining where clauses
Model.query.join(...).filter_by().all() => like chaining where clauses

## INSERT, UPDATE, DELETE

user = User(name="John")

*INSERT:*
session.add(user)

*UPDATE:*
user.name = 'Bob'

*DELETE:*
session.delete(user)

**You can now either, commit or rollback:**
db.session.commit()
db.session.rollback()


# Enter database:

Start the system if you have not already:

```
> docker-compose up
```

Enter the db container executing psql using:

```
>  docker exec -it example_db_1 psql -U postgres
```


# Tips

* Update requirements.txt from pipenv:

```
> pipenv lock -r > requirements.txt`
```