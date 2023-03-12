# 0x00. AirBnB clone - The console

```
Concepts
```
For this project, we expect you to look at these concepts:

- [Python packages](https://intranet.alxswe.com/concepts/66)
- [AirBnB clone](https://intranet.alxswe.com/concepts/74)

![AirBnB clone](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230310%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230310T124943Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=4388b1671c31de16681aa6c6bd4c7889340622d664bae34458c76d5f6ccde4cd)

# Background Context

# Welcome to the AirBnB clone project!

Before starting, please read the **AirBnB** concept page.

[![SE - HBNB project overview](https://img.youtube.com/vi/XRH_8w1DEGI/maxresdefault.jpg)](https://www.youtube.com/watch?v=XRH_8w1DEGI)

## First step: Write a command interpreter to manage your AirBnB objects.

This is the first step towards building your first full web application: the **AirBnB clone**. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration… 

Each task is linked and will help you to:

	. put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
	. create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
	. create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
	. create the first abstracted storage engine of the project: File storage. 
	. create all unittests to validate all our classes and storage engine

# What’s a command interpreter?

Do you remember the Shell? It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:

	. Create a new object (ex: a new User or a new Place)
	. Retrieve an object from a file, a database etc…
	. Do operations on objects (count, compute stats, etc…)
	. Update attributes of an object
	. Destroy an object

# Resources

**Read or watch:**

- [cmd module](https://docs.python.org/3.8/library/cmd.html)
- [cmd module in depth](http://pymotw.com/2/cmd/)
- [uuid module](https://docs.python.org/3.8/library/uuid.html)
- packages concept page
- [datetime](https://docs.python.org/3.8/library/datetime.html)
- [unittest module](https://docs.python.org/3.8/library/unittest.html#module-unittest)
- [args/kwargs](https://yasoob.me/2013/08/04/args-and-kwargs-in-python-explained/)
- [Python test cheatsheet](https://www.pythonsheets.com/notes/python-tests.html)
- [cmd module wiki page](https://wiki.python.org/moin/CmdModule)
- [python unittest](https://realpython.com/python-testing/)

# Learning Objectives

At the end of this project, you are expected to be able to [explain to anyone](https://fs.blog/feynman-learning-technique/),** without the help of Google**:


## General
        
	. How to create a Python package
	. How to create a command interpreter in Python using the cmd module
	. What is Unit testing and how to implement it in a large project
	. How to serialize and deserialize a Class
	. How to write and read a JSON file
	. How to manage datetime
	. What is an UUID
	. What is *args and how to use it
	. What is **kwargs and how to use it
	. How to handle named arguments in a function

# Copyright - Plagiarism

	. You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.
	. You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work. 
	. You are not allowed to publish any content of this project.
	. Any form of plagiarism is strictly forbidden and will result in removal from the program.

# Requirements

## Python Scripts

	. Allowed editors: vi, vim, emacs
	. All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
	. All your files should end with a new line
	. The first line of all your files should be exactly #!/usr/bin/python3
	. A README.md file, at the root of the folder of the project, is mandatory
	. Your code should use the pycodestyle (version 2.8.*)
	. All your files must be executable
	. The length of your files will be tested using wc
	. All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
	. All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
	. All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
	. A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

## Python Unit Tests

	. Allowed editors: vi, vim, emacs
	. All your files should end with a new line
	. All your test files should be inside a folder tests
	. You have to use the [unittest module](https://docs.python.org/3.4/library/unittest.html#module-unittest)
	. All your test files should be python files (extension: .py)
	. All your test files and folders should start by test_
	. Your file organization in the tests folder should be the same as your project
	. e.g., For models/base_model.py, unit tests must be in: tests/test_models/test_base_model.py
	. e.g., For models/user.py, unit tests must be in: tests/test_models/test_user.py
	. All your tests should be executed by using this command: python3 -m unittest discover tests
	. You can also test file by file by using this command: python3 -m unittest tests/test_models/test_base_model.py
	. All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
	. All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
	. All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
	. We strongly encourage you to work together on test cases, so that you don’t miss any edge case

# GitHub

**There should be one project repository per group. If you clone/fork/whatever a project repository with the same name before the second deadline, you risk a 0% score.**

# More Info

## Execution

Your shell should work like this in interactive mode:

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```
But also in non-interactive mode: (like the Shell project in C)

```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```
All tests should also pass in non-interactive mode: $ echo "python3 -m unittest discover tests" | bash

![AirBnB clone](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/815046647d23428a14ca.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230310%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230310T124943Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=277655f5bdb4ea0fbdf9fe1586adeaf5f36eb45beeaab65f4d76de26260610de)

[![SE - HBNB - The console](https://img.youtube.com/vi/1mAC9x3aixE/maxresdefault.jpg)](https://www.youtube.com/watch?v=1mAC9x3aixE)

```
0. README, AUTHORS 
```
	- Write a README.md: 
	- description of the project
		- how to start it
		- how to use it
		- examples
	- You should have an AUTHORS file at the root of your repository, listing all individuals having contributed content to the repository. For format, reference [Docker’s AUTHORS page](https://github.com/moby/moby/blob/master/AUTHORS)
	- You should use branches and pull requests on GitHub - it will help you as team to organize your work

```
1. Be pycodestyle compliant! 
```
Write beautiful code that passes the pycodestyle checks.

**Repo:**

	- GitHub repository: AirBnB_clone

```
2. Unittests 
```
All your files, classes, functions must be tested with unit tests

```
guillaume@ubuntu:~/AirBnB$ python3 -m unittest discover tests
...................................................................................
...................................................................................
.......................
----------------------------------------------------------------------
Ran 189 tests in 13.135s

OK
guillaume@ubuntu:~/AirBnB$
```
Note that this is just an example, the number of tests you create can be different from the above example.

**Warning:**

Unit tests must also pass in non-interactive mode:

```
guillaume@ubuntu:~/AirBnB$ echo "python3 -m unittest discover tests" | bash
...................................................................................
...................................................................................
.......................
----------------------------------------------------------------------
Ran 189 tests in 13.135s

OK
guillaume@ubuntu:~/AirBnB$
```
**Repo:**

 - GitHub repository: AirBnB_clone
 - File: tests/

```
3. BaseModel 
```
Write a class BaseModel that defines all common attributes/methods for other classes:

	- models/base_model.py
	- Public instance attributes:
		- id: string - assign with an uuid when an instance is created:
			- you can use uuid.uuid4() to generate unique id but don’t forget to convert to a string
			- the goal is to have unique id for each BaseModel
		- created_at: datetime - assign with the current datetime when an instance is created
		- updated_at: datetime - assign with the current datetime when an instance is created and it will be updated every time you change your object
	- __str__: should print: [<class name>] (<self.id>) <self.__dict__>
	- Public instance methods: 
		- save(self): updates the public instance attribute updated_at with the current datetime
		- to_dict(self): returns a dictionary containing all keys/values of __dict__ of the instance: 
			- by using self.__dict__, only instance attributes set will be returned
			- a key __class__ must be added to this dictionary with the class name of the object
			- created_at and updated_at must be converted to string object in ISO format:
				- format: %Y-%m-%dT%H:%M:%S.%f (ex: 2017-06-14T22:31:03.285259)
				- you can use isoformat() of datetime object
			- This method will be the first piece of the serialization/deserialization process: create a dictionary representation with “simple object type” of our BaseModel

```
guillaume@ubuntu:~/AirBnB$ cat test_base_model.py
#!/usr/bin/python3
from models.base_model import BaseModel

my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89
print(my_model)
my_model.save()
print(my_model)
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

guillaume@ubuntu:~/AirBnB$ ./test_base_model.py
[BaseModel] (b6a6e15c-c67d-4312-9a75-9d084935e579) {'my_number': 89, 'name': 'My First Model', 'updated_at': datetime.datetime(2017, 9, 28, 21, 5, 54, 119434), 'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579', 'created_at': datetime.datetime(2017, 9, 28, 21, 5, 54, 119427)}
[BaseModel] (b6a6e15c-c67d-4312-9a75-9d084935e579) {'my_number': 89, 'name': 'My First Model', 'updated_at': datetime.datetime(2017, 9, 28, 21, 5, 54, 119572), 'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579', 'created_at': datetime.datetime(2017, 9, 28, 21, 5, 54, 119427)}
{'my_number': 89, 'name': 'My First Model', '__class__': 'BaseModel', 'updated_at': '2017-09-28T21:05:54.119572', 'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579', 'created_at': '2017-09-28T21:05:54.119427'}
JSON of my_model:
    my_number: (<class 'int'>) - 89
    name: (<class 'str'>) - My First Model
    __class__: (<class 'str'>) - BaseModel
    updated_at: (<class 'str'>) - 2017-09-28T21:05:54.119572
    id: (<class 'str'>) - b6a6e15c-c67d-4312-9a75-9d084935e579
    created_at: (<class 'str'>) - 2017-09-28T21:05:54.119427

guillaume@ubuntu:~/AirBnB$ 
```
**Repo:**

	- GitHub repository: AirBnB_clone
	- File: models/base_model.py, models/__init__.py, tests/

```
4. Create BaseModel from dictionary 
```
Previously we created a method to generate a dictionary representation of an instance (method to_dict()).


Now it’s time to re-create an instance with this dictionary representation.

```
<class 'BaseModel'> -> to_dict() -> <class 'dict'> -> <class 'BaseModel'>
```
Update models/base_model.py:

	- __init__(self, \*args, \*\*kwargs):
		- you will use \*args, \**kwargs arguments for the constructor of a BaseModel. (more information inside the AirBnB clone concept page)
		- \*args won’t be used
		- if kwargs is not empty: 
			- each key of this dictionary is an attribute name (Note __class__ from kwargs is the only one that should not be added as an attribute. See the example output, below)
			- each value of this dictionary is the value of this attribute name
			- Warning: created_at and updated_at are strings in this dictionary, but inside your BaseModel instance is working with datetime object. You have to convert these strings into datetime object. Tip: you know the string format of these datetime
		- otherwise: 
			- create id and created_at as you did previously (new instance)

```
guillaume@ubuntu:~/AirBnB$ cat test_base_model_dict.py
#!/usr/bin/python3
from models.base_model import BaseModel

my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
print(my_model.id)
print(my_model)
print(type(my_model.created_at))
print("--")
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

print("--")
my_new_model = BaseModel(**my_model_json)
print(my_new_model.id)
print(my_new_model)
print(type(my_new_model.created_at))

print("--")
print(my_model is my_new_model)

guillaume@ubuntu:~/AirBnB$ ./test_base_model_dict.py
56d43177-cc5f-4d6c-a0c1-e167f8c27337
[BaseModel] (56d43177-cc5f-4d6c-a0c1-e167f8c27337) {'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337', 'created_at': datetime.datetime(2017, 9, 28, 21, 3, 54, 52298), 'my_number': 89, 'updated_at': datetime.datetime(2017, 9, 28, 21, 3, 54, 52302), 'name': 'My_First_Model'}
<class 'datetime.datetime'>
--
{'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337', 'created_at': '2017-09-28T21:03:54.052298', '__class__': 'BaseModel', 'my_number': 89, 'updated_at': '2017-09-28T21:03:54.052302', 'name': 'My_First_Model'}
JSON of my_model:
    id: (<class 'str'>) - 56d43177-cc5f-4d6c-a0c1-e167f8c27337
    created_at: (<class 'str'>) - 2017-09-28T21:03:54.052298
    __class__: (<class 'str'>) - BaseModel
    my_number: (<class 'int'>) - 89
    updated_at: (<class 'str'>) - 2017-09-28T21:03:54.052302
    name: (<class 'str'>) - My_First_Model
--
56d43177-cc5f-4d6c-a0c1-e167f8c27337
[BaseModel] (56d43177-cc5f-4d6c-a0c1-e167f8c27337) {'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337', 'created_at': datetime.datetime(2017, 9, 28, 21, 3, 54, 52298), 'my_number': 89, 'updated_at': datetime.datetime(2017, 9, 28, 21, 3, 54, 52302), 'name': 'My_First_Model'}
<class 'datetime.datetime'>
--
False
guillaume@ubuntu:~/AirBnB$ 
```

**Repo:**

	- GitHub repository: AirBnB_clone
	- File: models/base_model.py, tests/
