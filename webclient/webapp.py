#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
A simple python web app that interfaces with a business logic server using ZeroMQ
"""

__author__ = """
Ralph W. Crosby
crosbyrw@cofc.edu
"""

# **************************************************

from flask import Flask, render_template, request, redirect, url_for
import os
import pickle
import zmq

app = Flask(__name__, template_folder='templates')

# zmq setup
sock = zmq.Context().socket(zmq.REQ)
sock.connect(f"tcp://server:{os.environ['ZMQ_REQ_PORT']}")

# **************************************************

def zmq_send_recv(msg):
    """
    Send a message to the server and wait for an answer

    Use Python's pickle capability to serialize/deserialize the data
    """
    sock.send(pickle.dumps(msg))
    return pickle.loads(sock.recv())

# **************************************************

@app.route('/', methods=['GET', 'POST'])
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

            rval = zmq_send_recv({'cmd': 'delete', 'id': id})
            msg = f'Deleted {rval["name"]}'

        elif cmd == 'update':

            return redirect(url_for("update", id=id))

    else:
        msg = ''

    students = zmq_send_recv({'cmd': 'list'})

    try:
        n_grades = max(len(s['grades']) for s in students)
    except ValueError:
        n_grades = 1

    return render_template('list.html',
                           students=students,
                           msg=msg,
                           n_grades=n_grades)

# **************************************************

@app.route('/create', methods=['GET', 'POST'])
def create():
    """
    Create a new student record
    """

    if request.method == 'POST':

        zmq_send_recv(dict(cmd='create',
                           name=request.form["name"],
                           grades=request.form["grades"]))

        return redirect(url_for("students"))

    return render_template('create.html')

# **************************************************

@app.route('/update', methods=['GET', 'POST'])
def update():
    """
    Update a new student record
    """

    if request.method == 'POST':

        zmq_send_recv(dict(cmd='update',
                           id=request.args['id'],
                           name=request.form["name"],
                           grades=request.form["grades"]))

        return redirect(url_for("students"))

    student = zmq_send_recv(dict(cmd='findone',
                                 id=request.args['id']))

    return render_template('update.html',
                           name=student['name'],
                           grades=(', ').join(str(grade) for grade in student['grades']))


# **************************************************

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
