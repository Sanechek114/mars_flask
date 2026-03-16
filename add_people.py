from data.users import User
from data import db_session

db_session.global_init("db/mars.db")
user = User()
user.surname = "Scott"
user.name = "Ridley"
user.age = 21
user.position = "captain"
user.speciality = "research engineer"
user.address = "module_1"
user.email = "scott_chief@mars.org"
db_sess = db_session.create_session()
db_sess.add(user)
db_sess.commit()