from . import db


class Blog:
    all_blogs = []

    # def __init__(self.blog):
    #     self.blog = blog

    def save_blog(self):
        Blog.all_blogs.append(self)

    @classmethod
    def clear_blogs(cls):
        Blog.all_blogs.clear()


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))

    def __repr__(self):
        return f'User {self.username}'
