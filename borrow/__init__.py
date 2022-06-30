from flask import Flask, request,jsonify
import pymongo
import libconfigs as configs
import json
import datetime 

client = pymongo.MongoClient(configs.DB_URL)
db = client[configs.DB_NAME] 
borrow_col = db[configs.COLLECTIONS["borrows"]]
book_col = db[configs.COLLECTIONS["books"]]
student_col = db[configs.COLLECTIONS["student"]]

app = Flask(__name__)

@app.route("/" , methods = ["GET"])
def borrow_debug():
    return "Hello World from borrow"


# @app.route("/test", methods = ["GET"])
# def test():
#     return "Hello World from test"

@app.route("/add" , methods = ["PUT"])
def create_borrow():
    try:
        data = json.loads(request.data)
        data["_id"] = data["borrow_id"]
        _ = data["SRN"]
        _ = data["book_id"]
        print(data)
        if student_col.find_one({"_id": data["SRN"]}) is None:
            return jsonify({"error": "Student not found"}), 404, {'Content-Type': 'application/json'}
        book_res = book_col.find_one({"_id": data["book_id"]})
        if book_res is None:
            return jsonify({"error": "Book not found"}), 404, {'Content-Type': 'application/json'}
        if book_res["isBorrowed"] is True:
            return jsonify({"error": "Book is already borrowed"}), 400, {'Content-Type': 'application/json'}
        data["timestamp"] = datetime.datetime.now()
        status = borrow_col.insert_one(data)
        book_col.update_one({"_id": data["book_id"]}, {"$set": {"isBorrowed": True}})
        print(status.acknowledged)
        return {"ok": "success"}, 201, {'Content-Type': 'application/json'}

    except pymongo.errors.DuplicateKeyError:
        return {"error": "Already borrowed"}, 400, {'Content-Type': 'application/json'}
    except Exception as e:
        return jsonify({"error": str(e)}), 400, {'Content-Type': 'application/json'}


@app.route("/fetch" , methods = ["GET"])
def get_borrow():
    try:
        return jsonify(list(borrow_col.find())), 200, {'Content-Type': 'application/json'}
    except TypeError:
        return jsonify({"error": "Collection is Empty"}), 400, {'Content-Type': 'application/json'}
    except Exception as E:
        return jsonify({"error": str(E)}), 400, {'Content-Type': 'application/json'}

@app.route("/fetch/<borrow_id>", methods=["GET"])
def get_one_borrow(borrow_id):
    try:
        return jsonify(borrow_col.find_one({"_id": borrow_id})), 200, {'Content-Type': 'application/json'}
    except TypeError:
        return jsonify({"error": "Student not found"}), 404, {'Content-Type': 'application/json'}


@app.route("/remove",methods=["DELETE"])
def delete_borrow():
    try:
        data = json.loads(request.data)
        data["_id"] = data["borrow_id"]
        print(data)
        book_id = borrow_col.find_one({"_id": data["borrow_id"]})["book_id"]
        status = borrow_col.delete_one({"_id": data["_id"]})
        book_col.update_one({"_id": book_id}, {"$set": {"isBorrowed": False}})
        return {"ok": "success", "count": status.deleted_count}, 201, {'Content-Type': 'application/json'}

    except TypeError:
        return jsonify({"error": "borrow not found"}), 404, {'Content-Type': 'application/json'}
    except Exception as e:
        return jsonify({"error": str(e)}), 400, {'Content-Type': 'application/json'}


if __name__ == "__main__":
    app.run(debug=True,port=5000)