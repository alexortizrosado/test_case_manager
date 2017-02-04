from flask import Flask
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from test_case_manager import settings
from test_case_manager.database import db, models

flask_app = Flask(__name__)
flask_app.config['SQLALCHEMY_DATABASE_URI'] = settings.SQLALCHEMY_DATABASE_URI
flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = (
    settings.SQLALCHEMY_TRACK_MODIFICATIONS)

Migrate(flask_app, db, models)

manager = Manager(flask_app)
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
