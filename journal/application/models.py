from application import db

class ToDoList(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(30), nullable=False)
	complete= db.Column(db.Boolean, default=False)

class Users(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	user_name = db.Column(db.String(30), nullable = False)
	
	
class Entries(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	entry = db.Column(db.String(1000), nullable=False)
	fk_user_id = db.Column('id', db.Integer, db.ForeignKey('Users.id'))
	fk_user_name = db.Column('user_name',. db.String(30), db.ForeignKey('Users.user_name'))