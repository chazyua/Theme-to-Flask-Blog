from app import app, db
from flask import render_template, url_for, request, redirect
from app.models import Post
from app.forms import PostForm


@app.route('/')
def index():
    return render_template('index-interactive_dark.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/blog-list-sidebar')
def bloglistsidebar():
    return render_template('blog-list-sidebar.html')

@app.route('/blog-singlepost-sidebar', methods=['GET', 'POST'])
def blogsinglepostsidebar():
    form = PostForm()
    context = {
        'form' : form,
        'posts' : Post.query.all()
    }
    if form.validate_on_submit():
        p = Post(
            name = form.name.data,
            email = form.email.data,
            comment = form.comment.data
        )
        db.session.add(p)
        db.session.commit()
        return redirect(url_for('blogsinglepostsidebar'))
    return render_template('blog-singlepost-sidebar.html', **context)

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

@app.route('/index-interactive_bright')
def indexinteractivebright():
    return render_template('index-interactive_bright.html')

@app.route('/index-interactive_dark')
def indexinteractivedark():
    return render_template('index-interactive_dark.html')

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