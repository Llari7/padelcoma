import os
from flask import Flask, url_for, request, render_template, redirect

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


    #@app.route("/")
    #def index():
        #return render_template("store/index.html")  

    @app.route("/login", methods=["POST", "GET"])
    def login():
        if request.method == "POST":
            return do_the_login()
        else:
            return render_template("auth/login.html")

    def do_the_login():
        return "login data"
    
    from . import auth
    app.register_blueprint(auth.bp)

    from . import store
    app.register_blueprint(store.bp)
    app.add_url_rule("/", endpoint="index")

    return app



