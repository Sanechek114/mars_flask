from flask_restful import reqparse, abort, Api, Resource
from flask import Flask, jsonify
from . import db_session
from .users import User
from .reqparser_user import parser
app = Flask(__name__)
api = Api(app)


@app.errorhandler(404)
def abort_if_users_not_found(users_id):
    session = db_session.create_session()
    users = session.query(User).get(users_id)
    if not users:
        abort(404, message=f"users {users_id} not found")


class UsersResource(Resource):
    def get(self, users_id):
        abort_if_users_not_found(users_id)
        session = db_session.create_session()
        users = session.get(User, users_id)
        return jsonify({'user': users.to_dict(
            only=('surname', 'name', 'age', 'position', 'speciality', 'address', 'email', 'hashed_password', 'modified_date'))})

    def delete(self, users_id):
        abort_if_users_not_found(users_id)
        session = db_session.create_session()
        users = session.get(User, users_id)
        session.delete(users)
        session.commit()
        return jsonify({'success': 'OK'})


class UsersListResource(Resource):
    def get(self):
        session = db_session.create_session()
        users = session.query(User).all()
        return jsonify({'users': [item.to_dict(
            only=('surname', 'name', 'age', 'position', 'speciality', 'address', 'email', 'hashed_password', 'modified_date')) for item in users]})

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        users = User(
            surname=args['surname'],
            name=args['name'],
            age=args['age'],
            position=args['position'],
            speciality=args['speciality'],
            address=args['address'],
            email=args['email'],
            hashed_password=args['hashed_password'],
        )
        session.add(users)
        session.commit()
        return jsonify({'id': users.id})