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
from models import db, Current, Parent, GrandParent

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
    Parents = []
    for Parent in all_Parent:
        print(Parent.serialize())
        Parents.append(Parent.serialize())

    return jsonify(parents), 200    


# @app.route('/GrandParent', methods=['GET'])
# def get_all_current():    
#     all_grandParent = GrandParent.query.all()
#     GrandParents = []
#     for Parent in all_GrandParent:
#         print(GrandParents.serialize())
#         GrandParents.append(GrandParent.serialize())

#     return jsonify(Grand_parents), 200   

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)

