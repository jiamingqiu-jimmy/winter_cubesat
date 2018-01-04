from app import app
from flask import Flask, render_template, flash, redirect
from app.forms import ContactForm

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home') 

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()

    if form.validate_on_submit():
        return 'Form posted.'
    return render_template('contact.html', form=form)

