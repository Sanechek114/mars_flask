from data.users import User
from data import db_session

db_session.global_init("db/mars.db")
db_sess = db_session.create_session()

user = User()
user.surname = "Ridley"
user.name = "Scott"
user.age = 21
user.position = "captain"
user.speciality = "research engineer"
user.address = "module_1"
user.email = "scott_chief@mars.org"

db_sess.add(user)

user = User()
user.surname = "Ermolaev"
user.name = "Aleksandr"
user.age = 18
user.position = "mechanic"
user.speciality = "repairs engines"
user.address = "module_1"
user.email = "aleks114@mars.org"

db_sess.add(user)

user = User()
user.surname = "Archipov"
user.name = "Vladimir"
user.age = 18
user.position = "mechanic"
user.speciality = "repairs engines"
user.address = "module_1"
user.email = "dfgyu@mars.org"

db_sess.add(user)

db_sess.commit()
