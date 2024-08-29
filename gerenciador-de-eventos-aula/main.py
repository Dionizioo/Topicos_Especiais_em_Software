from flask import render_template, redirect, url_for
from config import app


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')


@app.route('/logout')
def logout():
    pass


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


@app.route('/create_event', methods=['GET', 'POST'])
def create_event():
    return render_template('create_event.html')


@app.route('/edit_event/<int:event_id>', methods=['GET', 'POST'])
def edit_event(event_id):
    return render_template('edit_event.html')


@app.route('/delete_event/<int:event_id>', methods=['POST'])
def delete_event(event_id):
    pass


if __name__ == '__main__':
    app.run(debug=True)
