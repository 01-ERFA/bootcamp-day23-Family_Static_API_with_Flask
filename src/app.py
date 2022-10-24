"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os, json
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/members', methods=['GET'])
def handle_hello():

    # this is how you can use the Family datastructure by calling its methods
    members = jackson_family.get_all_members()
    response_body = {
        "hello": "world",
        "family": members
        
    }


    return jsonify(response_body), 200

@app.route("/members", methods=["POST"])
def add_member():
    first_name= request.json.get("first_name", None)
    age = request.json.get("age", None) 
    lucky_numbers= request.json.get("lucky_numbers", None)
    new_members = {
        "first_name": first_name,
        "age": age,
        "lucky_numbers":lucky_numbers
        }
    
#crea el acceso y devuelve un token a las personas al loguearse
    members = jackson_family.add_member(new_members)

    
    response_body={
       
       "msg":"New member added"
        
    }
    return jsonify(response_body), 200

@app.route("/member/<int:member_id>", methods=["GET"])
def get_member(member_id):
   

    if jackson_family.get_member(member_id) != "":
            
        return jsonify({"member":jackson_family.get_member(member_id)}), 200
    elif jackson_family.get_member(member_id) == "":
        return jsonify({"msg":"member not found"}), 404
    
    return jsonify({"msg":"member not found"}), 404

@app.route("/members", methods=["DELETE"])
def delete_member():
    body=json.loads(request.data)
    if body is not None:
        key="id"
        if key in body:
            if jackson_family.delete_member(body["id"]) == True:
               return jsonify({ "done": "True"}), 200 
            else:
                return jsonify({"msg":"member not found"}), 404
            
                     
    return jsonify({"msg":"Action not acepted"}), 400


    
   

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
