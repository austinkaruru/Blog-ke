from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, StringField
from wtforms.validators import Required, DataRequired


class BlogForm(FlaskForm):
    title = StringField('New Blog', validators=[DataRequired()])
    body = TextAreaField('Enter your Blog here', validators=[DataRequired()])
    submit = SubmitField('Submit')


class CommentForm(FlaskForm):
    comment = TextAreaField('Write a comment here',
                            validators=[DataRequired()])

    submit = SubmitField('Submit')


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.', validators=[Required()])
    submit = SubmitField('Submit')
