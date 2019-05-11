from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError

class PostForm(FlaskForm):
    name  = StringField('', validators=[DataRequired()])
    email = StringField('', validators=[DataRequired()])
    comment = StringField('', validators=[DataRequired()])
    submit = SubmitField('POST COMMENT')