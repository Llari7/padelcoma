from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

from werkzeug.exceptions import abort

from pcoma.db import get_db

bp = Blueprint("store", __name__)

@bp.route("/", methods=["POST", "GET"])
def index():
    db, c = get_db()
    c.execute(
        "select brand, name, price, description, image from product"
        " order by brand"
    )
    products = c.fetchall()
    if request.method=="POST": 
        return products
    return render_template("store/index.html", products=products)
