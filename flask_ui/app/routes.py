#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 17 10:37:10 2019

@author: Jonny
"""
from flask import render_template
from app import app

@app.route('/')
def index():
    return render_template('tableau_viz.html', title='Invitation To Edit')

