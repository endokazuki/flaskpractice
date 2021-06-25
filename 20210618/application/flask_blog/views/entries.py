from functools import wraps
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
from flask_blog.views.views import login_required

@app.route('/')
@login_required
def show_entries():
    entries= Entry.query.order_by(Entry.id.desc()).all()
    return render_template('entries/index.html',entries=entries)
    #entriesファイルにあるindex.htmlにアタッチする

@app.route('/entries/new',methods=['GET'])
@login_required
def new_entry():
    return render_template('entries/new.html')
    #entriesファイルにあるnew.htmlにアタッチする

@app.route('/entries',methods=['POST'])
@login_required
def add_entry():
    entry = Entry(
        title=request.form['title'],
        text=request.form['text']
    )
    db.session.add(entry)
    db.session.commit()
    flash('新しい記事が作成されました')
    return redirect(url_for('show_entries'))

@app.route('/entries/<int:id>',methods=['GET'])
@login_required
def show_entry(id):
    entry= Entry.query.get(id)
    return render_template('entries/show.html',entry=entry)

@app.route('/entries/<int:id>/edit',methods=['GET'])
@login_required
def edit_show(id):
    entry= Entry.query.get(id)
    return render_template('entries/edit.html',entry=entry)

@app.route('/entries/<int:id>/update',methods=['POST'])
@login_required
def update_entry(id):
    entry= Entry.query.get(id)
    #各行のid,title,textを指す（1,CPU,PCの頭脳）
    entry.title=request.form['title']
    entry.text=request.form['text']
    #DBの内容を書き換える
    db.session.merge(entry)
    db.session.commit()
    #DBの更新を行う
    flash('記事が更新されました')
    return redirect(url_for('show_entries'))

@app.route('/entries/<int:id>/delete',methods=['POST'])
@login_required
def delete_entry(id):
    entry= Entry.query.get(id)
    db.session.delete(entry)
    db.session.commit()
    flash('投稿が削除されました')
    return redirect(url_for('show_entries'))

