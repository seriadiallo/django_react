## Django react for beginners
#### this project is for beginners seeking for a quick start project django with react

process of installation

     git clone https://github.com/seriadiallo/django_react.git
##### Move into the project directory
      cd django_react
##### Create a python virtual enviroment
    virtualenv venv
##### Activate the venv
      source venv\bin\activate     #!--- Ubuntu
      venv\Scripts\activate       #!--- Windows
      
##### Install all the python dependencies
      pip install -r requirements.txt
### configuration of the project
 1) create a database (postgres, mysql, oracle...)
 2) create a file named settings.ini at the root of the project
 3) copy information from settings.example.ini and change information there according to your database and your generated key
 
 then
 ##### Execute the migrations
      python manage.py migrate
##### seed your database to get some test data
      python manage.py seed customers 15
##### run your server
        python manage.py runserver

#### start a new console an go to 'frontend' directory and install 'react' dependacies  

        yarn or yarn install 
##### start your react server
        yarn start

## Now, go through the project
