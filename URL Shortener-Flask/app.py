import os
from flask import Flask, render_template, request, flash
from utils import shorten_url
app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url_to_short']
        service = request.form['service']

        short_url, error = shorten_url(url, service)

        if error:
            flash(error)
            return render_template('index.html')

        return render_template('index.html', short_url=short_url)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)