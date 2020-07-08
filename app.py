from flask import Flask, redirect, url_for
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from os import environ
from forms import CollectibleForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '211c8c0e484b5eec9d582727aefbf64e'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://' + \
                                        environ.get('MYSQL_USER') + \
                                        ':' + \
                                        environ.get('MYSQL_PASSWORD') + \
                                        '@' + \
                                        environ.get('MYSQL_HOST') + \
                                        ':' + \
                                        environ.get('MYSQL_PORT') + \
                                        '/' + \
                                        environ.get('MYSQL_DB_NAME')

db = SQLAlchemy(app)


class Collectibles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    cat = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return ''.join(
            [
                'Name: ' + self.name + '\n'
                                       'Category: ' + self.cat
            ]
        )


@app.route('/')
@app.route('/home')
def home():
    post_data = Collectibles.query.all()
    return render_template('home.html', title='Home', collectibles=post_data)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/add', methods=['GET', 'POST'])
def add():
    form = CollectibleForm()
    if form.validate_on_submit():
        post_data = Collectibles(
            name=form.name.data,
            cat=form.cat.data
        )
        db.session.add(post_data)
        db.session.commit()
        return redirect(url_for('home'))
    else:
        return render_template('post.html', title='Add Collectible', form=form)


@app.route('/delete')
def delete():
    db.session.query(Collectibles).delete()  # drops contents of table
    # db.drop_all()  # drops all the schemas
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/create')
def create():
    db.create_all()
    post = Collectibles(name='Spider Man', cat='Marvel')
    db.session.add(post)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run()
