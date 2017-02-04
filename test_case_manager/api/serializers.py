from flask_restplus import fields
from test_case_manager.api.restplus import api

pagination = api.model('A page of results', {
    'page': fields.Integer(description='Number of this page of results'),
    'pages': fields.Integer(description='Total number of pages of results'),
    'per_page': fields.Integer(description='Number of items per page of results'),
    'total': fields.Integer(description='Total number of results'),
})

project = api.model('Project', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of a project'),
    'name': fields.String(required=False, description='Project name'),
    'description': fields.String(required=False, description='Project name'),
})
