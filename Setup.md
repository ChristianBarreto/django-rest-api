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

5.1 `$ python manage.py startapp poll`




----
`$ python manage.py migrate`
`$ python manage.py runserver`

5.1 Include app created in `mysite/settings.py` on `INSTALLED_APPS=[]`

# 6. Creating the App views 

6.1 Inside the new app created, create a new directory 'views' for multiple views
6.2 Delete the old `app/views.py`
6.3 Inside `app/views` create:
  - `fn_based_views.py`
  - `__init__.py`
6.4 On `fn_based_views.py`, create 

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
6.5 In `myapp/urls.py` import the new views and add to the `urlpatterns=[]`:

```
from app.views import (get_data, update_data, ...)

urlpatterns=[
  ...
  path('data/', get_data),
  path('data/update', update_data),
  ...
]
```

6.6 Comment out the CSRF middleware in `mysite/settings.py` or import `csrf_exempt` on urls and use in views functions.

6.7 To receive the json data in the endpoint:

```
import json

---on e.g POST view---
  body = json.loads(request.body)
```

