# -*- coding: utf-8 -*-
"""Create an application instance."""
from flsk_rest_template.app import create_app
from flask_restful import Resource, Api


app = create_app()

api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


api.add_resource(HelloWorld, '/')


if __name__ == '__main__':
    app.run(debug=True)