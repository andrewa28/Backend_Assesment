'''
Python file to manage the routes between API (app.py) and Database (Model/model.py)

Also, these "Request_Api routes are the ones the swagger calls in testing
'''

import json
from flask import abort, request, Blueprint
from Model import model as databaseModel

REQUEST_API = Blueprint('request_api', __name__)


def get_blueprint():
    """Return the blueprint for the main app module"""
    return REQUEST_API


@REQUEST_API.route('/Bids/All', methods=['GET'])
def get_all_bids():
    """Return all bids
    @return: 200: a dictionary of all known BIDS as a \
    flask/response object with application/json mimetype.
    """
    return_rows = databaseModel.get_allBids()
    return json.dumps(return_rows)


@REQUEST_API.route('/Bids', methods=['GET'])
def get_specificPetBids():
    """Return all bids for specific pet
    @return: 200: a dictionary of all known BIDS as a \
    flask/response object with application/json mimetype.
    """
    data = request.args.get('pet_id')
    return_rows = databaseModel.get_specificPetBids(data)
    if not return_rows:
        abort(404)

    return json.dumps(return_rows)



@REQUEST_API.route('/Bids/Insert', methods=['POST'])
def create_bid():
    """Create a book request record
    @param userID: post : the user ID
    @param petID: post : the pet ID
    @param money: post : money bidding on
    @return: 200: a new_uuid as a flask/response object \
    with application/json mimetype.
    @raise 400: misunderstood request
    """
    if not request.get_json(force=True):
        abort(400,"Bad data")
    data = request.get_json(force=True)


    if not data.get('user_id'):
        abort(400)
    if not data.get('pet_id'):
        abort(400)
    if not data.get('money') or data.get('money')<0:
        abort(400)

    databaseModel.insert_bid(data['pet_id'], data['user_id'], data['money'])

    resp = {"status": "succeed"}
    resp_code = 200

    return json.dumps(resp), resp_code