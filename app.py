from flask import Flask, render_template, request
import json

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]

        new_data = {"name": name, "email": email}

        try:
            with open("data.json", "r") as file:
                data = json.load(file)
        except:
            data = []

        data.append(new_data)

        with open("data.json", "w") as file:
            json.dump(data, file)

    return render_template("index.html")


app.run(debug=True)