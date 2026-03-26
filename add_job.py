
from data.jobs import Job
from data import db_session

db_session.global_init("db/mars.db")
db_sess = db_session.create_session()

job = Job()
job.team_leader = 1
job.job = "deployment of residential modules 1 and 2"
job.work_size = 15
job.collaborators = "2, 3"
job.is_finished = True

db_sess.add(job)
db_sess.commit()


job = Job()
job.team_leader = 2
job.job = "qwerty"
job.work_size = 99
job.collaborators = "4, 8"
job.is_finished = False

db_sess.add(job)
db_sess.commit()


job = Job()
job.team_leader = 3
job.job = "ytrewq"
job.work_size = 250
job.collaborators = "1, 2"
job.is_finished = True

db_sess.add(job)
db_sess.commit()