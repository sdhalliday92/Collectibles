from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class PostsForm(FlaskForm):
    name = StringField(
        'Name',
        validators=[
            DataRequired(),
            Length(min=1, max=100)
        ]
    )

    cat = StringField(
        'Category',
        validators=[
            DataRequired(),
            Length(min=1, max=100)
        ]
    )

    submit = SubmitField('Add a collectible')
