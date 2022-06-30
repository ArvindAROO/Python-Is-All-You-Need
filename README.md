# Python-Is-All-You-Need

Final Project for Python-Is-All-You-Need Summer Course

##### Team Members:
- Prarthan Vijeth: PES1UG19ME131
- Aadeesh Jadishkumar: PES1UG19ME001
- Arvind Krishna : PES1UG19CS090

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
├── .env # To contain info about the flask app and DB URL
├── libconfigs.py # configurations files for the server
├── microservice.py # The load balancing server
├── postman.json # The postman collection of all the API calls available
├── requirements.txt # pip installations
└── scripts.sh # Single bash script to run the entire program in docker
```



### Setup
- Installations:
	- Python3, Docker, git, mongod & Postman
- Clone the repository using `git clone git@github.com:ArvindAROO/Python-Is-All-You-Need.git`
- Install dependencies with `pip3 install -r requirements.txt`
- Create a `.env` and add  
```bash
FLASK_APP=microservice:microserviceApp
DB_URL="database to url" # or use "mongodb://localhost:27017/"
```
- Run the program using `./scripts.sh`


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

### Additional Features
###### Micro-service Architecture
- All the modules are split into individual files for development & maintenance purposes
- All the modules are independent of each other with no cyclic dependencies/imports
- Issues with Monolithic architecture have been resolved

###### Dockerized
- The entire software is dockerized to enable faster integration and delivery
- The development and deployment process has been smoothed