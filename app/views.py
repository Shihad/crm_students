from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask import render_template , request
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
	avatar=db.Column(db.String(255))
	

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

user1=User(name="Вася",surname="Пупкин",patronim="Васильевич",position="Старший уборщик",sex=1,avatar="img/avatars/avatar1.jpg")
db.session.add(user1)
db.session.commit()


user2=User(name="Петя")
user2.surname="Пяточкин"
user2.patronim="Кимович"
user2.position="Оператор метлы"
user2.sex=1
user2.avatar="img/avatars/avatar1.jpg"
db.session.add(user2)
db.session.commit()

user3=User(name="Дмитрий")
user3.surname="Кузнецов"
user3.patronim="Андреевич"
user3.position="Системный администратор"
user3.sex=1
user3.avatar="img/avatars/avatar1.jpg"
db.session.add(user3)
db.session.commit()

user4=User(name="Сергей")
user4.surname="Бронников"
user4.patronim="Дмитриевич"
user4.position="Специалист в области IT-технологий"
user4.sex=1
user4.avatar="img/avatars/avatar1.jpg"
db.session.add(user4)
db.session.commit()

user5=User(name="Александра")
user5.surname="Бульковна"
user5.patronim="Алексеевна"
user5.position="Диспетчер шкафчиков"
user5.sex=0
user5.avatar="img/avatars/avatar1.jpg"
db.session.add(user5)
db.session.commit()

user6=User(name="Юлия")
user6.surname="Казакова"
user6.patronim="Васильевна"
user6.position="Наладчик штор"
user6.sex=0
user6.avatar="img/avatars/avatar1.jpg"
db.session.add(user6)
db.session.commit()

user7=User(name="Евгений")
user7.surname="Чижов"
user7.patronim="Боричович"
user7.position="Уборщик"
user7.sex=1
user7.avatar="img/avatars/avatar1.jpg"
db.session.add(user7)
db.session.commit()

task=Task()
task.description="Убраться в офисе"
task.responsible_id=1
task.status="В процессе"
task.participants.append(user1)
task.participants.append(user2)
#task.end_date= datetime.time(8,48,45)
db.session.add(task)
db.session.commit()


task=Task()
task.description="Подмести двор"
task.responsible_id=2
task.status="В процессе"
task.participants.append(user2)
#task.end_date= datetime.time(8,48,45)
db.session.add(task)
db.session.commit()


task=Task()
task.description="Захватить мир"
task.responsible_id=1
task.status="Начата"
task.participants.append(user1)
#task.end_date= datetime.time(8,48,45)
db.session.add(task)
db.session.commit()


task=Task()
task.description="Купить цветы"
task.responsible_id=4
task.status="Начата"
task.participants.append(user4)
task.participants.append(user5)
task.participants.append(user6)
#task.end_date= datetime.time(8,48,45)
db.session.add(task)
db.session.commit()

task=Task()
task.description="Вылечить зубы"
task.responsible_id=5
task.status="В процессе"
task.participants.append(user5)
#task.end_date= datetime.time(8,48,45)
db.session.add(task)
db.session.commit()


@app.route("/index",methods=['POST','GET'])
@app.route("/",methods=['POST','GET'])
def index():
	if request.method=='POST':
		print(request.form)
		desc=request.form['description']
		start_date=request.form['start_date']
		print(start_date)
		start_date=datetime.strptime(start_date, '%m/%d/%Y')
		end_date=request.form['end_date']
		print(end_date)
		end_date=datetime.strptime(end_date, '%m/%d/%Y')
		status="Начата"
		task=Task()
		task.description=desc
		task.status=status
		task.responsible_id=4
		task.participants.append(user1)
		task.start_date= start_date
		task.end_date= end_date
		current_db_sessions = db.session.object_session(task)
		current_db_sessions.add(task)
		current_db_sessions.commit()
		users=User.query.all()
		user=User.query.filter(User.id==uid).first()
		new_deals=Task.query.filter(Task.status=="Начата").all()	
		prepare_deals=Task.query.filter(Task.status=="В процессе").all()
		return render_template("deals_flask.html",workers=users,user=user,new_deals=new_deals,prepare_deals=prepare_deals)
	else:
		users=User.query.all()
		user=User.query.filter(User.id==1).first()
		new_deals=Task.query.filter(Task.status=="Начата").all()	
		prepare_deals=Task.query.filter(Task.status=="В процессе").all()
		return render_template("deals_flask.html",workers=users,user=user,new_deals=new_deals,prepare_deals=prepare_deals)

@app.route("/contacts",methods=['POST','GET'])
def contacts():
	if request.method=='POST':
		print(request.form)
		name=request.form['name']
		surname=request.form['surname']
		patronim=request.form['patronim']
		position=request.form['position']
		user=User()
		user.name=name
		user.surname=surname
		user.patronim=patronim
		user.position=position
		#current_db_sessions = db.session.object_session(user)
		#current_db_sessions.add(user)
		#current_db_sessions.commit()
		db.session.add(user)
		db.session.commit()
		users=User.query.all()
		return render_template('contacts_mobile_flask.html',workers=users)
	else:
		users=User.query.all()
		return render_template('contacts_mobile_flask.html',workers=users)
	


app.run(debug=True)
