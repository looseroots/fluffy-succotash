from flask import (redirect, url_for, render_template, flash, g, request)
from app import app
from app.forms import HomeForm
import os
import random

@app.route('/', methods=['GET', 'POST'])
def index():
    home_form = HomeForm()
    if home_form.validate_on_submit():
        return "Form submission successful!"

    return render_template(
        'index.html',
        navbar_emoji=random.choice(app.config['NAVBAR_EMOJIS']),
        home_form=home_form
    )