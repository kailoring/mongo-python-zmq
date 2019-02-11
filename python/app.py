#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
A simple python web app
"""

__author__ = """
Ralph W. Crosby
crosbyrw@cofc.edu
College of Charleston
Charleston, SC
"""

# **************************************************

from flask import Flask
app = Flask(__name__)

# **************************************************

@app.route('/')
def hello_world():
    '''Just say hello to make sure it works
    '''
    return 'Python/Flask Dockerized for CSCI-459'

# **************************************************

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
