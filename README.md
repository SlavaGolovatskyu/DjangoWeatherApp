DjangoWeatherApp that's web-application where you can find your city and watch the weather and temperature.
We take the api from openweathermap.org. We take from the user him entered city after this we do request on this api and receiving data.
Also we have a database for example we take sqlite3 where we have UserIP, City and Support.
To make it easy for users, we create an account for them based on their IP address and added their city in database.
After each request on the central page we received 2 city (user can save 2 city max in database).
And render page with that's data.
## Stack:
## Frontend: BootStrap
## Backend: (Python/Django)

## If you want starting my project you must do:
* Instaling Python
* git clone https://github.com/SlavaGolovatskyu/DjangoWeatherApp.git
* cd DjangoWeatherApp
* pip install django
* py manage.py makemigrations
* py manage.py migrate
* py manage.py runserver
## If you want you can also create a super user (admin)
* py manage.py createsuperuser
