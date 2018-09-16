from . import db
from flask_login import UserMixin
from . import login_manager


from werkzeug.security import generate_password_hash, check_password_hash


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Blog(db.Model):
    __tablename__ = 'blog'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    body = db.Column(db.String)
    # Defining the foreign key from the relationship between a user and a pitch
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    # Defining the foreign key from the relationship between a pitch and a category

    comments = db.relationship(
        'Comment', cascade="all, delete-orphan", lazy="dynamic")

    def __repr__(self):
        return f'User {self.title}'


class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(255))
    comment = db.Column(db.String)

    blog_id = db.Column(db.Integer, db.ForeignKey("blog.id"))

    # Defining the foreign key from the relationship between a user and a comment
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def __repr__(self):
        return f'Comment {self.comment}'


class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), index=True)
    email = db.Column(db.String(255), unique=True, index=True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())

    password_hash = db.Column(db.String(255))

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'User {self.username}'
