import os
import markdown
from flask import Flask, request
from flask_restful import Resource, Api, abort, reqparse

app = Flask(__name__)
api = Api(app)

todo = {

    'todo1': {'task': 'Learn Flask-Restplus'},
    'todo2': {'task': 'Learn MERN stack'},
    'todo3': {'task': 'Learn Vuejs'}

}

def abort_if_todo_does_not_exist(todo_id):
    if todo_id not in todo:
        abort(404, message="Todo {} doesn't exist".format(todo_id))

def abort_if_id_exists(todo_id):
    if todo_id in todo:
        abort(404, message="Oops! Todo {} already exist".format(todo_id))

parser = reqparse.RequestParser()
parser.add_argument('task', required=True, help='Task cannot be empty : {error_msg}')


@app.route('/')
def index():
    """Present some documentation"""
    #Open the README file
    # with open('D:/Flask/apis/simple/README.md', 'r') as markdown_file:
    with open(os.path.dirname(app.root_path) + '/simple/README.md', 'r') as markdown_file:
        
        #Read the content of the file
        content = markdown_file.read()

        #convert it to HTML
        return markdown.markdown(content)


class ReadMe(Resource):
    def get(self):
        return {'message':'Hello There, Welcome to My ToDo List Flask-restful API'}


class ToDoSimple(Resource):
    def get(self, todo_id):
        abort_if_todo_does_not_exist(todo_id)
        return {todo_id: todo[todo_id]}, 200
    
    def delete(self, todo_id):
        abort_if_todo_does_not_exist(todo_id)
        del todo[todo_id]
        return '', 204
    
    def put(self, todo_id):
        args = parser.parse_args()
        task = {'tasks' : args['task']}
        todo[todo_id] = task
        return task, 201
        # todo[todo_id] = request.form['data']
        # return {todo_id: todo[todo_id]}


class TodoList(Resource):
    def get(self):
        return todo
    
    def post(self):
        args = parser.parse_args()
        t_id = int(max(todo.keys()).lstrip('todo')) + 1
        todo_id = 'todo%i' % t_id
        todo[todo_id] = {'task': args['task']}
        return todo[todo_id], 201


# api.add_resource(ReadMe, '/')
api.add_resource(TodoList, '/todos')
api.add_resource(ToDoSimple, '/todos/<string:todo_id>')


if __name__ == "__main__":
    app.run(debug=True)