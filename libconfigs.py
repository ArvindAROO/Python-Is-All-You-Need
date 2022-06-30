# read the environment variables
import os
import dotenv
dotenv.load_dotenv()
DB_URL = os.getenv('DB_URL')

DB_NAME = "special_topic"
COLLECTIONS = {
    "student":"students-col",
    "books":"books-col",
    "borrows":"borrow-col",
    "author": "author-col"
}