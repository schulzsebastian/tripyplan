#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask

app = Flask(__name__,
            template_folder='../templates',
            static_folder='../static')
app.config.from_object('config.Local')

from auth import *
from api import *
from routings import *
