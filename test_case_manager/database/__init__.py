from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def reset_database():
    from test_case_manager.database.models import Project #noqa
    db.drop_all()
    db.create_all()
