from flask import render_template
from app import app
# from .models import blogs
# from .forms import BlogForm
# Blog = blogs.Blog


@app.route('/')
def index():

    return render_template('index.html')


@app.route('/blog/<int:blog_id>')
def blog(blog_id):

    return render_template('new_blog.html', id=blog_id)
