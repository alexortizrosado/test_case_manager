import logging

from datetime import datetime

from test_case_manager.database import db
from test_case_manager.database.models import Project

log = logging.getLogger(__name__)


# Project
def create_project(data):
    name = data.get('name')
    description = data.get('description')
    created_at = data.get('created_at')
    log.info('Creating project: {}'.format(name))
    project = Project(name, description, created_at)
    db.session.add(project)
    db.session.commit()


def update_project(project_id, data):
    project = Project.query.filter(Project.id == project_id).one()
    name = data.get('name')
    description = data.get('description')
    if name:
        project.name = name
    if description:
        project.description = description
    project.updated_at = datetime.utcnow()
    log.info('Updating project: {}'.format(project_id))
    db.session.add(project)
    db.session.commit()


def delete_project(project_id):
    project = Project.query.filter(Project.id == project_id).one()
    log.info('Deleting project: {}'.format(project_id))
    db.session.delete(project)
    db.session.commit()
