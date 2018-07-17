from flask import Flask, jsonify
from flask.ext.sqlalchemy import SQLAlchemy
import random
import string

app = Flask(__name__)

username,password = "eric_s","1234"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://"+username+":"+password+"@localhost/query_db"
db = SQLAlchemy(app)

class Table(db.Model):
    __tablename__ = 'table'
    id = db.Column(db.Integer, primary_key=True)
    column_one = db.Column(db.String)
    label = db.Column(db.String)

    def __init__(self, column_one, label):
    	self.column_one = column_one
    	self.label = label


def generate_dummy_data():
	character_set = [elem for elem in string.ascii_lowercase]
	for _ in range(1000):
		column_one = random.randint(0, 4)
		column_one = str(column_one)
		label = random.choice(character_set)
		table = Table(column_one, label)
		db.session.add(table)
		db.session.commit()


def to_dict(elem):
    dicter = elem.__dict__
    del dicter["_sa_instance_state"]
    return dicter


@app.route("/<query>")
def api_query(query):
    return jsonify({"query_result":
    	[to_dict(elem) 
    	for elem in Table.query.filter_by(column_one=query).all()]})


if __name__ == '__main__':
	app.run(port=5001)
