# EMCALI test

## Usage
Object Mapping is based on a database whose data is presented in the order of the table defined below, please use a table as follows.

<img  width="180"  src="https://github.com/Juan8bits/emcali_test/blob/main/assets_readme/users_table.jpg"/>

Before starting it is assumed that there is already a database and user created, whose parameters are passed in the following environment variables.
* "EMCALI_MYSQL_USER" = MySQL user
* "EMCALI_MYSQL_PWD" = MySQL passwd
* "EMCALI_MYSQL_HOST" = MySQL host
* "EMCALI_MYSQL_DB" = MySQL database
* "EMCALI_ENV" = use "test" to drop all at the begining 

### How to launch it
```
$ EMCALI_ENV=test EMCALI_MYSQL_USER=emcali_test EMCALI_MYSQL_PWD=emcali_test_pwd EMCALI_MYSQL_HOST=localhost
EMCALI_MYSQL_DB=emcali_test_db EMCALI_TYPE_STORAGE=db python3 -m web_flask.myapp
```
