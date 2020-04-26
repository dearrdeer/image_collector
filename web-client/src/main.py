from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import json
import uuid
import base64

presentations = []

app = Flask(__name__)
CORS(app)
#images are base64 encoded!

@app.route('/', methods = ["GET"])
def url_explore():
    return jsonify(presentations)


@app.route('/create', methods = ["POST"])
def url_create(): 
    response_object = {'status': 'success', 'id': ''}
    if request.method == 'POST':
        pres = {
            'id' : uuid.uuid4().hex,
            'title': 'Untitled',
            'slides' : []
        }
        response_object['id'] = pres['id']
        presentations.append(pres)
        print("Presentation is saved to the database")
        return response_object

@app.route('/edit/<id>/<index>', methods = ["GET", "PUT"])
def url_edit(id, index):
    pres = {}
    for p in presentations:
        if p['id'] == id:
            pres = p
            break

    if request.method == 'GET':
        return jsonify(pres)
    else:
        try:
            title = request.form['title']
            pres['title'] = title
        except KeyError: 
            img = request.files['image']
            img_string = str(base64.b64encode(img.read()))[2:-1]
            pres['slides'][int(index)] = img_string
    
        print("Presentation is updated and saved to the database")
        return jsonify(pres)

@app.route('/add_slide/<id>', methods = ["GET", "POST"])
def url_add_slide(id):
    pres = {}
    for p in presentations:
        if p['id'] == id:
            pres = p
            break

    if request.method == 'GET':
        return jsonify(pres)
    else:
        pres['slides'].append("")
        print("Presentation is updated and saved to the database")
        return jsonify(pres)

@app.route('/delete_slide/<id>/<slide_id>', methods = ["GET", "DELETE"])
def url_delete_slide(id, slide_id):
    pres = {}
    for p in presentations:
        if p['id'] == id:
            pres = p
            break

    if request.method == 'GET':
        return jsonify(pres)
    else:
        pres['slides'].pop(int(slide_id))
        print("Presentation is updated and saved to the database")
        return jsonify(pres)

@app.route('/delete_pres/<id>', methods = ["GET", "DELETE"])
def url_delete_pres(id):
    pres = {}
    for p in presentations:
        if p['id'] == id:
            pres = p
            break

    if request.method == 'GET':
        return jsonify(pres)
    else:
        presentations.remove(pres)
        print("Presentation is updated and saved to the database")
        return jsonify(pres)

if __name__ == "__main__":
    app.run(debug = True)