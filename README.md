# Django-CRM-Python-APPARKY


> In this Django Project we have designed a basic CRM system 
> 
> We have agreed the terms and conditions of [Bootstrap](https://getbootstrap.com/) and have used free [Bootstrap](https://getbootstrap.com/) Templates in our work.
> 
> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Bootstrap is a free, open source front-end development framework for the creation of websites and web apps. 
> Designed to enable responsive development of mobile-first websites, Bootstrap provides a collection of syntax for template designs.
> 
> 
> 

## Step 1:

Create a Folder first and open it from `CMD` (Windows) or your native `terminal`

Install [`Django`](https://www.djangoproject.com/) to your system by using this `command`

```commandline
pip install django
```

We have shared `requirement.txt` file with this repo. You can also install all required libraries by following this command

```commandline
pip install -r requirement.txt
```

If done, create a new project file by typing this

```commandline
django-admin startproject YOURPROJECTNAME .
# In this project is the name of it is MyCRM.
```

That's all. All your Native file will be created to yhe folder, and you are ready to start

## Step 2:

Now open the project file with the `IDLE` you like to use

Open the `terminal` from your `IDLE` and type 

```commandline
python manage.py runserver
```

> And you are good to go. Open this link form you browser [http://localhost:8001/](http://localhost:8001/)
> 
> You will see the `server` is running
> 
> 

Now Let's Create an application for our Ecommerce Page.

For Creating an Application type this to your `terminal`

```commandline
python manage.py startapplications YOURAPPLICATIONNAME
# In this project your application name is crm
```

You can see now a new folder has been created to your project directory

Now go to `MyCRM/settings.py` file you will find some list of installed application there

```commandline
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',    
]
```

add the application name and save the file

```commandline
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'crm', # app name has to insert here to make it work
]
```

like this

By Default Django use `SQLite3`, but in this project we are going to use `MySQL` in stade of `SQLite3`



























-------------------
> 
> To get more interesting projects follow our GitHub page at [Here](https://github.com/Apparky)
> 
> To get more interesting projects follow our Bitbucket page at [Here](https://bitbucket.org/apparky-web/workspace/overview)
> 
> To know more about [__APPARKY__](https://apparky.vercel.app/) Click [Here](https://apparky.vercel.app/)

