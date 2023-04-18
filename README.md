
# Teachbase API client

This service can help you to communicate with [Teachbase](https://go.teachbase.ru/) API.

You can:

- Get list of courses. `/teachbase/courses/`
- Get detail information of course. `/teachbase/courses/<int:course_id>/`
- Create new user in Teachbase. `/teachbase/users/create/`
- Get sessions of course. `/teachbase/courses/<int:course_id>/course_sessions/`
- Register user to course' session. `/teachbase/course_sessions/<int:session_id>/register/`

Also you can save course in db.

- Get list of courses from db. `/courses/`
- Get detail information of course. `/courses/<int:id>/`

## Configurations

* Python version: 3.10.
* Libraries: check [requirements.txt](https://github.com/etokosmo/teachbase/blob/main/backend/requirements.txt).

## Set `.env` file

- Write the environment variables in the `.env` file in the format KEY=VALUE

`SECRET_KEY` - A secret key for a particular Django installation. This is used to provide cryptographic signing, and should be set to a unique, unpredictable value.

`ALLOWED_HOSTS` - A list of strings representing the host/domain names that this Django site can serve. This is a security measure to prevent HTTP Host header attacks, which are possible even under many seemingly-safe web server configurations.

`DEBUG` - A boolean that turns on/off debug mode. If your app raises an exception when DEBUG is True, Django will display a detailed traceback, including a lot of metadata about your environment, such as all the currently defined Django settings (from settings.py).

`DATABASE_URL` - URL to db. For more information check [this](https://github.com/jazzband/dj-database-url).

`CLIENT_ID` - [Teachbase](https://go.teachbase.ru/) Public key.

`CLIENT_SECRET` - [Teachbase](https://go.teachbase.ru/) Secret key .

`TEACHBASE_API` - [Teachbase](https://go.teachbase.ru/) API endpoint.


## Launch

### With Docker

- Download code
- Install Docker
- Write the environment variables in the `.env` file in the format KEY=VALUE
- Create images and run container with command:
```bash
docker compose up --build
```
- Open `localhost:8000`

### Local server

- Download code
- Through the console in the directory with the code, install the virtual environment with the command:
```bash
python3 -m venv env
```

- Activate the virtual environment with the command:
```bash
source env/bin/activate
```

- Install the libraries with the command:
```bash
pip install -r requirements.txt
```

- Write the environment variables in the `.env` file in the format KEY=VALUE

- Create your database with the command:
```bash
python manage.py makemigrations
python manage.py migrate
```

- Run local server with the command (it will be available at http://127.0.0.1:8000/):
```bash
python manage.py runserver
```
