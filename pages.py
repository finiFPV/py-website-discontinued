from flask import Blueprint, render_template, redirect, request, make_response
from functions import login

app = Blueprint('app', 'app')

@app.route('/', methods=['GET', 'POST'])
def main():
    if 'Credentials' in request.cookies:
        return make_response(f"return")
    else:
        return redirect('/login')

@app.route('/login')
def login_page():
    return render_template('login.html')

@app.route('/handle_data', methods=['POST'])
def handle_data():
    method = request.form['method']
    if method == 'Login':
        user = request.form['user']; password = request.form['pass']
        results = login(user, password)
        if results == 404: return redirect('/user-not-found')
        else: 
            response = make_response(redirect('/'))
            response.set_cookie('Credentials','AskPython')
            return response
    elif method == 'Register':
        ...

@app.route('/user-not-found')
def user_not_found():
    return make_response(f"user not found")