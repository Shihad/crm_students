from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app=Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///"+os.path.join(basedir,"database.db")
db = SQLAlchemy(app)





class User(db.Model):
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



db.drop_all()
db.create_all()

user1=User(name="Вася",surname="Пупкин",patronim="Васильевич",position="Старший уборщик",sex=1)
db.session.add(user1)
db.session.commit()

user2=User(name="Петя")
user2.surname="Пяточкин"
user2.patronim="Кимович"
user2.position="Оператор метлы"
user2.sex=1
db.session.add(user2)
db.session.commit()

task=Task()
task.description="Убраться в офисе"
task.responsible_id=1
task.status="В процессе"
task.participants.append(user1)
task.participants.append(user2)
db.session.add(task)
db.session.commit()






app.run(debug=True)
