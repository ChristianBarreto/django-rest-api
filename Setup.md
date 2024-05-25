# How to setup a project from scratch

## 1. Verify requirements

1.1 `$ python --version`
1.2 `$ python -m django --version`

## 2. Installing Django if necessary
2.1 `$ python -m pip install Django`

## 3. Starting a project
3.1 `$ django-admin startproject mysite`

## 4. Running the project
4.1 `$ python manage.py runserver` + `0.0.0.0` (IP) + `8000` (PORT)

## 5. Creating an "App" (functionality)
Whenever we need to create a new functionality we create a new "App".

5.1 Create an app:
`$ python manage.py startapp myApp`
`$ python manage.py migrate`
`$ python manage.py runserver`

5.2 Include app created in `mysite/settings.py` on `INSTALLED_APPS=[]`

```
INSTALLED_APPS = [
    'myApp.apps.myAppConfig',
  ...
```

## 6. Logging
Django contains a simple pre configured logging, we just have the import the logging library and execute.

```
import logging
logging.waring("Hello world")
```

The logging handlers configures what does the logging does: log in the console, write in a file, or network.


## 7. Creating the App views 

7.1 Inside the new app created, create a new directory 'views' for multiple views
7.2 Delete the old `app/views.py`
7.3 Inside `app/views` create:
  - `fn_based_views.py`
  - `__init__.py`
7.4 On `fn_based_views.py`, create 

```
from django.http import JsonResponse

def get_data(request):
  res = {
    'success': True,
    'message': 'Function based view: get blogs'
  }
  return JsonResponse(res)

def create_data(request):
  if request.method == 'POST':
    res = {
      'success': True,
      'message': 'Function based view: get blogs'
    }
  else:
    res = {
      'success': False,
      'message': 'Function based view: Invalid request'
    }
  return JsonResponse(res)

...same for update and delete.
```
7.5 In `myapp/urls.py` import the new views and add to the `urlpatterns=[]`:

```
from app.views import (get_data, update_data, ...)

urlpatterns=[
  ...
  path('data/', get_data),
  path('data/update', update_data),
  ...
]
```

7.6 Comment out the CSRF middleware in `mysite/settings.py` or import `csrf_exempt` on urls and use in views functions.

7.7 To receive the json data in the endpoint:

```
import json

---on e.g POST view---
  body = json.loads(request.body)
```

## 8. Models
Models are classes that will create tables on DB.

8.1 Create models
```
# on app/models.py #

class User(models.Model):
  name = models.CharField(max_lenght=50)
  timestamp = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.name
  ...

class order(models.Model):
  order_name = models.CharField(max_lenght=50)
  timestamp = models.DateTimeField(auto_now_add=True)
  created_by = models.ForeignKey(User, on_delete=models.CASCADE)
  ...
```

8.2 Make migrations (create diff)
`$ python manage.py makemigrations`

8.3 Migrade (create DB based on diff)
`$ python manage.py migrate`

## 9 Queries
9.1 Import the model class in your view.
`from myApp.models import Users`

9.1 Create:
Instantiate and use methods.
```
u = Users(**userData) # spread operator **
u.save()
```

