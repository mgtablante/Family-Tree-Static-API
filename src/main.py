"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, Current, Parent, Grand_parent

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/current', methods=['GET'])
def get_all_current():    
    all_current= Current.query.all()
    currents = []
    for current in all_current:
        print(current.serialize())
        currents.append(current.serialize())

    return jsonify(currents), 200

@app.route('/parent', methods=['GET'])
def get_all_parent():    
    all_parent = Parent.query.all()
    parents = []
    for parent in all_parent:
        print(parent.serialize())
        parents.append(parent.serialize())

    return jsonify(parents), 200    


@app.route('/grand_parent', methods=['GET'])
def get_all_grand_parent():    
    all_grand_parent = Grand_parent.query.all()
    grand_parents = []
    for grand_parent in all_grand_parent:
        print(grand_parent.serialize())
        grand_parents.append(grand_parent.serialize())

    return jsonify(grand_parents), 200   

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)

