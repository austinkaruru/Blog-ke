from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import Required


class BlogForm(FlaskForm):

    title = StringField('Review title', validators=[Required()])
    blog = TextAreaField('New Blog', validators=[Required()])
    submit = SubmitField('Submit')
