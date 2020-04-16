# Application Folder

## Purpose
The purpose of this folder is to store all the source code and related files for your team's application. Source code MUST NOT be in any of folder. <strong>YOU HAVE BEEN WARNED</strong>

You are free to organize the contents of the folder as you see fit. But remember your team is graded on how you use Git. This does include the structure of your application. Points will be deducted from poorly structured application folders.

## Please use the rest of the README.md to store important information for your team's application.



# Application Folder Structure:

django/ : our backend framework

django/lingo : our Django project

django/lingo/mainapp : the main Django app, all site related backend files shall reside here

django/lingoenv : virtual environment for Unix like system

django/venv_win : virtual environment for Windows

doing/tempaltes/mainapp : template html files for our front end team





# Setting Up For Development:

#### Prerequisites:

[Python 3.8](https://www.python.org/downloads/)

[pip3](https://pip.pypa.io/en/stable/installing/)

[virtualenv](https://virtualenv.pypa.io/en/latest/)

### Linux/MacOS:

clone this GitHub repo

``` git clone https://github.com/CSC-648-SFSU/csc648-04-sp20-team02.git ```

go to django folder

``` cd application/django```

activate venv

```source lingoenv/bin/activate```

make sure everything is installed on requirement.txt

```pip3 install -r requirement.txt```

make manage.py executable

``` chmod +x manage.py```

migrate database

```./manage.py migrate```

create super user to use the django admin panel

```./manage.py createsuperuser```



once those steps are done you can open django folder with your favorite python editor (personally i prefer [PyCharm](https://www.jetbrains.com/pycharm/))

once you have the project open you can either run the project in PyCharm or run the local server in terminal

```./manage.py runserver```



### Windows 

After cloning the repo I manage mostly everything on Pycharm including setting up virtual enviroment in File - Settings - Project:django - Project Interpreter and change the project interpreter to Python3.8 and use venv_win as venv path



**Happy Coding! :)**

