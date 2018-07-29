from flask import (redirect, url_for, render_template, flash, g, request,
                    session, jsonify)
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
    return render_template('index.html')

@app.route('/validate', methods=['GET', 'POST'])
def validate():
    start_location = request.args.get('start_location', 0, type=str)
    end_location = request.args.get('end_location', 0, type=str)
    
    return jsonify(result="start @ " + start_location + " and ending @ " + end_location)
