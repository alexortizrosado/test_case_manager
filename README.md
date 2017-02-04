Test Case Manager
================
Test case management application written in Python using the Flask microframework.

Currently provides an api endpoint for `project`.

## Setup
1. Install prerequisites
```
$ git clone https://github.com/alexortizrosado/test_case_manager.git
$ cd test_case_manager
$ virtualenv ~/.virtualenv/test_case_manager && source ~/.virtualenv/test_case_manager/bin/activate
$ pip install -r requirements.txt
```

2. Setup the database
```
$ python test_case_manager/manage.py db migrate
```

3. Start the server
```
$ python test_case_manager/app.py
```

4. Open a browser and navigate to
[http://localhost:8888/api/](http://localhost:8888/api/)

