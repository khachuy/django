# Start new project
## Install env and django
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
## Create project and start first project
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

## Update config of runserver
In manage.py add
```pydocstring
# Override default port and default_addr for `runserver` command
from django.core.management.commands.runserver import Command as runserver
runserver.default_addr = "localhost"
runserver.default_port = "8080"
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

# Create new app + URLs Mapping + Simple View
## Difference between project and app
 * Project: each project include many apps
 * App: each app execute difference work.

## Create new app
```shell script
django-admin startapp home
```
Add app to project
* In settings.py: add 'home' to list INSTALLED_APPS

Run command to update setting.py
```shell script
python manage.py migrate
```

## Request and response objects
Reference:
https://docs.djangoproject.com/en/3.2/ref/request-response/

## Create view
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

## Create urls mapping
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

# Models + Database
## 1. Models
A model is the single, definitive source of information about your data. It contains the essential fields and behaviors of the data you’re storing. Generally, each model maps to a single database table.

The basics:
* Each model is a Python class that subclasses [django.db.models.Model](https://docs.djangoproject.com/en/3.2/ref/models/instances/#django.db.models.Model).
* Each attribute of the model represents a database field.
* With all of this, Django gives you an automatically-generated database-access API; see [Making queries](https://docs.djangoproject.com/en/3.2/topics/db/queries/).

Example:
```pydocstring
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
```
Some technical notes:
* The name of the table, myapp_person, is automatically derived from some model metadata but can be overridden. See [Table names](https://docs.djangoproject.com/en/3.2/ref/models/options/#table-names) for more details.
* An id field is added automatically, but this behavior can be overridden. See [Automatic primary key fields](https://docs.djangoproject.com/en/3.2/topics/db/models/#automatic-primary-key-fields).
* The CREATE TABLE SQL in this example is formatted using PostgreSQL syntax, but it’s worth noting Django uses SQL tailored to the database backend specified in your [settings file](https://docs.djangoproject.com/en/3.2/topics/settings/).

Example change name table and change primary key column:
```pydocstring
class Person(models.Model):
    # column 'no' will primary key of table
    no = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

class Meta:
    # table name in db will save member
    db_table = 'member'
```

### 1.1 Fields
The most important part of a model – and the only required part of a model – is the list of database fields it defines. Fields are specified by class attributes. Be careful not to choose field names that conflict with the [models API](https://docs.djangoproject.com/en/3.2/ref/models/instances/) like clean, save, or delete.
#### 1.1.1 Field types
Each field in your model should be an instance of the appropriate Field class. Django uses the field class types to determine a few things:

The column type, which tells the database what kind of data to store (e.g. INTEGER, VARCHAR, TEXT).

The default HTML [widget](https://docs.djangoproject.com/en/3.2/ref/forms/widgets/) to use when rendering a form field (e.g. &lt;input type="text"&gt;, &lt;select&gt;).

The minimal validation requirements, used in Django’s admin and in automatically-generated forms.

Some commonly used fields:
* BigAutoField
* BooleanField
* CharField
* DateField
* DateTimeField
* FloatField
* IntegerField
* TextField
* TimeField

Django ships with dozens of built-in field types; you can find the complete list in the [model field reference](https://docs.djangoproject.com/en/3.2/ref/models/fields/#model-field-types). You can easily write your own fields if Django’s built-in ones don’t do the trick; see Writing [custom model fields](https://docs.djangoproject.com/en/3.2/howto/custom-model-fields/).
### 1.1.2 Field options
Each field takes a certain set of field-specific arguments (documented in the [model field reference](https://docs.djangoproject.com/en/3.2/ref/models/fields/#model-field-types)). For example, CharField (and its subclasses) require a max_length argument which specifies the size of the VARCHAR database field used to store the data.

Some commonly used field options:
* null
* blank
* choices
* default
* primary_key
* unique

You can find more information in [document](https://docs.djangoproject.com/en/3.2/topics/db/models/#field-options)

## 1.2 Relationships
Clearly, the power of relational databases lies in relating tables to each other. Django offers ways to define the three most common types of database relationships: many-to-one, many-to-many and one-to-one.

### 1.2.1 Many-to-one relationships
To define a many-to-one relationship, use django.db.models.ForeignKey.

ForeignKey requires a positional argument: the class to which the model is related.

Example:
```pydocstring
from django.db import models

class Car(models.Model):
    manufacturer = models.ForeignKey(
        'Manufacturer',
        on_delete=models.CASCADE,
    )
    # ...

class Manufacturer(models.Model):
    # ...
    pass
```

### 1.2.2 Many-to-many relationships
A many-to-many relationship. Requires a positional argument: the class to which the model is related, which works exactly the same as it does for ForeignKey, including recursive and lazy relationships.

Related objects can be added, removed, or created with the field’s [RelatedManager](https://docs.djangoproject.com/en/3.2/ref/models/relations/#django.db.models.fields.related.RelatedManager).

Example:
```pydocstring
from django.db import models

class Topping(models.Model):
    # ...
    pass

class Pizza(models.Model):
    toppings = models.ManyToManyField(Topping)
```

### 1.2.3 One-to-one relationships
A one-to-one relationship. Conceptually, this is similar to a ForeignKey with unique=True, but the “reverse” side of the relation will directly return a single object.

This is most useful as the primary key of a model which “extends” another model in some way; Multi-table inheritance is implemented by adding an implicit one-to-one relation from the child model to the parent model, for example.

One positional argument is required: the class to which the model will be related. This works exactly the same as it does for ForeignKey, including all the options regarding recursive and lazy relationships.

If you do not specify the related_name argument for the OneToOneField, Django will use the lowercase name of the current model as default value.

Example:
```pydocstring
from django.conf import settings
from django.db import models

class MySpecialUser(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    supervisor = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='supervisor_of',
    )
```

## 2. Database
Django officially supports the following databases:
* PostgreSQL
* MariaDB
* MySQL
* Oracle
* SQLite

## 3. Update model and database for project
### 3.1 Update database
This sample will setting config database with PostgreSQL

Install library support:
```shell script
pip install psycopg2
``` 
Update setting.py as below:
```pydocstring
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'django',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```
You can refer to other databases at [document](https://docs.djangoproject.com/en/3.2/ref/databases/#connecting-to-the-database)
### 3.1 Create models
In sample, i create app user and create models in this app.

I add urls of user to project.

* Warning: After create table or update table in models. run makemigrations (app) to create file migrations and migrate to django apply file migrations to database.
```shell script
python manage.py makemigrations user
python manage.py migrate
```

## 4. Test
Run server:
```shell script
python manage.py runserver
```
Access to [here](http://localhost:8080/user/insert) to insert member dummy.

Access to [here](http://localhost:8080/user) to get member dummy.
