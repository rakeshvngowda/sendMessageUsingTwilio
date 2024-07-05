from app import app
from flask import jsonify, request
from utils.sendMessage import SendMessageFromTwilio

class Routes:
    @app.route('/hello')
    def index():
        return jsonify({"msg": "Hello World"})

    @app.route('/sendMessage', methods=["POST"])
    def sendMessage():
        # get JSON Data from the request
        data = request.get_json()
        message = data.get('message')
        return SendMessageFromTwilio().send_message(message)
