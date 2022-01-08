# Das Motorrad - Django
A web application based on Django Framework.


## At a Glance
- [Prerequisites](#prerequisites)
- [Django: Essential Training](#django-essential-training)
- [RESTFUL API's](#restful-apis)
- [Security Practices](#security-practices)
- [Useful Resources](#useful-resources)

### Prerequisites
##### Technologies
* [Python](https://www.python.org/): Version 9
* [Django](https://www.djangoproject.com/download/): Version 4.0
* [Editor](#useful-resources): Visual Code, PyCharm, or an editor of your choice.
##### Security
* Turn off `DEBUG` on `Production` environment.
* Move out `SECRET_KEY` from `settings.py` and replace it with Django's `get_random_secret_key()`.
    ```
    from django.core.management.utils import get_random_secret_key
    SECRET_KEY = get_random_secret_key()
    ```
* If the `SECRET_KEY` is accidentally pushed to production, generate new secret key and do not use the compromised ones. (see: [Secure Your Secret Key](#django))

### Django Essential Training
#### Django's Rule of Thumb
* Django follows MVT (Model-View-Template) Framework.
* Each page is separated through Django's `App`. (e.g. `home`)
* Each `App` contains `Template` folder that is rendered from the `View`.
* A Django `App` must be self-contained, meaning, independent and can be reused to other Django projects without a hitch. see `home/urls.py` for more details.


#### Django Fundamental Commands
##### Create a Project
```
# Create a Project: django-admin startproject <project> <path>
# e.g. django-admin startproject dasmotorrad .
```
##### Start the Project
```
# python manage.py runserver
```

##### Create New App and adding to Project. 
```
# django-admin startapp <app>
# project > settings.py > installed apps > add <app> 
# project > urls.py > url patterns > add <view>
```

##### ORM - Object Relational Mapping
```
ORM: Classes > MakeMigrations > Migrate > Database
```

##### Django Shell
For more information, visit: [Django Queries](#django)
```
>>> from motorräder.models import Motorräder 

# Select Object
>>> motorcycles = Motorräder.objects.get(pk='1')

# Query values from an Object
>>> motorcycles.brand

# list all objects from a Database
>>> Motorräder.objects.all()
<QuerySet [<Motorräder: Motorräder object (1)>]>

# Create a new object
>>> new_motorcycles = Motorräder.objects.create(brand, origin, year, history)

# Filter & Exclude Query
>>> Motorräder.objects.filter(brand__startswith='B')
>>> Motorräder.objects.filter(origin__icontains='Germany')
>>> Motorräder.objects.exclude(origin__icontains='Germany')
>>> Motorräder.objects.filter(year__icontains='19').exclude(origin__icontains='Germany')
```

##### Class-based Views
For more information, visit: [Django Class-based Views](#django)
```
from django.views.generic import ListView

class MotorräderView(ListView):
    model = Motorräder # from models.py
    context_object_name = "motorräder" # a variable that is called from an HTML View
    template_name = "motorräder/motorräder.html" # an HTML View to render the model
```

### RESTFUL API's
| API  | Description |
| ---- | ----------- |
| motorräder/ | Returns a list of motorcycle companies |
| motorräder/\<company> | Returns a list of motorcycles from a given \<company> |
| motorräder/\<company>/\<motorrad>  | Returns a motorcycle model from a specific \<company>  |

### Unit Tests

### Security Practices

### Building Django Projects with Bulma CSS

### Useful Resources
#### Editor
* [Microsoft Visual Code](https://code.visualstudio.com/)
* [Jetbrains PyCharm](https://www.jetbrains.com/pycharm/)

#### Django
* [Documentation](https://docs.djangoproject.com)
* [Django Secret Key](https://docs.gitguardian.com/secrets-detection/detectors/specifics/django_secret_key)
* [Secure your Secret Key](https://github.com/django/django/blob/1.10/django/core/management/utils.py#L81)
* [Essential Training](https://www.linkedin.com/learning/django-essential-training/)
* [Django Queries](https://docs.djangoproject.com/en/4.0/topics/db/queries/#retrieving-all-objects)
* [Django Class-based Views](https://docs.djangoproject.com/en/4.0/topics/class-based-views/)

#### Github
* [Secrets API Management](https://blog.gitguardian.com/secrets-api-management/?utm_source=product&utm_medium=product&utm_campaign=white_knight_v2)
* [Project Versions](VERSIONS.md)
* [What to do when you commit to the wrong git branch](https://www.clearvision-cm.com/blog/what-to-do-when-you-commit-to-the-wrong-git-branch/)

* [How to Create a Free Website Using GitHub Pages](https://www.youtube.com/watch?v=o5g-lUuFgpg)
  * [Github Pages deployment with NoJekyll](https://github.com/leo-jp/sandbox). This sample repository shows how to ignore Jekyll excluding node_modules and including specific modules (e.g. bootstrap) as well.

* [Git: When to Ignore Files](https://linuxize.com/post/gitignore-ignoring-files-in-git/) 