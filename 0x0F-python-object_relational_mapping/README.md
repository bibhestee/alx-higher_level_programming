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
