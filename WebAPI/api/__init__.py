from flask import Flask
from api.modules.auth import Auth
from flask_pymongo import PyMongo


app = Flask(__name__)
auth = Auth()

app.config['MONGO_URI'] = 'URI GOES HERE'
app.secret_key = 'SECRET'

mongo = PyMongo(app)

from api.modules.update.routes import umod
from api.modules.get.routes import gmod

app.register_blueprint(gmod)
app.register_blueprint(umod)


if __name__ == '__main__':
    app.run()
