import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash
from pcoma.db import get_db

bp = Blueprint("auth", __name__, url_prefix="/auth")


@bp.route("register", methods=("GET", "POST"))
def register():
    if request.method == "POST":
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
            error = f"User '{username}' is already registered."
        
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

@bp.route("/login", methods=("GET", "POST"))
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        db, c = get_db()
        error = None

        c.execute(
            "select * from user where username = %s",
            (username,)
        )
        user = c.fetchone()

        if user is None:
            error="Username or password incorrects"
        elif not check_password_hash(user["password"], password):
            error="Username or password incorrects"
        if error is None:
            session.clear()
            session["user_id"] = user["id"]
            return redirect(url_for("index"))

        flash(error)
    return render_template("auth/login.html")

