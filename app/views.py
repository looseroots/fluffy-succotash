from flask import (redirect, url_for, render_template, flash, g, request, session)
from app.forms import HomeForm
from app import app
import datetime
import random
import os


@app.before_request
def pick_nav_emoji():
    if 'nav_emoji' not in session.keys():
        session['nav_emoji'] = random.choice(app.config['NAVBAR_EMOJIS'])

@app.route('/', methods=['GET', 'POST'])
def index():
    home_form = HomeForm()
    if home_form.validate_on_submit():
        home_form = [home_form.start_location.data,home_form.end_location.data, home_form.start_time.data, home_form.end_time.data]
        home_form = [str(field) for field in home_form]
        session['home_form'] = home_form
        return redirect(url_for('planner'))

    return render_template(
        'index.html',
        home_form=home_form
    )

@app.route('/planner', methods=['GET', 'POST'])
def planner():
    return render_template(
        'planner.html',
        start_location=session['home_form'][0],
        end_location=session['home_form'][1],
        start_time=session['home_form'][2],
        end_time=session['home_form'][3]
    )
