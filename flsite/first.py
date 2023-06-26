from flask import Flask, render_template, url_for, g, request, flash, session, redirect
import sqlite3
import os
from FDataBase import FDataBase

DATABASE = '/tmp/flsk.db'
DEBUG = True
SECRET_KEY = 'e25d17506d812fc709c75584804bcb5b40e34a1d'

app = Flask(__name__)
app.config.from_object(__name__)
# app.config['SECRET_KEY'] = 'hgfsfhnghmgm'
app.config.update(dict(DATABASE=os.path.join(app.root_path, 'flsk.db')))
m = [
    {"name": "Главная", "url": "main"},
    {"name": "О компании", "url": "company"},
    {"name": "Обратная связь", "url": "connection"},
    {"name": "Добавление цветка", "url": "add_post"},

]

def connect_db():
    con = sqlite3.connect(app.config['DATABASE'])
    con.row_factory = sqlite3.Row
    return con

def create_db():
    db = connect_db()
    with app.open_resource('sq_db.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()


def get_db():
    if not hasattr(g, 'link_db'):
       g.link_db = connect_db()
    return g.link_db



@app.route("/")
def main():
    db = get_db()
    dbase = FDataBase(db)
    return render_template('main.html', title="Главная", m=dbase.get_menu(), posts=dbase.get_posts_annonce())

# dbase.get_menu()
@app.route("/add_post", methods=["POST", "GET"])
def add_post():
    db = get_db()
    dbase = FDataBase(db)

    if request.method == "POST":
        if len(request.form['name']) > 4 and len(request.form['post']) > 10:
            res = dbase.add_post(request.form['name'], request.form['post'], request.form['url'])
            if not res:
                flash('Ошибка добавления данных', category='error')
            else:
                flash("Данные добавлены успешно", category='success')
        else:
            flash("Данные добавлены успешно", category='error')


    return render_template('add_post.html', menu=dbase.get_menu(), title="Добавление цветка")

@app.route("/post/<alias>")
def show_post(id_post):
    db = get_db()
    dbase = FDataBase(db)
    title, post = dbase.get_post(alias)
    return render_template('post.html', menu=dbase.get_menu(), title=title, post=post)


@app.route("/company")
def company():
    print(url_for('company'))
    return render_template('company.html', title="О компании", m=m)



@app.route('/profile/<username>')
def profile(username):
    return f"Пользователь: {username}"

@app.route("/connection", methods=["POST", "GET"])
def connection():
    if request.method == 'POST':
        if len(request.form['username']) > 2:
            flash('Сообщение отправлено успешно!', category='success')
        else:
            flash('Ошибка отправки', category='error')
        # print(request.form)
        # context = {
        #     'username': request.form['username'],
        #     'email': request.form['email'],
        #     'message': request.form['message']
        #
        # }
        # return render_template('connection.html',**context, title="Обратная связ", menu=menu)
    return render_template('connection.html', title="Обратная связь ", m=m)



@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()

if __name__ == '__main__':
    app.run(debug=True)



