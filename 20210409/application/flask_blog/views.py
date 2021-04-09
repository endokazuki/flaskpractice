from flask import request,redirect,url_for,render_template,flash,session
#flask内のライブラリを活用する
#request:postされた(サーバ側に送信された)データのリクエスト（処理）を行う
#redirect:パスの転送を行う
#url_for:
#render_template:対象のHTMLファイルを出力する
#flash:ターミナルの出力をブラウザ上に表示する
#session:認証の時に使うライブラリ
from flask_blog import app
#app(Flaskの設定)を利用する

@app.route('/')
def show_entries():
    return render_template('entries/index.html')
    #entriesファイルにあるindex.htmlにアタッチする
@app.route('/login', methods=['GET','POST'])
def login():
    error = None
    if request.method =='POST':
        if request.form['username'] != app.config['USERNAME']:
            flash('ユーザ名が異なります')
        elif request.form['password'] != app.config['PASSWORD']:
            flash('パスワードが異なります')
        else:
            session['logged_in']=True
            flash('ログイン成功です')
            return redirect('/')
    return render_template('login.html')
#login.htmlで認証を行なっている
@app.route('/logout')
def logout():
    session.pop('logged_in',None)
    flash('ログアウトしました')
    return redirect('/')
