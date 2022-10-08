# 0x0F. Python - Object-relational mapping

## Concepts

- Python

- OOP
- SQL
- MySQL
- ORM
- SQLAlchemy

## INSTALLATIONS
Install MySQLdb module version 2.0.x
For installing MySQLdb, you need to have MySQL installed

### MySQL
```
$ sudo apt update
$ sudo apt install mysql-server
$ service mysql start [ To start the server in as container-on-demand root/root]
```

### MySQLdb
```
$ sudo apt-get install python3-dev
$ sudo apt-get install libmysqlclient-dev
$ sudo apt-get install zlib1g-dev
$ sudo pip3 install mysqlclient
...
$ python3
>>> import MySQLdb
>>> MySQLdb.version_info 
(2, 0, 3, 'final', 0)
```

### Install SQLAlchemy module version 1.4.x
```
$ sudo pip3 install SQLAlchemy
...
$ python3
>>> import sqlalchemy
>>> sqlalchemy.__version__ 
'1.4.22'
```


## USEFULL INFORMATIONS 

### Process to Create a new table class
- import create_engine, declarative_base
- Create a the table class that inherit from declarative_base class
    ```
        Base = declarative_base
        Table(Base)...
    ```
- Create an Engine that activate your orm to database
    for sqlalchemy
    `engine = create_engine('myslq+myslqdb://<user>:<pass>@localhost/<db>)`

- Start the engine to create the table and it ignores if its created already
    `Base.metadata.create_all(engine)`

### Process to Initiate a session
- After the successful creation of engine then create a session instance
    ```
    Session = sessionmaker()
    session = Session(engine)`
    or 
     first configure the session class then create an instance
    ```
    Session = sessionmaker(bind=engine)
    session = Session()
    ```
- Or Use `Session.configure(bind=engine)` if engine was created later

