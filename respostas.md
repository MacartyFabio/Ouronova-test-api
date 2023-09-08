## What is Python? What are the benefits of using Python?

Python is a high-level programming language known for its simplicity and readability. Some benefits of using Python include clear and concise syntax, a broad standard library, modularity, the ability to integrate with other languages, support for object-oriented programming, a large community, and being open source.

## What is dynamic typing in a programming language?

In a dynamically typed language, the type of a variable is determined at runtime rather than at compile time. This means you can assign different data types to a variable throughout the program.

## What is an interpreted language?

An interpreted language is one where the source code is executed line by line by an interpreter rather than being compiled into machine code.

## What is PEP 8, and why is it important?

PEP 8 is a style guide for Python code that defines formatting and style conventions. It is important because it helps maintain Python code readability and consistency, making it easier for developers to collaborate on projects.

## What is scope in Python?

Scope in Python refers to the visibility and accessibility of variables in different parts of a program. There are local and global scopes.

## What are lists and tuples? What is the main difference between the two?

Lists and tuples are data structures in Python. The main difference is that lists are mutable, whereas tuples are immutable.

## What are common built-in data types in Python?

Some common built-in data types in Python include integers, floats, strings, lists, tuples, dictionaries, and sets.

## What does 'pass' mean in Python?

'Pass' is an empty statement in Python that does nothing. It is often used as a placeholder when a code block is required for syntactical reasons but no actual action is desired.

## What are modules and packages in Python?

Modules are Python files containing function, variable, and class definitions. Packages are directories that contain related modules and an **init.py** file. They are used for code organization and reuse.

## What are global, protected, and private attributes in Python?

In Python, the convention is to use a single underscore (_) as a prefix for protected attributes and double underscores (__) for private attributes. Global attributes are defined outside of any function or class, but it's more of a convention defined by the community.

## What is the purpose of 'self' in Python?

'self' is used as a parameter in instance methods of a class to reference the current instance of the class. It is used to access attributes and methods of the instance.

## What is 'init'?

'init' is a special method (also known as a "constructor") used to initialize objects of a class.

## What are 'break,' 'continue,' and 'pass' in Python?

These are jump statements used in loops. 'Break' is used to exit a loop, 'continue' is used to skip the current iteration and move to the next one, and 'pass' is an empty statement used as a placeholder.

## What are unit tests in Python?

Unit tests are tests that verify the functionality of individual units of code, such as functions or methods, to ensure they produce correct results.

## What is a docstring in Python?

A docstring in Python is a documentation string embedded in the source code of a module, class, function, or method. It is used to document the purpose, behavior, and usage of that code element. Docstrings are intended to be read by humans and do not affect program execution.

## What is slicing in Python?

Slicing in Python refers to extracting specific parts of a sequence (like a string or a list) using indices.

## Explain how you can make a Python script executable on Unix?

