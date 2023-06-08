## Step 3:
In this step we are going to set up `crm/views.py`, create and setup `crm/urls.py`

Let's go to `crm/view.py` and copy & paste the following code into it
```commandline
from django.shortcuts import render, redirect
from django.http import HttpResponse

def index(request):
    return HttpResponse('Welcome to Django')
```

`crm/views.py` returns the web view, `crm/urls.py` create the `url` for that

Now go to the `cmr/urls.py` and copy and paste the following 
```commandline
from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.index, name='index'),
]
```

Now run the server by the following `command` to see the web page

```commandline
python manage.py runserver
```

Click on this link [http://localhost/test/](http://localhost/test/)

This is how it looks like

![ApparkyOutPut](../ss/ss.PNG)

Your basic app has been set up. Now let's go to next project
