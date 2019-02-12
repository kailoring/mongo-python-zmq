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

from flask import Flask, render_template, request, redirect, url_for, g
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__, template_folder='templates')
client = MongoClient('mongo')
db = client.GradeBook

# **************************************************

@app.route('/', methods=['GET','POST'])
def students():
    '''
    Connect to the database and display the contents of the collection
    '''

    if request.method == 'POST':

        id = list(request.form.keys())[0]
        cmd = request.form[id]
        
        if cmd == 'add':

            return redirect(url_for("create"))
            
        elif cmd == 'delete':

            rcd = db.students.find_one_and_delete({'_id' : ObjectId(id)})
            msg = f'Deleted {rcd["name"]}'
            
        elif cmd == 'update':
            
            msg=f'update: {id}'
            app.logger.info(f'update: {id}')

    else:
        msg = ''    

    students = list(db.students.find())
   
    try:
        n_grades = max(len(s['grades']) for s in students)
    except:
        n_grades = 1

    return render_template('list.html',
                           students=students,
                           msg=msg,
                           n_grades=n_grades)

# **************************************************

@app.route('/create', methods=['GET','POST'])
def create():
    """
    Create a new student record
    """
    
    if request.method == 'POST':

        name = request.form["name"]
        grades_text = request.form["grades"]

        grades = [float(grade) for grade in grades_text.split(',')]
 
        db.students.insert(dict(name=name, grades=grades))

        return redirect(url_for("students"))

    return render_template('create.html')


# **************************************************

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
