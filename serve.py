from flask import Flask, render_template

app = Flask(__name__, template_folder='', static_url_path="")
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


@app.route('/s')
def hello():
    return render_template('index.html')

app.run("0.0.0.0", port=5000)