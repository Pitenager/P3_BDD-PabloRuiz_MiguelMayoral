# P3-PabloRuiz_MiguelMayoral

Pratice 3 for Verificación y Desarrollo (TDD module)

## Python Version

The program was coded in Python 3.6, so run it in same version.

## How it works

You can install the dependencies using:

```bash
make bootstrap
```

And execute test by 2 methods once you are in folder /tests (/project/mysite/analyzerapp/tests):

```bash
aloe features/tests.feature
```
This is to run all the selenium + aloe test automatically.
But you can execute the tests one by one by doing:
```bash
aloe features/name_of_the_feature.feature
```
You can find the names of the features into the /test folder.

You can execute the program using the next command from the directory where manage.py is located (P3_BDD-PabloRuiz_MiguelMayoral/project/mysite):

```bash
python manage.py runserver
```

