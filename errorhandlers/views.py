from datetime import datetime

from flask import Blueprint, jsonify, request

errorhandlers = Blueprint('errorhandlers', __name__)


@errorhandlers.app_errorhandler(404)
def error_404(error):
    return jsonify({"url": request.url,
                    "status": f'{error}',
                    "datetime": datetime.now(),
                    "status_code": 404}), 404


@errorhandlers.app_errorhandler(500)
def error_500(error):
    return jsonify({"url": request.url,
                    "status": f'{error}',
                    "datetime": datetime.now(),
                    "status_code": 500}), 500


@errorhandlers.app_errorhandler(Exception)
def error_Exception(error):
    return jsonify({"url": request.url,
                    "method": request.method,
                    "status": f'{error}',
                    "datetime": datetime.now(),
                    "status_code": 500}), 500
