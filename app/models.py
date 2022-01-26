from app import db, login_manager
from datetime import datetime
from flask_login import (LoginManager, UserMixin, login_required,
			  login_user, current_user, logout_user)
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model,UserMixin):
	__tablename__="users"
	id=db.Column(db.Integer(),primary_key=True)
	name=db.Column(db.String(255),nullable=False)
	surname=db.Column(db.String(255))
	patronim=db.Column(db.String(255))
	position=db.Column(db.String(255))
	sex=db.Column(db.Boolean())
	responsible=db.relationship("Task",backref="users")
	

class Task(db.Model):
	__tablename__="tasks"
	id=db.Column(db.Integer(),primary_key=True)
	participants=db.relationship("User",secondary="user_tasks",backref="tasks")
	description=db.Column(db.String(255))
	start_date=db.Column(db.DateTime(),default=datetime.utcnow,nullable=False)
	end_date=db.Column(db.DateTime())
	status=db.Column(db.String(255))
	responsible_id=db.Column(db.Integer(),db.ForeignKey("users.id"),)
	

user_tasks=db.Table('user_tasks',
					db.Column("user_id", db.Integer,db.ForeignKey("users.id")),
					db.Column("task_id", db.Integer,db.ForeignKey("tasks.id")))

