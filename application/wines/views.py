from flask import redirect, render_template, request, url_for
from application import app, db
from application.wines.models import Wine
from application.wines.forms import WineForm

@app.route("/wines", methods=["GET"])
def wines_index():
    return render_template("wines/list.html", wines = Wine.query.all())

@app.route("/wines/new/")
def wines_form():
    return render_template("wines/new.html", form = WineForm())

@app.route("/wines/", methods=["POST"])
def wines_create():
    form = WineForm(request.form)

    if not form.validate():
        return render_template("wines/new.html", form = form)

    w = Wine(form.name.data)
    w.rate = form.rate.data
    
    db.session().add(w)
    db.session().commit()
  
    return redirect(url_for("wines_index"))