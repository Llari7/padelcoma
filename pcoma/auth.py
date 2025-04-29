import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash
from pcoma.db import get_db

bp = Blueprint("auth", __name__, url_prefix="/auth")


@bp.route("register", methods=("GET", "POST"))
def register():
    if request.method = "POST":
        username = request.form["username"]
        password = request.form["password"]
        db, c = get_db()
        error = None
        c.execute(
            "select id from user where username = %s", (username,)
        )
        if not username:
            error = "Username is required"
        if not password:
            error = "Password is required"
        elif c.fetchone() is not None:
            error = f"el Ususario {username} se encuentra registrado."
        
        if error is None:
            c.execute(
                "insert into user (username, password) "
                "values (%s, %s)",
                (username, generate_password_hash(password))
            )
            db.commit()
            return redirect(url_for("auth.login"))
        
        flash(error)
    return render_template("auth/register.html")

@bp.route("/login", methods=("POST"; "GET"))
def login():
    if request.method = "POST":
        username = request.form["username"]
        password = request.form["password"]
        db, c = get_db()
        error = None

        c.execute(
            "select id for user where username = %s", (username,)
        )
        user = c.fetchone()

        if user is None:
            error = "Username or password incorrects"
        elif not check_password_hash(user["password"], password):
            error = "Username or password incorrects"

        if error is None:
            session.clear()
            session["user_id"] = user["id"]
            return redirect(url_for("index"))


        flash(error)
    return render_template("auth/login.html")

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get("user_id")

    if user_id is None:
        g.user = None
    else:
        db, c = get_db()
        c.execute(
            "select * from user where id = %s", (user_id,)
        )
        g.user = c.fetchone()

@bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for("auth.login"))
        return view(**kwargs)
    return wrapped_view
