# accountaboddies-back-end

Back-end repository of my Capstone Accountaboddies build in Django and Django REST.


### Due date 23th September. Updates comming. 
### App is not fully working yet!

The app is supposed to authenticate and provide the data requested from the Front-End (To be build in React.js)

## Installations and Configuration for the Django Rest Framework:
1. Clone the repository to your machine.
2. ``` cd accountaboddies-back-end ```
3. ```python -m venv AccountaboddiesEnv```
4. Activate the enviroment. Use ``` source ./AccountaboddiesEnv/bin/activate ```
5. ``` pip install -r requirements.txt ```



## Create Base Django Tables
1. Go to the repository on your machine.
2. Activate the enviroment. Use ``` source ./AccountaboddiesEnv/bin/activate ```
3. Make the migrations using:
``` python manage.py makemigrations  ```
4. Migrate them using:
``` python manage.py migrate ```

## Run the server
1. Go to the repository on your machine.
2. Activate the enviroment. Use ``` source ./AccountaboddiesEnv/bin/activate ```
3. Run the server using ```python manage.py run server ```
4. Now you are able to access the database and use POST, GET, PUT and DELETE requistions using the Browsable API. To do that access http://localhost:8000/.

## Helpers:
Database structure: https://dbdiagram.io/d/5f58064788d052352cb6724f
