from flask import render_template, request, redirect
from models.models import create_link,search_link,query,app


@app.route('/<short_url>')

def redirect_to_url(short_url):
    link = search_link(short_url)
    return redirect(link.original_url) 


@app.route('/')

def index():
    return render_template('index.html') 
@app.route('/add_link', methods=['POST'])

def add_link():
    original_url = request.form['original_url']
    new_link = create_link(original_url)
    
    return render_template('link_added.html', 
        new_link=new_link.short_url, original_url=new_link.original_url)
@app.route('/stats')

def stats():
    links = query()

    return render_template('stats.html', links=links)

@app.errorhandler(404)
def handle_not_found(e):
    return render_template('404.html'),404