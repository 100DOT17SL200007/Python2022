from flask import Flask, render_template, url_for, flash, request
import sqlite3
import os

DATA = '/tmp/fsk.db'
DEBUG = True
SECRET_KEY = '00e5ac0533d63a946b67ef7b22477fa7bad987ae'

app = Flask(__name__)
# app.config['SECRET_KEY'] = 'DBHDGKJBNXFKJBNLDBNDLKB,B,ZMBLKJ'
app.config.update(dict(DATABASE=os.path.join(app.root_path, 'fsk.db')))

lis = [
    {"name": "Главная", "url": "main"},
    {"name": "Информация о компании", "url": "company"},
    {"name": "Добавить покупку", "url": ""},
]


def fw_db():
    c = sqlite3.connect(app.config['DATA'])
    c.row_factory = sqlite3.Row
    return c


def create_d():
    db = fw_db()
    with app.open_resource('s_db.sql', mode='r') as d:
        db.cursor().executescript(d.read())
    db.commit()
    db.close()


@app.route("/")
@app.route("/main")
def main():
    return render_template('main.html', title="Магазин цветов!!!", lis=lis)


@app.route("/company")
def company():
    return render_template('company.html', title="Информация о компании", lis=lis)


if __name__ == '__main__':
    app.run(debug=True)
