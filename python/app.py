#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
A simple python web app
"""

__author__ = """
Ralph W. Crosby
crosbyrw@cofc.edu
"""

# **************************************************

from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__, template_folder='templates')
client = MongoClient('mongo')
db = client.GradeBook

# **************************************************

@app.route('/', methods=['GET','POST'])
def students():
    '''Connect to the database and display the contents of the collection
    '''

    if request.method == 'POST':

        id = list(request.form.keys())[0]
        cmd = request.form[id]
        
        if cmd == 'add':
            msg='add a record'
            app.logger.info('add')
        elif cmd == 'delete':
            msg=f'delete: {id}'
            app.logger.info(f'delete: {id}')
        elif cmd == 'update':
            msg=f'update: {id}'
            app.logger.info(f'update: {id}')

    else:
        msg = ''    
        
    return render_template('list.html', students=db.students.find(), msg=msg)
        
# **************************************************

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
