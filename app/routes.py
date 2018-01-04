from app import app
from flask import Flask, render_template, flash, redirect
from app.forms import ContactForm

@app.route('/')
def index():
    return render_template('home.html', title='Home')

@app.route('/services')
def services():
    return render_template('services.html', title='Services')

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()

    if form.validate_on_submit():
        return 'Form posted.'
    return render_template('contact.html', form=form)

