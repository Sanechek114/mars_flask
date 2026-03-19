from data.db_session import global_init, create_session
from data.users import User

if False:
    name_db = "db/mars.db"
else:
    name_db = input()

global_init(name_db)
db_sess = create_session()
for user in db_sess.query(User).filter(User.address.like("%module_1%"), 
                                       User.speciality.notilike("%engineer%"), 
                                       User.position.notilike("%engineer%")):
    print(user.id)
