from flask import Flask, render_template
import os

app = Flask(__name__, template_folder='')
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


@app.route('/')
def hello():
    return render_template('home.html')

app.run("0.0.0.0", port=int(os.environ.get('PORT', 5000)))