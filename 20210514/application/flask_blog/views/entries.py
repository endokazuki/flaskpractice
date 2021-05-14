from flask import request,redirect,url_for,render_template,flash,session
#flask内のライブラリを活用する
#request:postされた(サーバ側に送信された)データのリクエスト（処理）を行う
#redirect:パスの転送を行う
#url_for:URLのリンクを指定するライブラリ
#render_template:対象のHTMLファイルを出力する
#flash:ターミナルの出力をブラウザ上に表示する
#session:認証の時に使うライブラリ
from flask_blog import app
from flask_blog import db
from flask_blog.models.entries import Entry
#app(Flaskの設定)を利用する

@app.route('/')
def show_entries():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    entries= Entry.query.order_by(Entry.id.desc()).all()
    return render_template('entries/index.html',entries=entries)
    #entriesファイルにあるindex.htmlにアタッチする

@app.route('/entries/new',methods=['GET'])
def new_entry():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('entries/new.html')
    #entriesファイルにあるnew.htmlにアタッチする

@app.route('/entries',methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    entry = Entry(
        title=request.form['title'],
        text=request.form['text']
    )
    db.session.add(entry)
    db.session.commit()
    flash('新しい記事が作成されました')
    return redirect(url_for('show_entries'))
