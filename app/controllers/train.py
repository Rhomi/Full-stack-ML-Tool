
''' controller and routes for train '''
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

# Train your model
@app.route('/train', methods=['GET', 'POST', 'DELETE', 'PATCH'])
def train():
    data = request.get_json()
    if request.method == 'POST':
        if data.get('file_name', None) is not None and data.get('exp_name', None) is not None:
            file_path = os.path.join(ROOT_PATH, data['file_name'])
            experiment = mongo.db.experiments.find_one({ "exp_name": data['exp_name']})
            result = utils.train_model(file_path, experiment)
            #mongo.db.users.insert_many(input_data)
            LOG.info('Result for model training: %s', result)
            return jsonify({'ok': True, 'message': result}), 200
        else:
            return jsonify({'ok': False, 'message': 'Bad parameters for model training!'}), 400
