from flask import Flask, render_template
import os

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


@app.route('/')
def hello():
    return render_template("home.html")

@app.route("/<function>")
def render_function(function):
    return render_template("code.html", code_to_insert=open(f"templates/{function}.html", encoding="utf-8").read().replace("\n", ""))

app.run("0.0.0.0", port=int(os.environ.get('PORT', 5000)))