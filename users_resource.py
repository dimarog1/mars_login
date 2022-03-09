from flask import Flask, jsonify
from flask_restful import abort, Api, Resource, reqparse

from data import db_session
from data.users import User

parser = reqparse.RequestParser()
parser.add_argument('name', required=True)
parser.add_argument('surname', required=True)
parser.add_argument('age', required=True, type=str)
parser.add_argument('position', required=True, type=str)
parser.add_argument('speciality', required=True, type=str)
parser.add_argument('address', required=True, type=str)
parser.add_argument('email', required=True, type=str)


app = Flask(__name__)
api = Api(app)


@app.errorhandler(404)
def abort_if_user_not_found(user_id):
    session = db_session.create_session()
    user = session.query(User).get(user_id)
    if not user:
        abort(404, message=f"User {user_id} not found")


class UsersResource(Resource):
    def get(self, user_id):
        abort_if_user_not_found(user_id)
        session = db_session.create_session()
        user = session.query(User).get(user_id)
        return jsonify({'user': user.to_dict(
            only=('id', 'name', 'surname', 'age', 'position', 'speciality', 'address', 'email'))})

    def delete(self, user_id):
        abort_if_user_not_found(user_id)
        session = db_session.create_session()
        user = session.query(User).get(user_id)
        session.delete(user)
        session.commit()
        return jsonify({'success': 'OK'})


class UsersListResource(Resource):
    def get(self):
        session = db_session.create_session()
        users = session.query(User).all()
        return jsonify({'users': [item.to_dict(
            only=('id', 'name', 'surname', 'age', 'position', 'speciality', 'address', 'email')) for item in users]})

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        user = User(
            name=args['name'],
            surname=args['surname'],
            age=args['age'],
            position=args['position'],
            address=args['address'],
            email=args['email']
        )
        session.add(user)
        session.commit()
        return jsonify({'success': 'OK'})
