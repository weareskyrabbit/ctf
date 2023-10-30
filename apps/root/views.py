from flask import Blueprint, render_template, redirect, url_for

root = Blueprint(
  "root",
  __name__,
  template_folder="templates",
  static_folder="static",
)

@root.route("/")
def index():
  return redirect(url_for("root.helloworld"))

@root.route("/helloworld")
def helloworld():
  return render_template("helloworld.html")