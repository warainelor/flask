from crypt import methods

from flask import Flask, render_template, redirect, flash, url_for
from forms import ContactForm

app = Flask(__name__)
app.secret_key = 'my_secret_key_123'

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        message = form.message.data
        flash('Message is successfully sent!', 'success')
        return render_template('contact.html', form=form, name=name, email=email, message=message)
    return render_template('contact.html', form=form)