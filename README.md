
# Best-Fit-Job-ML

> This is Machine Learning part of [Best-Fit-Job](https://github.com/RajithaKumara/Best-Fit-Job) project. Best-Fit-Job makes a platform for job seekers to find jobs and employers to offer jobs easily. In order to fulfil this task, this system has portals for job seekers and people who offer jobs. Job seekers are able to add their knowledge, skills, attitudes and other extra attributes to their account. On the other hand, employers can add their job opportunities with expected skills. The output of this system is matching job opportunities with job seekers profiles and sending notifications to both parties.

## Prerequisites
•	Python version 3.6 installed locally (installation guides for [OS X](http://docs.python-guide.org/en/latest/starting/install3/osx/), [Windows](http://docs.python-guide.org/en/latest/starting/install3/win/), and [Linux](http://docs.python-guide.org/en/latest/starting/install3/linux/))

•	Pipenv installed locally ([installation guides](http://docs.python-guide.org/en/latest/dev/virtualenvs/))

## Usage
First clone the repository.
``` bash
$ git clone https://github.com/RajithaKumara/Best-Fit-Job-ML
```
Go to inside directory.
``` bash
$ cd Best-Fit-Job-ML
```
Install dependencies.
``` bash
$ pip install -r requirements.txt
```
Install virtualenv.
``` bash
$ pipenv install
```
Create model tables in database. [Read more...](https://docs.djangoproject.com/en/2.0/intro/tutorial02/#database-setup)
``` bash
$ python manage.py migrate
```
Start Django development server at localhost:8000 (default). [Read more...](https://docs.djangoproject.com/en/2.0/intro/tutorial01/#the-development-server)
``` bash
$ python manage.py runserver
```
or

Start the development server using Heroku CLI. [Read more...](https://devcenter.heroku.com/articles/getting-started-with-python#run-the-app-locally)
``` bash
# on Microsoft Windows system
$ heroku local web -f Procfile.windows
#or
$ python manage.py runserver

#on a Unix system
$ heroku local web
#or
$ gunicorn app.wsgi
```
