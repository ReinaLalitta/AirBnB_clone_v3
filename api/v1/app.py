#!/usr/bin/python3
from flask import Flask, jsonify, make_response, request
from models import storage
from api.v1.views import app_views

app = Flask('v1')
app.register_blueprint(app_views)

@app.teardown_appcontext
def close_storage(exception):
    storage.close()
    if __name__ == "__main__":
        app.run(host='HBNB_API_HOST', port='HBNB_API_PORT', threaded=True)
