from app import app
from flask import render_template, url_for

@app.route('/')
def index():
    return render_template('index-interactive_dark.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/blog-list-sidebar')
def bloglistsidebar():
    return render_template('blog-list-sidebar.html')

@app.route('/blog-singlepost-sidebar')
def blogsiglepostsidebar():
    return render_template('blog-singlepost-sidebar.html')

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

@app.route('/index-interactive_bright')
def indexinteractivebright():
    return render_template('index-interactive_bright.html')

# @app.route('/index-interactive_dark')
# def indexinteractivedark():
#     return render_template('index-interactive_dark.html')

@app.route('/index-parallax_dark')
def indexparallaxdark():
    return render_template('index-parallax_dark.html')

@app.route('/portfolio-grid_1')
def portfoliogrid1():
    return render_template('portfolio-grid_1.html')

@app.route('/portfolio-grid_2')
def portfoliogrid2():
    return render_template('portfolio-grid_2.html')

@app.route('/pricing')
def pricing():
    return render_template('pricing.html')