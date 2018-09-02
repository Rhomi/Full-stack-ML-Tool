
''' controller and routes for users '''
import os
from flask import request, jsonify
from app import app, mongo
from bson.json_util import dumps
import json
import logger

ROOT_PATH = os.environ.get('ROOT_PATH')
LOG = logger.get_root_logger(
    __name__, filename=os.path.join(ROOT_PATH, 'output.log'))


@app.route('/user', methods=['GET', 'POST', 'DELETE', 'PATCH'])
def user():
    if request.method == 'GET':
        #query = request.args
        #data = mongo.db.users.find()
        #return dumps(mongo.db.users.find()), 200
        #return jsonify(dumps(mongo.db.users.find())), 200 #  It turns the JSON output into a Response object with the application/json mimetype.
        #return json.loads(mongo.db.users.find()), 200
        return jsonify(dumps(mongo.db.users.find())), 200


    data = request.get_json()
    if request.method == 'POST':
        if data.get('file_name', None) is not None:
            file_path = os.path.join(ROOT_PATH, data['file_name'])
            input_data = json.load(open(file_path))
            mongo.db.users.insert_many(input_data)
            return jsonify({'ok': True, 'message': 'User created successfully!'}), 200
        else:
            return jsonify({'ok': False, 'message': 'Bad request parameters!'}), 400

    