# from flask import Flask, jsonify, request, render_template
# app = Flask(__name__)
#
import numpy
# data = [{"name1":["dob", "phno1", "father1", "mother1"],
#          "name2":["dob2", "phno2", "father2", "mother2"],
#          "name3":["dob3", "phno3", "father3", "mother3"]}]
#
# details = []
#
# @app.route("/home")
# def home():
#     return render_template("homePage.html")
#
# @app.get("/info/<string:name>")
# def get_info(name):
#     for student_data in data:
#         if name in student_data:
#             return {"name": name, "details": student_data[name]}
#     return {"error": "Student not found"}, 404
#
# @app.post("/info")
# def post_info():
#     req_data = request.get_json()
#     new_student = {'fname': req_data['fname'],
#                    'lname': req_data['lname'],
#                    'dob': req_data['dob'],
#                    'phno': req_data['phno'],
#                    'address':req_data['address'],
#                    'class':req_data['class'],
#                    'mfname':req_data['mfname'],
#                    'mlname':req_data['mlname'],
#                    'mphno':req_data['mphno'],
#                    'memail':req_data['memail'],
#                    'ffname':req_data['ffname'],
#                    'flname':req_data['flname'],
#                    'fphno':req_data['fphno'],
#                    'femail':req_data['femail'],
#                    'username':req_data['username'],
#                    'password':req_data['password']}
#     details.append(new_student)
#     return details, 201
#
# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5000,debug = True)
