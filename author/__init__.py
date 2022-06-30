from flask import Flask, request,jsonify
import pymongo
import libconfigs as configs
import json

client = pymongo.MongoClient(configs.DB_URL)
db = client[configs.DB_NAME] 
author_col = db[configs.COLLECTIONS["author"]]

app = Flask(__name__)

@app.route("/" , methods = ["GET"])
def book_debug():
    return "Hello World from Author"

# @app.route("/test", methods = ["GET"])
# def test():
#     return "Hello World from test"


@app.route("/add" , methods = ["PUT"])
def create_author():
    try:
        data = json.loads(request.data)
        data["_id"]= data["author_id"]
        print(data)
        status = author_col.insert_one(data)
        return jsonify({"message": "Success"})
    
    except pymongo.errors.DuplicateKeyError:
        return {"error": "Author already exists"}, 400, {'Content-Type': 'application/json'}
    except Exception as e:
        return jsonify({"error":str(e)})



@app.route("/fetch" , methods = ["GET"])
def get_book():
    try:
        return jsonify(list(author_col.find())), 200, {'Content-Type': 'application/json'}
    except TypeError:
        return jsonify({"error": "Collection is Empty"}), 400, {'Content-Type': 'application/json'}
    except Exception as E:
        return jsonify({"error": str(E)}), 400, {'Content-Type': 'application/json'}

@app.route("/fetch/<author_id>", methods=["GET"])
def get_one_book(author_id):
    try:
        return jsonify(author_col.find_one({"_id": author_id})), 200, {'Content-Type': 'application/json'}
    except TypeError:
        return jsonify({"error": "Student not found"}), 404, {'Content-Type': 'application/json'}


@app.route("/change",methods=["POST"])
def update_book():
    try:
        data = json.loads(request.data)
        data["_id"] = data["author_id"]
        print(data)
        # upsert = True
        status = author_col.update_one(
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
        status = author_col.delete_one({"_id": data["_id"]})
        return {"ok": "success", "count": status.deleted_count}, 201, {'Content-Type': 'application/json'}

    except Exception as e:
        return jsonify({"error": str(e)}), 400, {'Content-Type': 'application/json'}



if __name__ == "__main__":
    app.run(debug=True,port=5000)