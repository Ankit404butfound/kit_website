from flask import Flask, render_template

app = Flask(__name__, template_folder='', static_url_path="")
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


@app.route('/<filename>')
def hello(filename):
    return open('code.html', encoding="utf-8").read().replace("<--CODE_INSERTION_AREA-->", open(f"html/{filename}.html", encoding="utf-8").read())

app.run("0.0.0.0")