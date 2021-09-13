import click
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_moment import Moment


app = Flask('zffsayhello')
bootstrap = Bootstrap(app)
moment = Moment(app)


app.config.from_pyfile('settings.py')
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

db = SQLAlchemy(app)
from zffsayhello import views, errors, commands # 因为这些模块也需要从构造文件中导入程序实例，为了避免循环依赖，这些导入语句写在构造文件的末尾




