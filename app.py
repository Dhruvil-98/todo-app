# app.py

from flask import Flask, render_template, request, redirect, url_for


def create_app():
    app = Flask(__name__)

    todos = []
    

    @app.route('/')
    def index():
        return render_template('index.html', todos=todos)

    @app.route('/add', methods=['POST'])
    def add_todo():
        todo = request.form.get('todo')
        if todo:
            todos.append(todo)
        return redirect(url_for('index'))

    @app.route('/delete/<int:todo_id>', methods=['POST'])
    def delete_todo(todo_id):
        if 0 <= todo_id < len(todos):
            todos.pop(todo_id)
        return redirect(url_for('index'))

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)
