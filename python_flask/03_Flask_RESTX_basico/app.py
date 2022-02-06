from flask import Flask, request
from flask_restx import Api, Resource


app = Flask(__name__)
api = Api(app)


@api.route("/test")
class test(Resource):
    def get(self):
        return {"test": "first test"}


tasks = {"task1": "Estudar", "task2": "Treinar"}
print(tasks)


@api.route("/alltasks")
class AllTasks(Resource):
    def get(self):
        return tasks, 200


@api.route("/<string:todo_id>")
class TodoSimple(Resource):
    def get(self, todo_id):
        return {todo_id: tasks[todo_id]}, 200

    # put enviado como form title data e conteúdo
    def put(self, todo_id):
        tasks[todo_id] = request.form["data"]
        print(tasks)
        return {todo_id: tasks[todo_id]}, 201


if __name__ == "__main__":
    app.run(debug=True)
