## Instructions
# 1. Install env and django
Create env
```shell
python -m venv marble
```
Active env
```shell
marble\Scripts\active
```
Install pip(if module not found)
```shell
easy_install pip
```
Upgrade env
```shell
pip install --upgrade pip setuptools wheel
```
Install django
```shell
pip install django
```
Check version django
```shell
django-admin --version
```
# 2. Create project and start first project
Create project hello_world
```shell
django-admin startproject hello_world
```
* Start project
```shell
cd hello_world
python manage.py runserver
```
* Start project with port
```shell
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
* __init__.py: This is an empty file. The function of this file is to tell the Python interpreter that this directory is a package and involvement of this __init.py_ file in it makes it a python project.
* setttings.py: It contains the Django project configuration. (Ex: database, timezone, ...)
* urls.py: URL is a universal resource locator, it contains all the endpoints that we should have for our website. It is used to provide you the address of the resources (images, webpages, websites, etc) that are present out there on the internet. In simpler words, this file tells Django that if a user comes with this URL, direct them to that particular website or image whatsoever it is.
* wsgi.py: When you will complete your journey from development to production, the next task is hosting your application. Here you will not be using the Django web server, but the WSGI server will take care of it.
* asgi.py: ASGI works similar to WSGI but comes with some additional functionality.  ASGI stands for Asynchronous Server Gateway Interface. It is now replacing its predecessor WSGI.
