from flask import Flask, request,jsonify
import pymongo
import libconfigs as configs
import json

client = pymongo.MongoClient(configs.DB_URL)
db = client[configs.DB_NAME] 
stud_col = db[configs.COLLECTIONS["student"]]


app = Flask(__name__)

@app.route("/" , methods = ["GET"])
def student_debug():
    return "Hello World from Student"

# @app.route("/test", methods = ["GET"])
# def test():
#     return "Hello World from test"


@app.route("/add" , methods = ["PUT"])
def create_student():
    try:
        data = json.loads(request.data)
        data["_id"] = data["SRN"]
        print(data)
        status = stud_col.insert_one(data)
        print(status.acknowledged)
        return {"ok": "success"}, 201, {'Content-Type': 'application/json'}

    except pymongo.errors.DuplicateKeyError:
        return {"error": "SRN already exists"}, 400, {'Content-Type': 'application/json'}
    except Exception as e:
        return jsonify({"error": str(e)}), 400, {'Content-Type': 'application/json'}

@app.route("/fetch" , methods = ["GET"])
def get_student():
    try:
        return jsonify(list(stud_col.find())), 200, {'Content-Type': 'application/json'}
    except TypeError:
        return jsonify({"error": "Collection is Empty"}), 400, {'Content-Type': 'application/json'}
    except Exception as E:
        return jsonify({"error": str(E)}), 400, {'Content-Type': 'application/json'}


@app.route("/fetch/<SRN>", methods=["GET"])
def get_one_student(SRN):
    try:
        return jsonify(stud_col.find_one({"_id": SRN})), 200, {'Content-Type': 'application/json'}
    except TypeError:
        return jsonify({"error": "Student not found"}), 404, {'Content-Type': 'application/json'}



@app.route("/change",methods=["POST"])
def update_student():
    try:
        data = json.loads(request.data)
        data["_id"] = data["SRN"]
        print(data)
        status = stud_col.update_one(
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
def delete_student():
    try:
        data = json.loads(request.data)
        data["_id"] = data["SRN"]
        print(data)
        status = stud_col.delete_one({"_id": data["_id"]})
        return {"ok": "success", "count": status.deleted_count}, 201, {'Content-Type': 'application/json'}

    except Exception as e:
        return jsonify({"error": str(e)}), 400, {'Content-Type': 'application/json'}

if __name__ == "__main__":
    app.run(debug=True,port=5000)