You can make a Python script executable on Unix by adding a shebang line (e.g., #!/usr/bin/env python3) at the beginning of the file and giving the file execute permission using the chmod +x filename.py command.

## What is the difference between arrays and lists in Python?

In Python, a "list" is a built-in data type, while "array" typically refers to NumPy arrays, which are more efficient for numerical calculations.

## How is memory managed in Python?

Python uses an automatic memory management system that includes a garbage collector. Objects that are no longer referenced are automatically released.

## What are Python namespaces, and why are they used?

Namespaces in Python are containers that hold variable and function names. They are used to avoid naming conflicts between different parts of the code.

## What is scope resolution in Python?

Scope resolution in Python refers to the process of determining from which namespace a variable or function is accessed.

## What are decorators in Python?

Decorators are a design pattern in Python. They are functions that can be used to modify the behavior of other functions or methods. They are commonly used to add additional functionality at runtime and are indicated by the @decorator syntax.

## What are Dict and List comprehensions?

Dict and list comprehensions are concise constructs for creating dictionaries and lists more efficiently. Here's an example of their basic syntax:

- Dictionary comprehension: `{key: value for element in iterable}`
- List comprehension: `[expression for element in iterable]`

## What is a lambda function in Python, and why is it used?

A lambda function is used to create anonymous (unnamed) functions in Python. It is useful when you need a simple function for a single task.

## How do you copy an object in Python?

You can copy an object in Python using methods like `copy.copy()` (shallow copy) or `copy.deepcopy()` (deep copy) from the `copy` module.

## What is the difference between `xrange` and `range` in Python?

In older versions of Python, `xrange` was a more memory-efficient version of `range`, saving memory. However, in Python 3, `range` was optimized, and `xrange` no longer exists.

## What are pickling and unpickling?

Pickling and unpickling are terms used for serializing and deserializing Python objects. They are used to convert objects into a representation that can be stored in a file or transmitted over the network and then recreate the original object from that representation.

## Define GIL (Global Interpreter Lock).

GIL, or Global Interpreter Lock, is a mutual exclusion mechanism in CPython that allows only one Python execution thread at a time. This can limit Python's ability to take full advantage of multi-core systems in some situations.

## Define PYTHON

PATH.

PYTHONPATH is an environment variable that specifies the directories where the Python interpreter should look for imported modules and packages.

## Define PIP.

PIP is a command-line tool used for installing, updating, and managing Python packages. It is widely used to add functionality to Python projects, similar to npm for Node.js and composer for PHP.

## Are there tools for bug identification and static analysis in Python?

Yes, there are several tools for bug identification and static analysis in Python, such as PyLint, Flake8, mypy (for static type checking), and integrated tools in IDEs like PyCharm.

## Differentiate between shallow and deep copies.

A shallow copy of an object creates a new object that is a copy of the original object's elements but does not create copies of nested elements (e.g., objects in a list). A deep copy creates a copy of the original object and all nested data structures.

## What is the main function in Python, and how do you invoke it?

The main function in Python is typically named `main()`. You can invoke it simply by calling it in your code, such as `main()`.

## Write a Python function that accepts a variable number of arguments.

```python
def my_function(*args):
    for arg in args:
        print(arg)

my_function(1, 2, 3, 4)  # Accepts any number of arguments.
```

## Write a program that takes a sequence of numbers and checks if all numbers are unique.

```python
def is_unique(seq):
    return len(seq) == len(set(seq))

numbers = [1, 2, 3, 4, 5]
result = is_unique(numbers)
print(result)  # True
```

## Write a program to count the occurrences of each character in a given text file.

```python
file = open("file.txt", "r")
text = file.read()
counter = {}

for character in text:
    if character in counter:
        counter[character] += 1

file.close()

for character, count in counter.items():
    print(f"'{character}': {count}")
```

## Write a program to find pairs in a given array whose sum equals a target value.

```python
def find_pairs_sum(arr, target):
    pairs = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                pairs.append((arr[i], arr[j]))
    return pairs

array = [2, 4, 3, 5, 6, 7]
target = 9
pairs = find_pairs_sum(array, target)
print(pairs)  # [(2, 7), (4, 5)]
```

## Write a program to add two positive integers without using the addition operator.

```python
def sum_without_operator_plus(a, b):
    while b != 0:
        carry = a & b
        a = a ^ b
        b = carry << 1
    return a

result = sum_without_operator_plus(5, 7)
print(result)  # 12
```

## Write a program to solve the given equation, assuming a, b, c, m, n, and o are constants.

```python
A = 2
B = 3
C = 5
M = 4
N = 6
O = 8

result = (A + B - C) * (M / N) + (O ** 2)
print(result)
```

## Write a program to match a string that has the letter 'a' followed by 4 to 8 'b's.

```python
import re

text = "abbbbbbb"
pattern = "ab{4,8}"
matched = re.match(pattern, text)

if matched:
    print("Match found.")
else:
    print("No match found.")
```

## Write a program to convert dates from the yyyy-mm-dd format to the dd-mm-yyyy format.

```python
from datetime import datetime

date_str = "2023-09-05"
date_obj = datetime.strptime(date_str, "%Y-%m-%d")
formatted_date = date_obj.strftime("%d-%m-%Y")

print(formatted_date)  # 05-09-2023
```

## Write a program to merge two different dictionaries. When merging, if you encounter the same keys, you can add the values of those keys. Produce the new dictionary.

```python
dictionary1 = {"a": 1, "b": 2, "c": 3}
dictionary2 = {"b": 4, "d": 5, "e": 6}

dictionary1.update(dictionary2)
print(dictionary1)
```

## How can you access the dataset from a publicly shared CSV file stored on Google Drive?

```python
import pandas as pd

url = "https://drive.google.com/.../view?usp

=sharing" 
dataframe = pd.read_csv(url)
```

# DJANGO

## Explain the Django architecture:

The Django architecture follows the Model-View-Controller (MVC) pattern but uses the nomenclature: Model-View-Template (MVT).

Model: Represents data and business logic. Models define the database structure.
View: Handles presentation logic and processes client requests. Views render templates.
Template: Defines the output's appearance. Templates include placeholders filled with data by views.

## Explain the project directory structure in Django:

The typical directory structure includes folders such as:

manage.py: A script for interacting with the Django project.
project_name/: The root folder of the project.
settings.py: Project settings.
urls.py: URL definitions for the project.
wsgi.py: Entry point for web servers.
apps/: Directory for project applications.
media/: Location for storing media files.
static/: Location for static files (CSS, JS, images).
templates/: Directory for HTML templates.
venv/: Virtual environment (optional).

## What are models in Django?

Models in Django are Python classes that define the structure of database data. They represent tables in the database and define the fields and relationships between these tables.

## What are templates in Django or Django's template language?

In Django, templates are used to define the visual presentation of web pages, separating business logic from the user interface. These templates, written in Django's template language, allow dynamic data insertion and facilitate the development of dynamic and reusable web pages.

## What are views in Django?

In Django, "views" are components that process client requests and return responses, playing a central role in a web application's logic.

## What is Django ORM?

Django ORM (Object-Relational Mapping) is a part of Django that allows you to interact with the database using Python objects. It abstracts SQL queries away, enabling you to work with databases in a more object-oriented manner.

## Define static files and explain their uses?

Static files in Django are files that are not generated dynamically by the web server. They include CSS, JavaScript, images, and other resources served directly to clients to enhance the user experience. These files are stored in the project's static folder.

## What is Django Rest Framework (DRF)?

Django Rest Framework is a third-party library that simplifies the creation of RESTful APIs in Django projects. It provides tools for data serialization, authentication, authorization, and more.

## What is Django-admin and Manage.py, and explain their commands?

django-admin: A command-line tool for various Django project management tasks.
manage.py: An automatically generated Python script that simplifies interaction with the Django project, including running management commands like runserver, makemigrations, migrate, etc.

## What is the Jinja template engine?

Jinja is a template engine used in Python web projects, including Django. It allows you to create HTML templates with placeholders (tags) that can be dynamically filled with data.

## What are Django URLs?

Django URLs are mappings between request URLs and view functions. They determine how client requests are routed to the correct views.

## What's the difference between a project and an app in Django?

A Django project is a collection of configurations and applications that form a complete web application. A Django app is a reusable part of a project with specific functionality, such as user authentication, a blog, or a forum.

## What are the different model inheritance styles in Django?

Django supports three model inheritance styles: single-table inheritance, multi-table inheritance, and abstract inheritance.

## What are Django signals?

Django signals are a way to allow certain pieces of code to be executed in response to specific events. Signals are used to decouple different parts of code and enable applications to respond to events in other applications.

## Explain caching strategies in Django?

Django offers support for various caching strategies, including page caching, fragment caching, object caching, and database caching. These strategies allow you to cache data to improve performance and reduce server load.

## Explain user authentication in Django?

User authentication in Django involves creating, managing, and authenticating user accounts. Django provides a built-in authentication system that includes features like login, logout, user registration, and password management.

## How to configure static files?

To configure static files in Django, you need to specify the folder where static files are stored and set up the URL for serving these files. This is done in the settings.py file by specifying STATIC_URL and STATIC_ROOT.

## Explain the Django Response lifecycle?

The Django Response lifecycle begins when a view processes a request and returns a response. The response goes through various middlewares, which can modify it or add information. Finally, the response is sent back to the client.

## Which databases are supported by Django?

Django supports several relational databases, including PostgreSQL, MySQL, SQLite, and Oracle, among others. Additionally, there are third-party adapters for other databases.

## What is the purpose of a session framework?

The session framework in Django is used to track and store temporary user-related information in a web application, such as authentication, preferences, and shopping cart state, allowing customization of the user experience.

## What is Middleware's purpose in Django?

Middleware in Django is used to globally process requests and responses before they reach views. It can be used to add functionality such as authentication, compression, security, and more.

## What is context in Django?

Context in Django is a Python dictionary that contains information made available to templates during the rendering process. It allows variables to be accessed in templates.

## What is the django.shortcuts.render function?

django.shortcuts.render is a function that renders an HTML template with context data and returns an HTTP response.

## What does the settings.py file signify?

The settings.py file contains the global settings for the Django project, including database settings, security settings, caching settings, and more.

## How to retrieve all items from a Model?

You can retrieve all items from a model by using a model query, for example: MyModel.objects.all().

## How to filter items in the Model?

You can filter items in the model using the filter() or get() method to specify query conditions, for example: MyModel.objects.filter(key='value').

## How to use file-based sessions?

You can set up file-based sessions in Django by configuring the session storage to use the django.contrib.sessions.backends.file.FileSession class.

## What is a mixin?

A mixin is a class that provides additional functionality to other classes. In the context of Django, mixins are often used to add methods or behaviors to views.

## What is a Django Field Class?

A Django Field Class is a definition that specifies the data type and options of a field in a Django model.

## Why is permanent redirection not a good option?

Permanent redirection (HTTP status code 301) is not a good option when you want to maintain the flexibility to change the target URL in the future. It is appropriate when you are certain that the URL will not change.

## Difference between Django OneToOneField and ForeignKey Field?

OneToOneField: Establishes a one-to-one relationship between two models, meaning each record in the related model is associated with a single record in the current model.
ForeignKey: Establishes a many-to-one relationship (i.e., multiple records in the current model can point to the same record in the related model). A ForeignKey creates a foreign key field that stores the primary key of the related record.

## How can you combine multiple QuerySets in a View?

You can combine multiple QuerySets in a view using methods like union(), intersection(), difference(), provided by the Django ORM. These methods allow you to merge the results of

 multiple queries into a single query.

## How to retrieve a specific item in the Model?

To retrieve a specific item from a model in Django, you can use the get() method of the model, specifying query criteria. For example: MyModel.objects.get(key='value').

## How to obtain the SQL query from the queryset?

You can obtain the SQL query from a Django queryset using the str() method on the queryset. For example: str(MyModel.objects.filter(field='value').query).

## What are the ways to customize Django's admin interface functionality?

There are several ways to customize Django's admin interface, including:

1. Subclassing AdminSite to create a custom admin site.
2. Creating custom admin classes for models using admin.ModelAdmin.
3. Customizing admin templates.
4. Adding custom functionality using JavaScript and CSS.

## Difference between select_related and prefetch_related?

select_related and prefetch_related are methods that allow you to optimize related database queries in Django:

1. select_related: Performs an SQL "join" to fetch related data along with the main object in a single query. It is used for ForeignKey and OneToOneField fields.
2. prefetch_related: Performs additional queries to retrieve related objects after the main query. It is used for ManyToManyField and reverse ForeignKey fields.

## Explain Django ORM's Q objects?

Q is a Django ORM class that enables you to create complex queries using logical operators. It is used to create more elaborate query conditions, such as OR and NOT queries, making queries more flexible.

## What are the Django exceptions?

Django has various exceptions that can be used to catch errors and framework-specific exceptions. Some common exceptions include ObjectDoesNotExist, MultipleObjectsReturned, ValidationError, PermissionDenied, Http404.