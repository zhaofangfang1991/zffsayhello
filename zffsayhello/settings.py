# 配置文件，程序的配置项。.flaskenv用于存放项目环境变量
import os
from zffsayhello import app

dev_db = 'sqlite:///' + os.path.join(os.path.dirname(app.root_path), 'data.db') # 在.env这一级

SECRET_KEY = os.getenv('SECRET_KEY', '123546')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', dev_db)
