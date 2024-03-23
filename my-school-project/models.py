# from main import db, ma
# from sqlalchemy import UniqueConstraint
#
# import sqlite3
# conn = sqlite3.connect("instance.db")
# c = conn.cursor()
#
# c.execute("""CREATE TABLE frfr (
#             name TEXT,
#             age INTEGER,
#             height REAL
#     )""")
#
# conn.commit()



# columns = [
#     "id INTEGER PRIMARY KEY",
#     "fname VARCHAR",
#     "lname VARCHAR UNIQUE",
#     "dob VARCHAR",
#     "phno VARCHAR",
#     "address VARCHAR",
#     "cls VARCHAR",
#     "mfname VARCHAR",
#     "mlname VARCHAR",
#     "memail VARCHAR",
#     "mphno VARCHAR",
#     "ffname VARCHAR",
#     "flname VARCHAR",
#     "femail VARCHAR",
#     "fphno VARCHAR"
#     "usename VARCHAR UNIQUE",
#     "password VARCHAR"
# ]



# create_table_cmd = f"CREATE TABLE example({','.join(columns)})"
# conn.execute(create_table_cmd)
# conn.commit()

# people = ["1, 'Rishi', 'Rao', '18-12-2020', '9000459462','Flat 202, Blue Hills', 'preK', 'Sonia', 'Kailash', 'sonic5@gmail.com', '9654387542','Rahul','Rao', 'rahulr@gmail.com', '7843289563', 'rishi_rao', 'RishiRao'",
#           "2, 'Bhanu', 'Mishra', '15-11-2022', '9054673490','12-4/5, Tower fields', 'Toddler', 'Charmi', 'Rao', 'charmi@gmail.com', '8943568934', 'Arun', 'Mishra','arun@gmail.com','6943062544', 'bhanu_mishra', 'BhanuMishra'"]
#
# for person_data in people:
#     insert_cmd = f"INSERT INTO students VALUES({person_data})"
#     conn.execute(insert_cmd)
# conn.commit()


# class StudentModel(db.Model):
#     __tablename__ = "students"
#
#     id = db.Column(db.Integer, primary_key=True)
#     fname = db.Column(db.String(25), nullable=False)
#     lname = db.Column(db.String(25), nullable=False, unique = True)
#     dob = db.Column(db.String(12), nullable=False)
#     phno = db.Column(db.String(15), nullable=False)
#     address = db.Column(db.String(50), nullable=False)
#     cls = db.Column(db.String(25), nullable=False)
#     mfname = db.Column(db.String(25), nullable = False)
#     mlanme = db.Column(db.String(25), nullable = False)
#     memail = db.Column(db.String(25), nullable = False)
#     mphno = db.Column(db.String(25), nullable = False)
#     ffname = db.Column(db.String(25), nullable = False)
#     flname = db.Column(db.String(25), nullable = False)
#     femail = db.Column(db.String(25), nullable = False)
#     fphno = db.Column(db.String(25), nullable = False)
#     username = db.Column(db.String(25), unique=True, nullable=False)
#     password = db.Column(db.String(25), nullable=False)
#     __table_args__ = (UniqueConstraint('fname', 'lname', name='_fname_lname_uc'),)
#
#
# class StudentSchema(ma.SQLAlchemyAutoSchema):
#     class Meta:
#         model = StudentModel
#         load_instance = True
#         sqla_session = db.session
#
# student_schema = StudentSchema()
# students_schema = StudentSchema(many=True)
