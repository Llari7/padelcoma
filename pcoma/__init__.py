import os
from flask import Flask, url_for, request, render_template

def create_app():

    app = Flask(__name__)

    app.config.from_mapping(
        SECRET_KEY="mikey",
        DATABASE_HOST=os.environ.get("FLASK_DATABASE_HOST"),
        DATABASE_USER=os.environ.get("FLASK_DATABASE_USER"),
        DATABASE_PASSWORD=os.environ.get("FLASK_DATABASE_PASSWORD"),
        DATABASE=os.environ.get("FLASK_DATABASE"),
    )
    
    from . import db

    db.init_app(app)


    @app.route("/")
    def index():
        return "<h1>PADELCOMA</h1>"

    @app.route("/login", methods=["POST", "GET"])
    def login():
        if request.method == "POST":
            return do_the_login()
        else:
            return render_template("auth/login.html")

    def do_the_login():
        return "login data"

    def show_the_login_form():
        return "<content>LOGIN HTML FORM</content>"

    @app.route("/user/<int:user_id>")
    def user(user_id):
        return f"<p>ID: {user_id}</p>"

    from . import auth
    app.register_blueprint(auth.bp)

    return app



