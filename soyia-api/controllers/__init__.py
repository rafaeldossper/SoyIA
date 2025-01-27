from flask import request, jsonify,Blueprint,make_response, request_started

from controllers.general import hello
from controllers.aiMethods import getGrainsEstimate
from controllers.upload import fileUpload

general_bp = Blueprint("general",__name__)
aiMethods_bp = Blueprint("aiMethods",__name__)
fileUpload_bp = Blueprint("fileUpload",__name__)

@general_bp.route("/",methods=['GET'])
def sayHello():
    res = hello()
    return res

@aiMethods_bp.route("/getGrains/<id>",methods=['GET'])
def grainsEstimate(id):
    res = getGrainsEstimate(id)
    return res

@fileUpload_bp.route("/upload",methods=['POST'])
def uploadFile():
    folderPath = request.get_json()['folderPath']
    file = request.get_json()['file']

    if(file is None):
        res = make_response({"mensagem":'falta arquivo'},400)
        return res

    if(folderPath is None):
        res = make_response({"mensagem":'falta caminho'},400)
        return res

    res = fileUpload(file,folderPath)
    return res