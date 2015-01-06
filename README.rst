=================
 Running employee
=================

Setup
-----

First, you need to create a virtual environment and activate it.

::

  $ pip install virtualenv
  $ virtualenv .venv
  $ . .venv/bin/activate
  (.venv)$ 

Next, install requirment in the environment.

::

  (.venv)$ pip install -r requirements.txt

Now, install the employee into the virtual environment.

::

  (.venv)$ python setup.py install

Usage
-----

Simple employee manage system for course design, you can now play with it.
To see a list of commands available, run:

::

  (.venv)$ cliffdemo --help

You can use 'summary' to see list of all, 'detail' to see someone,
'add' to add someone, 'update' to update someone' data, 'query' to query
some key words, 'delete' to delete someone's data amd 'sort' to sort all
employees' data by one attribute.

Cleaning Up
-----------

Finally, when done, deactivate your virtual environment::

  (.venv)$ deactivate
  $
