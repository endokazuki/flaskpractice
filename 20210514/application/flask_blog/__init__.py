from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#Flaskを使う

app = Flask(__name__)
app.config.from_object('flask_blog.config')

db = SQLAlchemy(app)

from flask_blog.views import views,entries
#処理命令をviews.py、entries.pyに受け渡す