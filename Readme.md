## How to contribute
1.First clone the repo, [https://github.com/alice-njoroge/CCV](https://github.com/alice-njoroge/CCV)    
2.Make sure you have the right system dependencies.
The project depends on python3.6 and virtualenv. You can use pyvenv3 or even virtualenv or virtualenvwrapper  
3.Create a virtualenv. Creating one using pyvenv, `cd` into the project root and run   `python3.6 -m venv venv`  
You can install pyvenv 3 by typing `sudo apt install python3-venv` on the terminal.  
4.Update project dependencies by running the command `pip install -r requirements.txt`  
5.Copy `.env.example` file to `.env` by running the copy `cp .env.example .env`. This file keeps the project environment 
variables.It is not committed with Git.  
6.Run migrations to update the database schema by running the command `python manage.py migrate`  
7.Finally run server `python manage.py runserver`

To start developing on the project, we recommend vs code with python plugin and django templates plugin.

If you have any comments or issue, just open a github issue on the repo