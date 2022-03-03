from temp_flask import db#, login_manager
from datetime import datetime
from flask_login import (LoginManager, UserMixin, login_required,
			  login_user, current_user, logout_user)
from werkzeug.security import generate_password_hash, check_password_hash



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

user1=User(name="Вася",surname="Пупкин",patronim="Васильевич",position="Старший уборщик",sex=1)
db.session.add(user1)
db.session.commit()


user2=User(name="Петя")
user2.surname="Пяточкин"
user2.patronim="Кимович"
user2.position="Оператор метлы"
user2.sex=1
user2.avatar="avatar1.png"
db.session.add(user2)
db.session.commit()

user3=User(name="Дмитрий")
user3.surname="Кузнецов"
user3.patronim="Андреевич"
user3.position="Системный администратор"
user3.sex=1
user3.avatar="avatar3.png"
db.session.add(user3)
db.session.commit()

user4=User(name="Сергей")
user4.surname="Бронников"
user4.patronim="Дмитриевич"
user4.position="Специалист в области IT-технологий"
user4.sex=1
user4.avatar="avatar4.png"
db.session.add(user4)
db.session.commit()

user5=User(name="Александра")
user5.surname="Бульковна"
user5.patronim="Алексеевна"
user5.position="Диспетчер шкафчиков"
user5.sex=0
user5.avatar="avatar5.png"
db.session.add(user5)
db.session.commit()

user6=User(name="Юлия")
user6.surname="Казакова"
user6.patronim="Васильевна"
user6.position="Наладчик штор"
user6.sex=0
user6.avatar="avatar6.png"
db.session.add(user6)
db.session.commit()

user7=User(name="Евгений")
user7.surname="Чижов"
user7.patronim="Боричович"
user7.position="Уборщик"
user7.sex=1
user7.avatar="car.jpg"
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
