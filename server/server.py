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

from bson.objectid import ObjectId
import logging
import os
from pymongo import MongoClient
import pickle
import sys
import zmq

# **************************************************

client = MongoClient('mongo')
db = client.GradeBook

# **************************************************

def init():
    """
    Initialize the ZMQ socker
    """

    sock = zmq.Context().socket(zmq.REP)
    sock.bind(f"tcp://*:{os.environ['ZMQ_BIND_PORT']}")
    return sock

# **************************************************

def run(sock):
    """
    Loop processing requests:

       Wait for a message
       Depending on the command code in the message, do the database operation
    """

    while True:

        pmsg = pickle.loads(sock.recv())

        if pmsg['cmd'] == 'list':
            omsg = list(db.students.find())

        elif pmsg['cmd'] == 'delete':
            omsg = db.students.find_one_and_delete({'_id': ObjectId(pmsg['id'])})

        elif pmsg['cmd'] == 'create':
            grades = [float(grade) for grade in pmsg['grades'].split(',')]
            db.students.insert(dict(name=pmsg['name'], grades=grades))
            omsg = dict(rc=0)

        elif pmsg['cmd'] == 'update':
            grades = [float(grade) for grade in pmsg['grades'].split(',')]
            db.students.update_one({'_id': ObjectId(pmsg['id'])},
                                   {'$set': {'name': pmsg['name'],
                                             'grades': grades}})
            omsg = dict(rc=0)

        elif pmsg['cmd'] == 'findone':
            omsg = db.students.find_one({'_id': ObjectId(pmsg['id'])})

        sock.send(pickle.dumps(omsg))


# **************************************************

if __name__ == '__main__':
    run(init())
