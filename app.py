from flask import Flask, redirect, url_for, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import UserMixin, LoginManager, login_user, logout_user, login_required, current_user
from wtforms.validators import ValidationError
from forms import CollectibleForm, RegistrationForm, LoginForm, UpdateAccountForm, UpdateCollectibleForm
from os import environ
from datetime import datetime


app = Flask(__name__)
bcrypt = Bcrypt(app)

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
                                        environ.get('MYSQL_DB_NAME2')

db = SQLAlchemy(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'


class Collectibles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    c_name = db.Column(db.String(100), nullable=False)
    cat = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        return ''.join([
            'User ID: ', self.user_id, '\r\n',
            'Name: ', self.name, '\r\n', self.cat
        ])


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(250), nullable=False)
    entry = db.relationship('Collectibles', backref='author', lazy=True)

    def __repr__(self):
        return ''.join(['UserID: ', str(self.id), '\r\n',
                        'Email: ', self.email], '\r\n',
                       'Name: ', self.first_name, ' ', self.last_name
                       )


@login_manager.user_loader
def load_user(id):
    return Users.query.get(int(id))


@app.route('/')
@app.route('/home')
def home():
    post_data = Collectibles.query.all()
    return render_template('home.html', title='Home', collectibles=post_data)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hash_pw = bcrypt.generate_password_hash(form.password.data)
        user = Users(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            email=form.email.data,
            password=hash_pw
        )

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('home'))

    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            if next_page:
                return redirect(next_page)
            else:
                return redirect('home')
    return render_template('login.html', title='Login', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        current_user.first_name = form.first_name.data
        current_user.last_name = form.last_name.data
        current_user.email = form.email.data
        db.session.commit()
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.first_name.data = current_user.first_name
        form.last_name.data = current_user.last_name
        form.email.data = current_user.email
    return render_template('account.html', title='Account', form=form)


@app.route("/account/delete", methods=["GET", "POST"])
@login_required
def account_delete():
    user = current_user.id
    collectibles = Collectibles.query.filter_by(user_id=user)
    for entry in collectibles:
        db.session.delete(entry)
    account = Users.query.filter_by(id=user).first()
    logout_user()
    db.session.delete(account)
    db.session.commit()
    return redirect(url_for('register'))


@app.route('/addcollectible', methods=['GET', 'POST'])
@login_required
def add():
    form = CollectibleForm()
    if form.validate_on_submit():
        post_data = Collectibles(
            c_name=form.c_name.data,
            cat=form.cat.data,
            user_id=current_user.id
        )
        db.session.add(post_data)
        db.session.commit()
        return redirect(url_for('home'))
    else:
        return render_template('addcollectible.html', title='Add Collectible', form=form)


@app.route('/updatecollectible/<int:update>', methods=['GET', 'POST'])
@login_required
def updatecollectible(update):
    form = UpdateCollectibleForm()
    collectibleupdate = Collectibles.query.filter_by(id=update).first()
    if form.validate_on_submit():
        collectibleupdate.name = form.c_name.data
        collectibleupdate.cat = form.cat.data
        db.session.commit()
        return redirect(url_for('home'))
    elif request.method == 'GET':
        form.c_name = collectibleupdate.name
        form.cat = collectibleupdate.cat
    return render_template('updatecollectible.html', title='Update Collectible', form=form)


@app.route('/deletecollectible/<int:delete>', methods=["GET", "POST", "DELETE"])
@login_required
def deletecollectible(delete):
    collectibledelete = Collectibles.__table__.delete().where(Collectibles.id == delete)
    db.session.execute(collectibledelete)
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/delete')
def delete():
    db.session.query(Collectibles).delete()  # drops contents of table
    # db.drop_all()  # drops all the schemas
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/create')
def create():
    db.create_all()
    db.session.commit()
    return redirect(url_for('home'))


def validate_email(self, email):
    if email.data != current_user.email:
        user = Users.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email already in use')


if __name__ == '__main__':
    app.run()
