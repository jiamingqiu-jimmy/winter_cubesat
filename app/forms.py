from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms import validators


class ContactForm(FlaskForm):
    firstname = StringField('FirstName',
            [validators.DataRequired()])
    lastname = StringField('LastName',
            [validators.DataRequired()])
    email = StringField('Email Address', [validators.DataRequired(),
        validators.Email()])  
    subject = StringField('Subject', [validators.DataRequired()])
    message = TextAreaField('Message',
        [validators.DataRequired()])
    submit = SubmitField('Send')
