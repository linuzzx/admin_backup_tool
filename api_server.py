from flask import Flask, jsonify, request
from admin_backup_tool import *
from datetime import datetime

app = Flask(__name__)

data = import_data("data.json")

# Backup data.json
"""
if not os.path.exists("backup"):
    os.makedirs("backup")
    
current_datetime = datetime.now().strftime("%Y%m%d_%H%M%S")

with open(f"backup/data_{current_datetime}.json", 'w') as f:
    json.dump(data, f)

"""

@app.route("/get_student", methods=["POST"])
def api_get_student():
    payload = request.get_json()
    # Check if request format is valid
    if "name" in payload and isinstance(payload["name"], str):
        name = payload["name"]
    else:
        return jsonify({"error": "wrong format"}), 400

    if name not in data:
        return jsonify({"error": "Student does not exist."}), 404

    return jsonify(get_student(data, name)), 200


@app.route("/add_student", methods=["POST"])
def api_add_student():
    payload = request.get_json()
    # Check if request format is valid
    if "name" in payload and isinstance(payload["name"], str):
        name = payload["name"]
    else:
        return jsonify({"error": "wrong format"}), 400

    if name in data:
        return jsonify({"error": "Student already exists."}), 400

    add_student(data, name)

    export_data("data.json", data)

    return jsonify("Success"), 201


@app.route("/remove_student", methods=["POST"])
def api_remove_student():
    payload = request.get_json()

    # Check if request format is valid
    if "name" in payload and isinstance(payload["name"], str):
        name = payload["name"]
    else:
        return jsonify({"error": "wrong format"}), 400

    if name not in data:
        return jsonify({"error": "Student doesn't exists."}), 404

    remove_student(data, name)

    export_data("data.json", data)

    return jsonify("Success"), 200


@app.route("/add_grade", methods=["POST"])
def api_add_grade():
    payload = request.get_json()

    # Check if request format is valid
    if "name" in payload and "grade_type" in payload and "grade" in payload and isinstance(payload["name"], str) and isinstance(payload["grade_type"], str) and isinstance(payload["grade"], int):
        name = request.get_json()["name"]
        grade_type = request.get_json()["grade_type"]
        grade = request.get_json()["grade"]
    else:
        return jsonify({"error": "wrong format"}), 400

    if name not in data:
        return jsonify({"error": "Student doesn't exist."}), 404

    if grade < 1 or grade > 6:
        return jsonify({"error": "Grade must be between 1 and 6."}), 400
    
    add_grade(data, name, grade_type, grade)

    export_data("data.json", data)

    return jsonify("Success"), 201


@app.route("/remove_grade", methods=["POST"])
def api_remove_grade():
    payload = request.get_json()
    # Check if request format is valid
    if "name" in payload and "grade_type" in payload and "grade" in payload and isinstance(payload["name"], str) and isinstance(payload["grade_type"], str) and isinstance(payload["grade"], int):
        name = request.get_json()["name"]
        grade_type = request.get_json()["grade_type"]
        grade = request.get_json()["grade"]
    else:
        return jsonify({"error": "wrong format"}), 400

    if name not in data:
        return jsonify({"error": "Student doesn't exist."}), 404
    if [grade_type, grade] not in data[name]:
        return jsonify({"error": "Grade entry doesn't exist."}), 404

    remove_grade(data, name, grade_type, grade)

    export_data("data.json", data)

    return jsonify("Success"), 201


@app.route("/list_students", methods=["GET"])
def api_list_students():
    return jsonify(get_averages(data)), 200




app.run(debug=True)
