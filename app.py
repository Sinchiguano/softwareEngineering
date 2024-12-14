# pip install -r requirements.txt
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample data structure
tasks = []

# Route to display tasks
@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

# Route to add a task
@app.route('/add', methods=['POST'])
def add_task():
    task = request.form.get('task')
    if task:
        tasks.append({'task': task, 'completed': False})
    return redirect(url_for('index'))

# Route to mark task as complete
@app.route('/complete/<int:task_id>')
def complete_task(task_id):
    tasks[task_id]['completed'] = True
    return redirect(url_for('index'))

# Route to delete a task
@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    tasks.pop(task_id)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)# docker development
    # app.run(debug=True)/
