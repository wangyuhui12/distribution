# -*- coding:utf8 -*-
import sys
import os
from flask import jsonify
from flask_restful import Resource
from control.COrder import COrder
sys.path.append(os.path.dirname(os.getcwd()))

class AOrder(Resource):
    def __init__(self):
        self.corder = COrder()

    def post(self, order):
        print order
        apis = {
            'create_order': 'self.corder.create_order()',
        }
        res = eval(apis[message])
        return jsonify(res)

    def get(self, order):
        print order
        apis = {

        }
        res = eval(apis[message])
        return jsonify(res)