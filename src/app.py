"""Flask Application"""

# load libaries
from flask import Flask, request, jsonify
from flask_restful import Api, Resource, marshal_with, fields
from flask_sqlalchemy import SQLAlchemy
# load modules
from endpoints.blueprints.blueprint_x import blueprint_x
from endpoints.blueprints.blueprint_y import blueprint_y

# init Flask app
app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
db = SQLAlchemy(app)

class Task(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String, nullable=False)

	def __repr__(self):
		return self.name


fakeDatebase = {
	1 :{'name':'Clean car'},
	2 :{'name':'Write blog'},
	3 :{'name':'Start stream'},
}


class Items(Resource):
	def get(self):
		tasks = Task.query.all()
		return tasks

	def post(self,):
		data = request.json
		task = Task(name=data['name'])
		db.session.add(task)
		db.session.commit()
		return task

class Item(Resource):
	def get(self, pk):
		task = Task.query.filter_by(id=pk).first()
		return task

	def put(self, pk):
		data = request.json
		fakeDatebase[pk]['name'] = data['name']
		return fakeDatebase[pk]

	def delete(self, pk):
		del fakeDatebase[pk]
		return fakeDatebase


api.add_resource(Items, '/tasks')
api.add_resource(Item, '/tasks/<int:pk>')

@app.route('/')
def hello():
	return 'Hello World'


if __name__ == "__main__":
	####################
	# FOR DEVELOPMENT
	####################
	app.run(debug = True, host='0.0.0.0', port=5005)
