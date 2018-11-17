from flask import Blueprint, request
import json
from api import mongo, auth

gmod = Blueprint('get', __name__, url_prefix='/get')


@gmod.route('/all', methods=['GET'])
@gmod.route('/', methods=['GET'])
def get():
    if not auth.get(request):
        return json.dumps({'message': 'Auth failed.'})

    db = mongo.db.data
    data = db.find_one({'_id': 'LINKS'})['data']['results']
    return json.dumps({'results': data})
