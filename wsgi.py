from data import db_session
from main import app

if __name__ == '__main__':
    db_session.global_init("db/blogs.db")
    app.run()