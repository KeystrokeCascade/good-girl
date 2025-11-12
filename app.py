from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

title = 'Good Girl'
db_secret = 'd1ebf4ae-d828-4d12-99c4-5d276ecbd699'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = db_secret

db = SQLAlchemy(app)

class Tasks(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(80), nullable=False)
	description = db.Column(db.String(1000))

	def __init__(self, title, description):
		self.title = title
		self.description = description

	def __str__(self):
		return f'ID: {self.id}\nTask: {self.title}\nDesc: {self.description}'

with app.app_context():
	db.create_all()

@app.route('/')
def index():
	tasks = db.session.query(Tasks).all()
	return render_template('index.html', tasks=tasks, title=title)

@app.route('/get', methods=['POST'])
def get()
	return None

@app.route('/add', methods=['POST'])
def add():
	task = Tasks(request.form['title'], request.form['description'])
	db.session.add(task)
	db.session.commit()
	return redirect(url_for('index'))

@app.route('/check', methods=['POST'])
def check()
	return None

@app.route('/delete', methods=['POST'])
def delete()
	return None

@app.route('/admin')
def admin():
	return '<p>Hello, World!</p>'
