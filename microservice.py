from student import app as student_app
from borrow import app as borrow_app
from book import app as book_app
from author import app as author_app

from werkzeug.middleware.dispatcher import DispatcherMiddleware
from flask import Flask, request, jsonify
from werkzeug.exceptions import NotFound


microserviceApp = Flask(__name__)

microserviceApp.wsgi_app = DispatcherMiddleware(NotFound(), {
    '/student': student_app,
    '/borrow': borrow_app,
    '/book': book_app,
    '/author': author_app
})

@microserviceApp.route("/", methods = ["GET"])
def main_debug():
    return "Hello World from main"

if __name__ == "__main__":
    microserviceApp.run(port=5000)