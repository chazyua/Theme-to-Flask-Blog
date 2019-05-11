from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError

class PostForm(FlaskForm):
    name  = StringField('', validators=[DataRequired()])
    email = StringField('', validators=[DataRequired()])
    comment = TextAreaField('', validators=[DataRequired()])
    submit = SubmitField('POST COMMENT')