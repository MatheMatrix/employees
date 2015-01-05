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



Cleaning Up
-----------

Finally, when done, deactivate your virtual environment::

  (.venv)$ deactivate
  $
