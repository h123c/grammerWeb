from flask import Blueprint, request, redirect, render_template#, url_for, session

#from App.models import db, User, Grade, Student, Role, Permission
#from utils.ch_login import is_login

user_blueprint = Blueprint('home', __name__)

@user_blueprint.route('/index', methods=['GET','POST'])
def index():
    if request.method == 'GET':
    	return render_template('index.html')

error_blueprint = Blueprint('error', __name__)
@error_blueprint.errorhandler(404)
def page_not_found(error):
    return render_template('not_found.html')
