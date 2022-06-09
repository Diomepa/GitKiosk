## What is this
This is somewhat random sample of django 4 and drf usage
There are plenty of things which could and should be added

### Very short instructions

#### Run in development mode with bound volumes
```docker-compose -d --build```

Optionally load some demo data (same as the test data)
```docker-compose run --rm  backend bash -c "./scripts/dev.load_demo_data.sh"```  
Note that the services must be running (or rather database must be up and migrations need to have run)

Now you should have some data, including user with username `superadmin` and password `bananapaper`

#### Exploring the app

Visiting `http://localhost:8000/` should redirect you to the not entirely
helpful at this point API documentation 

Naturally admin can be found at `http://localhost:8000/admin`

#### User management
Currently there is no API for registering users. A superuser can be created using  
```docker-compose run --rm backend bash -c "python manage.py createsuperuser"```


#### Running existing tests 
Tests could be run by  
``` docker-compose run --rm backend bash -c "python manage.py test -v 2"```

There are some tests, however a lot are to be added at future date

#### Running in "production mode"
Currently, this is undone, however to run self-contained image (not just bound):  
```docker-compose  -f .\docker-compose.yml up  -d --build```

This is to be added at future iterations, with proper settings, production server etc. 
