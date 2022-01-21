from flask import Flask, render_template
import json
import os

import func_template

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


@app.route('/')
def hello():
    return render_template("home.html")

@app.route("/<function>")
def render_function(function):
    func_html = func_template.render_custom_template(json.load(open(f"static/json/{function}.json", encoding="utf-8")))
    return render_template("code.html", code_to_insert=func_html, title="PyWhatkit/"+function)#function_information=json.load(open(f"templates/json/{function}.json", encoding="utf-8")))

app.run("0.0.0.0", port=int(os.environ.get('PORT', 5000)))