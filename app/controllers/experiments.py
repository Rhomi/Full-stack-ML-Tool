
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
LOG = logger.get_root_logger(__name__, filename=os.path.join(ROOT_PATH, 'output.log'))

# Create and get Experiment
@app.route('/experiments', methods=['GET', 'POST', 'DELETE', 'PATCH'])
def experiments():
	if request.method == 'GET':
		return dumps(mongo.db.experiments.find()), 200

	data = request.get_json()
	LOG.info('request parameters: %s %s', data, type(data))
	if request.method == 'POST':
		if data.get('exp_name', None) and data.get('train_split', None) and data.get('type', None):
			#input_data = json.load(open(file_path))

			data['start_date'] = time.time()
			data['test_split'] = 100 - int(data['train_split'])
			mongo.db.experiments.insert_one(data)

			#[i for i in mongo.db.experiments.find({"_id": insert_res.insert_id})]
			return jsonify({'ok': True, 'message': 'Experiment created successfully!'}), 200
		else:
			return jsonify({'ok': False, 'message': 'Bad parameters to start a new experiment!'}), 400

	if request.method == 'DELETE':
		if data.get('exp_name', None):
			LOG.info('Attempting to delete experiment : %s', data.get('exp_name'))
			db_response = mongo.db.experiments.delete_one({'exp_name': data['exp_name']})
			if db_response.deleted_count == 1:
				response = {'ok': True, 'message': 'experiment deleted'}
			else:
				response = {'ok': True, 'message': 'no experiment found'}
			return jsonify(response), 200
		else:
			return jsonify({'ok': False, 'message': 'Bad request parameters!'}), 400


	if request.method == 'PATCH':
		if data.get('query', {}):
			LOG.info('Attempting to patch experiment : %s', data.get('query'))
			#LOG.info('request query: %s', data.get('query'))
			mongo.db.experiments.update_one(data['query'], {'$set': data.get('payload', {})})
			#if data.get('exp_name', None, **kwargs):
			#    mongo.db.experiments.find_one_and_update({"exp_name": data['exp_name']}, 
			#                         {"$set": {"result": result}})
			return jsonify({'ok': True, 'message': 'experiment updated'}), 200
		else:
			return jsonify({'ok': False, 'message': 'Bad request parameters!'}), 400
