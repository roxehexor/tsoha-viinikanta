from application import app, db
from flask import redirect, render_template, request, url_for
from application.wines.models import Wine

@app.route("/wines", methods=["GET"])
def wines_index():
    return render_template("wines/list.html", wines = Wine.query.all())

@app.route("/wines/new/")
def wines_form():
    return render_template("wines/new.html")

@app.route("/wines/", methods=["POST"])
def wines_create():
    name = request.form['name']
    rating = request.form['rating']
    w = Wine(name, rating)
    db.session().add(w)
    db.session().commit()
  
    return redirect(url_for("wines_index"))