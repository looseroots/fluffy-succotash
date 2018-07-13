from flask import (redirect, url_for, render_template, flash, g, request)
from app import app
import os

@app.route('/')
def index():
    return render_template('index.html')