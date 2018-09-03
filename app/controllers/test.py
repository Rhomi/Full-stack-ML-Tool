''' controller and routes for test '''
import os
from flask import request, jsonify
from app import app, mongo
from bson.json_util import dumps
from app.controllers import utils
import time
import json
import logger

ROOT_PATH = os.environ.get('ROOT_PATH')
LOG = logger.get_root_logger(
    __name__, filename=os.path.join(ROOT_PATH, 'output.log'))


# Test your model
@app.route('/test', methods=['GET', 'POST', 'DELETE', 'PATCH'])
def test():
    data = request.get_json()
    if request.method == 'POST':
        if data.get('file_name', None) is not None and data.get('exp_name', None) is not None:
            file_path = os.path.join(ROOT_PATH, data['file_name'])
            experiment = mongo.db.experiments.find_one({ "exp_name": data['exp_name']})
            result = utils.test_model(file_path, experiment)
            # updating results for the experiment
            mongo.db.experiments.find_one_and_update({"_id": experiment['_id']}, 
                                 {"$set": {"result": result}})
            return jsonify("Model test results ",result), 200
        else:
            return jsonify({'ok': False, 'message': 'Bad parameters for model testing!'}), 400

