#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import render_template, redirect, url_for, abort
from flask_login import login_required, current_user
from models import *
from . import app


@app.route('/')
def index():
    if current_user.is_authenticated():
        return redirect(url_for('dashboard'))
    return render_template('index.html')


@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')


@app.route('/user/<nick>')
@login_required
def user(nick):
    if(nick == current_user.nick):
        return redirect(url_for('dashboard'))
    try:
        user = User.get(User.nick == nick)
        return render_template('user.html', user=user)
    except:
        abort(404)


@app.route('/plan/<pid>')
@login_required
def plan(pid):
    try:
        plan = Plan.get(Plan.id == unhash_id(pid))
        if plan.nick == current_user.nick:
            return render_template('plan.html', plan=plan)
        else:
            abort(403)
    except:
        abort(404)
