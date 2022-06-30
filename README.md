# Python-Is-All-You-Need

Final Project for Python-Is-All-You-Need Summer Course

### File Structure
```perl
❯ tree -a
.
├── __pycache__
├── author
│   ├── __init__.py
│   └── __pycache__
├── book
│   ├── __init__.py
│   └── __pycache__
├── borrow
│   ├── __init__.py
│   └── __pycache__
├── student
│   ├── __init__.py
│   └── __pycache__
├── Dockerfile # Docker configurations
├── .env # To contain info about the flask app
├── libconfigs.py # configurations files for the server
├── microservice.py # The load balancing server
├── postman.json # The postman collection of all the API calls available
├── requirements.txt # pip installations
└── scripts.sh # Single bash script to run the entire program in docker
```

### Modules
#### Student
###### Available Endpoints
- `/student/add/`Add a student
- `/student/remove/` Remove a student
- `/student/change/`Update information about student
- `/student/fetch/` Fetch Info about student(s)

###### Restrictions
- A student must have a `SRN` compulsorily
- The `SRN` attribute must be unique, and is considered as the primary key always


#### Author
###### Available Endpoints
- `/author/add/` Add an Author
- `/author/remove` Remove an author
- `/author/change` Update information about author
- `/author/fetch` Fetch Info about author(s)

###### Restrictions
- A student must have a `author_id` compulsorily
- The `author_id` attribute must be unique, and is considered as the primary key always


#### Book
###### Available Endpoints
- `/book/add/` Add a Book
- `/book/remove` Remove a book
- `/book/change` Update information about book
- `/book/fetch` Fetch Info about book(s)

###### Restrictions
- A student must have a `book_id` compulsorily
- The `book_id` attribute must be unique, and is considered as the primary key always
- The `author_id` is an optional attribute, 
	- Leave empty if required
	- But if mentioned, it should already exist in the `author-col` collection


#### Borrow
###### Available Endpoints
- `/borrow/add/` Borrow a book
- `/borrow/remove/` Return a book
- `/borrow/fetch/` Fetch Info about current borrowing(s)

###### Restrictions
- A student must have a `borrow_id` compulsorily
- The `borrow_id` attribute must be unique, and is considered as the primary key always
- `book_id` is a compulsory attribute which must refer to an existing book in the library
- `SRN` is a compulsory attribute which must refer to an existing student 