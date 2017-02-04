import logging

from flask import request
from flask_restplus import Resource
from test_case_manager.api.actions import create_project, delete_project, update_project
from test_case_manager.api.serializers import project
from test_case_manager.api.restplus import api
from test_case_manager.database.models import Project

log = logging.getLogger(__name__)

ns = api.namespace('projects', description='Operations related to projects.')


@ns.route('/')
class ProjectCollection(Resource):

    @api.marshal_list_with(project)
    def get(self):
        """
        Returns list of projects.
        """
        projects = Project.query.all()
        return projects

    @api.response(201, 'Project successfully created.')
    @api.expect(project)
    def post(self):
        """
        Creates a new project.
        """
        data = request.json
        create_project(data)
        return None, 201


@ns.route('/<int:id>')
@api.response(404, 'Project not found.')
class ProjectItem(Resource):

    @api.marshal_with(project)
    def get(self, id):
        """
        Returns a project.
        """
        return Project.query.filter(Project.id == id).one()

    @api.expect(project)
    @api.response(204, 'Project successfully updated.')
    def put(self, id):
        """
        Updates a project.
        Use this method to change the name and description of a project.
        * Send a JSON object with the new name in the request body.
        ```
        {
          "name": "New Project Name",
          "description": "New Project Description"
        }
        ```
        * Specify the ID of the project to modify in the request URL path.
        """
        data = request.json
        update_project(id, data)
        return None, 204

    @api.response(204, 'Project successfully deleted.')
    def delete(self, id):
        """
        Deletes project.
        """
        delete_project(id)
        return None, 204
