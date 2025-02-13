from flask import Blueprint, render_template, jsonify

views = Blueprint(__name__, "views")


@views.route("/")
def home():
    return render_template("index.html", name="Jimmy")


@views.route("/profile/<username>")
def profile(username):
    return render_template("index.html", name=username)


@views.route("/json")
def get_json():
    return jsonify({"name": "Ethan", "age": "17"})


@views.route("/data")
def get_data():
    data = request.json
    return jsonify(data)
