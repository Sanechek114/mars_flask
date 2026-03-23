from data.db_session import global_init, create_session
from data.users import User
from data.jobs import Job

if False:
    name_db = "db/mars.db"
else:
    name_db = input()

global_init(name_db)
db_sess = create_session()
for user in db_sess.query(User).filter(User.position.like("chief") | User.position.like("middle")):
    print(f"<Colonist> {user.id} {user.surname} {user.name} {user.position} {user.speciality}")
