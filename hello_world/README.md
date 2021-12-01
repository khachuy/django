## Instructions
# 1. Install env and django
Create env
```shell script
python -m venv marble
```
Active env
```shell script
marble\Scripts\active
```
Install pip(if module not found)
```shell script
easy_install pip
```
Upgrade env
```shell script
pip install --upgrade pip setuptools wheel
```
Install django
```shell script
pip install django
```
Check version django
```shell script
django-admin --version
```
# 2. Create project and start first project
Create project hello_world
```shell script
django-admin startproject hello_world
```
* Start project
```shell script
cd hello_world
python manage.py runserver
```
* Start project with port
```shell script
cd hello_world
python manage.py runserver 8080
```

## Introduce about Django MTV pattern
* MTV(Model-Template-View) pattern is one pattern similar with MVC but have some little and tricky changes that are better match to Django web development.
* MTV pattern divides development works into three parts:
    * Model: connect project with database, probably like a Object/Relation Mapping(ORM)
    * Template: show data to users, usually by html pages or somethings like that.
    * View: finish the project logic part, and maybe call Model and Template sometimes by URL mapping.

## The Project Structure
* &lowbar;&lowbar;init&lowbar;&lowbar;.py: This is an empty file. The function of this file is to tell the Python interpreter that this directory is a package and involvement of this &lowbar;&lowbar;init&lowbar;&lowbar;.py file in it makes it a python project.
* setttings.py: It contains the Django project configuration. (Ex: database, timezone, ...)
* urls.py: URL is a universal resource locator, it contains all the endpoints that we should have for our website. It is used to provide you the address of the resources (images, webpages, websites, etc) that are present out there on the internet. In simpler words, this file tells Django that if a user comes with this URL, direct them to that particular website or image whatsoever it is.
* wsgi.py: When you will complete your journey from development to production, the next task is hosting your application. Here you will not be using the Django web server, but the WSGI server will take care of it.
* asgi.py: ASGI works similar to WSGI but comes with some additional functionality.  ASGI stands for Asynchronous Server Gateway Interface. It is now replacing its predecessor WSGI.

## Difference between project and app
 * Project: each project include many apps
 * App: each app execute difference work.

## Create app home
```shell script
django-admin startapp home
```
Add app home to project
* In settings.py: add 'home' to list INSTALLED_APPS

Run command to update setting.py
```shell script
python manage.py migrate
```

## Request and response objects
Reference:
https://docs.djangoproject.com/en/3.2/ref/request-response/

## Simple View And URLs Mapping
# Create view
In views.py of home. Add function index as below:
```pydocstring
from django.http import HttpResponse

def index(request):
    response = HttpResponse()
    response.writelines("Hello")
    response.writelines("<br/>")
    response.writelines("This first app django")
    return response
```

# Create urls mapping
Create urls.py in home as below:
```pydocstring
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
]
```

In urls.py of project(hello_world)
* Import include 
```pydocstring
from django.urls import path, include
```
* Add path home to urlpatterns
```pydocstring
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', include('home.urls')),
]
```
## Update config of runserver
In manage.py add
```pydocstring
# Override default port and default_addr for `runserver` command
from django.core.management.commands.runserver import Command as runserver
runserver.default_addr = "localhost"
runserver.default_port = "8080"
```