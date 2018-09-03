
''' controller and routes for users '''
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

# Create and get Experiment
@app.route('/experiments', methods=['GET', 'POST', 'DELETE', 'PATCH'])
def experiments():
    if request.method == 'GET':
        return dumps(mongo.db.experiments.find()), 200

    data = request.get_json()
    LOG.info('request parameters: %s %s', data, type(data))
    if request.method == 'POST':
        if data.get('exp_name', None) is not None and data.get('train_split', None) is not None and data.get('type', None) is not None:
            #input_data = json.load(open(file_path))
            
            data['start_date'] = time.time()
            data['test_split'] = 100 - int(data['train_split'])
            mongo.db.experiments.insert_one(data)

            #[i for i in mongo.db.experiments.find({"_id": insert_res.insert_id})]
            return jsonify({'ok': True, 'message': 'Experiment created successfully!'}), 200
        else:
            return jsonify({'ok': False, 'message': 'Bad parameters to start a new experiment!'}), 400