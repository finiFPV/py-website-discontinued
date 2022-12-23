from flask import Blueprint, render_template, redirect, request, make_response, session
from functions import Account
from json import dumps

app = Blueprint("app", "app")
Account = Account()
Main = Account.Main()


@app.route("/", methods=["GET", "POST"])
def main():
    if "Credentials" in request.cookies:
        return make_response(f"Logged in! (Work in progress...)")
    else:
        return redirect("/login")


@app.route("/login")
def login_page():
    if "Credentials" in request.cookies:
        return redirect("/")
    error = session.get("error")
    success = session.get("success")
    return render_template("login.html", error=error, success=success)


@app.route("/register")
def register():
    if "Credentials" in request.cookies:
        return redirect("/")
    error = session.get("error")
    success = session.get("success")
    return render_template("register.html", error=error, success=success)


@app.route("/handle_data", methods=["POST"])
def handle_data():
    def reset_message():
        try:
            for i in ["error", "success"]:
                if session[i] != None:
                    session[i] = None
        except:
            pass

    method = request.form["method"]

    if method == "Register":
        reset_message()
        return redirect("/register")

    elif method == "Back":
        reset_message()
        return redirect("/login")

    elif method == "Login":
        user = request.form["user"]
        if user == "":
            return redirect("/login")
        password = request.form["pass"]
        results = Main.login(user, password)
        if results == 404:
            reset_message()
            session["error"] = f"User: {user} not found!"
            return redirect("/login")
        elif results == 401:
            reset_message()
            session["error"] = f"Password for user is incorrect!"
            return redirect("/login")
        else:
            response = make_response(redirect("/"))
            response.set_cookie(
                "Credentials",
                bytes(dumps({"User": user, "Password": password}), encoding="utf-8"),
            )
            return response

    elif method == "Register Now":
        reset_message()
        user = request.form["user"]
        password = request.form["pass"]
        results = Main.register(user, password)
        for response in [
            (302, "error", f"Username: {user} already exists! Please use a different username.", "/register"),
            (201, "success", "Successfully registered! You can log in now.", "/"),
            (404, "error", "There was an internal server error! Please try again later", "/register"),
        ]:
            if results == response[0]:
                session[response[1]] = response[2]
                return redirect(response[3])