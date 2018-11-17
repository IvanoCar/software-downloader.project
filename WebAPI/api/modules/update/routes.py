from flask import Blueprint, request
import json
from api import mongo, auth

umod = Blueprint('update', __name__, url_prefix='/update')


@umod.route('/all', methods=['POST'])
def update():
    if not auth.post(request):
        return json.dumps({'message': 'Auth failed.'})

    data = request.get_data(as_text=True)
    try:
        data = json.loads(data)
    except json.JSONDecodeError:
        return json.dumps({'message': 'Invalid JSON'})

    db = mongo.db.data
    # db.remove({'_id': 'LINKS'})
    # db.insert({'_id': 'LINKS', 'data': data })
    db.update_one({'_id': 'LINKS'}, {'$set': {'data': data}})
    return json.dumps({'message': 'OK.'})
