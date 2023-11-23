from flask import render_template, request, redirect, url_for

from app import app
from app.util.main import insert_data, shorten_url, get_data


@app.route("/", methods=("GET", "POST"))
def index():          
    if request.method == "POST":
        url = request.form.get('url')
        return redirect(url_for('.result', url=url))

    return render_template('public/index.html')

@app.route("/result")
def result():
    url = request.args['url']
    short_url = request.root_url+shorten_url()
    val = insert_data(url, short_url)

    return render_template('public/result.html', short_url=val)

@app.route("/<shorten_url>")
def redirect_to_original_url(shorten_url):
    shorten_url = request.root_url + shorten_url
    val = get_data(shorten_url)

    return redirect(val)




