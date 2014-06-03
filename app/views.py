# -*- coding: utf-8 -*-

from app import app
from flask import render_template

@app.route('/')
def index():
	title = "Home"
	return render_template('index.html', title = title)


@app.route('/locations')
def locations():
	title = "DuckWorld"
	return render_template('locations.html', title = title)

@app.route('/search')
def search():
	title = "Search"
	return render_template('search.html', title = title)