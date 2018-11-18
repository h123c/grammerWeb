#encoding:utf-8
import os

#import redis
from flask import Flask

from app.main.views import user_blueprint
#from App.models import db
#from datetime import timedalta


def create_app():
	#/aicoding/app
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    static_dir = os.path.join(BASE_DIR, 'static')
    templates_dir = os.path.join(BASE_DIR, 'templates')

    app = Flask(__name__,
                static_folder=static_dir,
                template_folder=templates_dir)
    #app.config['DEBUG']=True
    
    app.register_blueprint(blueprint=user_blueprint, url_prefix='/grammer')
 #    #配置缓存最大时间
	# app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds =1)

	# #配置session有效期
	# app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(seconds=1)
    #app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@127.0.0.1:3306/Htai'
    #app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # 设置session密钥
    #app.config['SECRET_KEY'] = 'secret_key'
    # 设置连接的redis数据库 默认连接到本地6379
    #app.config['SESSION_TYPE'] = 'redis'
    # 设置远程
    #app.config['SESSION_REDIS'] = redis.Redis(host='127.0.0.1', port=6379)

    #db.init_app(app=app)

    return app

if __name__ == "__main__":
    print(root_path)
