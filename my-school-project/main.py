from flask import Flask, render_template, request, jsonify, url_for, redirect
from flask_pymongo import PyMongo
from functools import wraps
from pymongo import MongoClient
from bson import ObjectId
from flask import session

app = Flask(__name__)

app.config['MONGO_URI'] = 'mongodb://localhost:27017/students'
mongo = PyMongo(app)

app.secret_key = 'Saibaba@321'

user_data = {
    'username': 'Lalithya',
    'password': 'Saibaba56',
    'role': 'admin'
}
mongo.db.users.insert_one(user_data)

@app.route("/login", methods=['POST','GET'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = mongo.db.record.find_one({'username': username})

        if user:
            if user['password'] == password:
                session['username'] = username
                session['role'] = user.get('role', 'user')
                return redirect(url_for('student_details')), 302
            else:
                return jsonify({'message': 'Invalid Username or Password'}), 200
        else:
            return jsonify({'message': 'User not found'}), 200
    else:
        return render_template("loginPage.html")

@app.route("/admin/students")
def all_students():
    if 'username' in session and session['role'] == 'admin':
        students = mongo.db.record.find()
        return render_template("all_students.html", students=students)
    else:
        return redirect(url_for('login'))


@app.route('/student_info')
def student_details():
    username = session.get('username')
    if username:
        student = mongo.db.record.find_one({'username': username})
        if student:
            return render_template("student_info.html", student=student)
        else:
            return jsonify({'message': 'Student details not found'}), 404
    else:
        return redirect(url_for('login')), 302

@app.route("/home")
def home():
    return render_template("homePage.html")


@app.route('/info', methods=['POST','GET'])
def post_info():
    if request.method == 'POST':
        child_first_name = request.form['childFirstName']
        child_last_name = request.form['childLastName']
        dob = request.form['dob']
        primary_phone_number = request.form['primaryPhoneNumber']
        address = request.form['address']
        cls = request.form['class']
        mother_first_name = request.form['motherFirstName']
        mother_last_name = request.form['motherLastName']
        mother_phone_number = request.form['motherPhoneNumber']
        mother_email = request.form['motherEmail']
        father_first_name = request.form['fatherFirstName']
        father_last_name = request.form['fatherLastName']
        father_phone_number = request.form['fatherPhoneNumber']
        father_email = request.form['fatherEmail']
        username = request.form['loginUserName']
        password = request.form['loginPassword']
        student_data = {
            "child_first_name": child_first_name,
            "child_last_name": child_last_name,
            "dob": dob,
            "primary_phone_number": primary_phone_number,
            "address": address,
            "class": cls,
            "mother_first_name": mother_first_name,
            "mother_last_name": mother_last_name,
            "mother_phone_number": mother_phone_number,
            "mother_email": mother_email,
            "father_first_name": father_first_name,
            "father_last_name": father_last_name,
            "father_phone_number": father_phone_number,
            "father_email": father_email,
            "username": username,
            "password": password
        }

        # Insert the data into the "record" collection
        mongo.db.record.insert_one(student_data)

        return jsonify({'message': 'Data received successfully'}), 200
    else:
        return render_template("signInForm.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
