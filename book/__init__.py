from flask import Flask, request,jsonify
import pymongo
import libconfigs as configs
import json

client = pymongo.MongoClient(configs.DB_URL)
db = client[configs.DB_NAME] 
book_col = db[configs.COLLECTIONS["books"]]
author_col = db[configs.COLLECTIONS["author"]]


app = Flask(__name__)

@app.route("/" , methods = ["GET"])
def book_debug():
    return "Hello World from book"

# @app.route("/test", methods = ["GET"])
# def test():
#     return "Hello World from test"


@app.route("/add" , methods = ["PUT"])
def create_book():
    try:
        data = json.loads(request.data)
        data["isBorrowed"] = False
        data["_id"]= data["book_id"]
        _ = data["author_id"]
        if _ != "":
            author = author_col.find_one({"_id": data["author_id"]})
            if author is None:
                return jsonify({"error": "Author not found"}), 404, {'Content-Type': 'application/json'}
            data["Author"] = author["name"]
        else:
            data["Author"] = ""
        print(data)
        status = book_col.insert_one(data)
        return jsonify({"message": "Success"})
    
    except pymongo.errors.DuplicateKeyError:
        return {"error": "Book already exists"}, 400, {'Content-Type': 'application/json'}
    except Exception as e:
        return jsonify({"error":str(e)})



@app.route("/fetch" , methods = ["GET"])
def get_book():
    try:
        return jsonify(list(book_col.find())), 200, {'Content-Type': 'application/json'}
    except TypeError:
        return jsonify({"error": "Collection is Empty"}), 400, {'Content-Type': 'application/json'}
    except Exception as E:
        return jsonify({"error": str(E)}), 400, {'Content-Type': 'application/json'}

@app.route("/fetch/<book_id>", methods=["GET"])
def get_one_book(book_id):
    try:
        return jsonify(book_col.find_one({"_id": book_id})), 200, {'Content-Type': 'application/json'}
    except TypeError:
        return jsonify({"error": "Student not found"}), 404, {'Content-Type': 'application/json'}


@app.route("/change",methods=["POST"])
def update_book():
    try:
        data = json.loads(request.data)
        data["_id"] = data["book_id"]
        print(data)
        # upsert = True
        status = book_col.update_one(
            {
                "_id": data["_id"]
            }, 
            {
                "$set": data
            },
            upsert=True
        )
        print(status.modified_count)
        return {"ok": "success", "changed": status.modified_count}, 201, {'Content-Type': 'application/json'}

    except Exception as e:
        return jsonify({"error": str(e)}), 400, {'Content-Type': 'application/json'}

@app.route("/remove",methods=["DELETE"])
def delete_book():
    try:
        data = json.loads(request.data)
        data["_id"] = data["book_id"]
        print(data)
        status = book_col.delete_one({"_id": data["_id"]})
        return {"ok": "success", "count": status.deleted_count}, 201, {'Content-Type': 'application/json'}

    except Exception as e:
        return jsonify({"error": str(e)}), 400, {'Content-Type': 'application/json'}



if __name__ == "__main__":
    app.run(debug=True,port=5000)