from flask import Flask
#Flaskを使う

app = Flask(__name__)

import flask_blog.views
#処理命令をviews.pyに受け渡す