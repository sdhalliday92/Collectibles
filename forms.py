from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class CollectibleForm(FlaskForm):
    c_name = StringField(
        'Collectible Name',
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

    submit = SubmitField('Add Collectible')


class RegistrationForm(FlaskForm):
    first_name = StringField('First Name',
                             validators=[
                                 DataRequired(),
                                 Length(min=4, max=30)
                             ]
                             )

    last_name = StringField('Last Name',
                            validators=[
                                DataRequired(),
                                Length(min=4, max=30)
                            ]
                            )
    email = StringField('Email',
                        validators=[
                            DataRequired(),
                            Email()
                        ]
                        )
    password = PasswordField('Password',
                             validators=[
                                 DataRequired(),
                             ]
                             )
    confirm_password = PasswordField('Confirm Password',
                                     validators=[
                                         DataRequired(),
                                         EqualTo('password')
                                     ]
                                     )
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[
                            DataRequired(),
                            Email()
                        ])
    password = PasswordField('Password',
                             validators=[
                                 DataRequired(),
                             ])
    remember = BooleanField('Remember Me')

    submit = SubmitField('Login')


class UpdateAccountForm(FlaskForm):
    first_name = StringField('First Name',
                             validators=[
                                 DataRequired(),
                                 Length(min=4, max=30)
                             ]
                             )

    last_name = StringField('Last Name',
                            validators=[
                                DataRequired(),
                                Length(min=4, max=30)
                            ]
                            )
    email = StringField('Email',
                        validators=[
                            DataRequired(),
                            Email()
                        ]
                        )
    submit = SubmitField('Update')
