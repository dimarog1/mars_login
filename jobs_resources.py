from flask import Flask, jsonify
from flask_restful import reqparse, abort, Api, Resource

from data import db_session
from data.jobs import Jobs

app = Flask(__name__)
api = Api(app)


parser = reqparse.RequestParser()
parser.add_argument('title', required=True)
parser.add_argument('leader_id', required=True)
parser.add_argument('work_size', required=True, type=int)
parser.add_argument('collaborators', required=True, type=str)
parser.add_argument('is_finished', required=True, type=bool)


@app.errorhandler(404)
def abort_if_news_not_found(job_id):
    session = db_session.create_session()
    job = session.query(Jobs).get(job_id)
    if not job:
        abort(404, message=f"Jobs {job_id} not found")


# 'id', 'title', 'leader_id', 'work_size', 'collaborators', 'is_finished', 'user_id', 'user.name'

class JobsResource(Resource):
    def get(self, job_id):
        abort_if_news_not_found(job_id)
        session = db_session.create_session()
        job = session.query(Jobs).get(job_id)
        return jsonify({'job': job.to_dict(
            only=('id', 'title', 'leader_id', 'work_size', 'collaborators', 'is_finished', 'user_id', 'user.name'))})

    def delete(self, job_id):
        abort_if_news_not_found(job_id)
        session = db_session.create_session()
        job = session.query(Jobs).get(job_id)
        session.delete(job)
        session.commit()
        return jsonify({'success': 'OK'})


class JobsListResource(Resource):
    def get(self):
        session = db_session.create_session()
        jobs = session.query(Jobs).all()
        return jsonify({'jobs': [item.to_dict(
            only=('id', 'title', 'leader_id', 'work_size', 'collaborators', 'is_finished', 'user_id', 'user.name')) for item in jobs]})

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        job = Jobs(
            title=args['title'],
            leader_id=args['leader_id'],
            work_size=args['work_size'],
            collaborators=args['collaborators'],
            is_finished=args['is_finished']
        )
        session.add(job)
        session.commit()
        return jsonify({'success': 'OK'})
