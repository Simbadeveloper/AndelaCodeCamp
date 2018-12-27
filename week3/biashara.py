"""
crud(create read update delete) for business
"""
from flask import Flask, jsonify, request, abort #importing libraries

app = Flask(__name__)

#store for business
business = [{
    'id':1,
    'company':'Andela',
    'title':'Programmer'
},
{
    'id':2,
    'company':'Google',
    'title':'Programmer'
},]


#index route
@app.route('/')
def home():
    """home function render home page"""
    return jsonify({"message" : "Welcome to Biashara Mashinani"}), 200

@app.route('/business', methods=['POST'])
def createbusiness():
    """
    route to create a new business
    """
    data = {
        "id":len(business),
        "company":request.json["company"],
        "title":request.json["title"]
    }
    business.append(data)
    return jsonify(data), 200

@app.route('/business', methods=['GET'])
def viewbusinesses():
    """
    route to view all business
    """
    return jsonify({"All business":business}), 200

@app.route('/business/<int:bizid>', methods=['GET'])
def viewonebusiness(bizid):
    """
    route to view one business
    """
    biz = [biz for biz in business if (biz['id'] == bizid)]
    return jsonify({'business':biz}), 200

@app.route('/business/<int:bizid>', methods=['PUT'])
def updatebusiness(bizid):
    """
    route to update a particular business
    """
    biz = [biz for biz in business if (biz['id'] == bizid)]

    if 'company' in request.json:
        biz[0]['company'] = request.json['company']

    if 'title' in request.json:
        biz[0]['title'] = request.json['title']
        return jsonify({'business':biz[0]})

    return jsonify({"message":"Your business was successful updated "})


@app.route('/business/<int:bizid>', methods=['DELETE'])
def deletebusiness(bizid):
    """
    route to delete a business using its id
    """
    biz = [biz for biz in business if (biz['id'] == bizid)]

    if len(biz) == 0:
        abort(404)

    business.remove(biz[0])
    return jsonify({'Message':'Your business was successful deleted'})

@app.errorhandler(404)
def route_not_found(error):
    """route to handle error"""
    return error

if __name__ == "__main__":
    app.run(debug=True, port=5000)
