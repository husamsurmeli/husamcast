
### TO EXECUTE THE TESTS
    python test.py

is enough. That's goodnews. For the reviewer's benefit database is already configured to my Heroku Database.
Badnews is it may require couple seconds more compared to local database. But thinking of `create database`,`init`, `migrate`, `upgrade` commands' execution time it is still better. 

### TO RUN THE API
    `flask run`
Though, since there is no frontend you can see the health of the api only with one route. @app.route('/')

JWT for each role is stored in `models.py`

