from flask import render_template, flash, redirect, request

from app import app, db
from .forms import LoginForm
from .models import User, Team

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Ruggles'}
    posts = [
        {
            'author': {'nickname': 'Alex'},
            'body': 'Good Game'
        },
        {
            'author': {'nickname': 'Bill'},
            'body': 'Godlike!'
        }
    ]

    return render_template('index.html',
                           titel = 'Home',
                           user = user,
                           posts = posts)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="' + form.openid.data + '", remember_me=' + str(form.remember_me.data))
        return redirect('/index')
    return render_template('login.html',
                           title = 'Sign In',
                           form = form,
                           providers = app.config['OPENID_PROVIDERS'])

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

@app.route('/teams')
def team_all():
    lcs = Team.query.filter_by(region='LCS').all()
    lec = Team.query.filter_by(region='LEC').all()
    lpl = Team.query.filter_by(region='LPL').all()
    lck = Team.query.filter_by(region='LCK').all()
    return render_template('team_all.html', lcs=lcs, lec=lec, lpl=lpl, lck=lck)

@app.route('/team/<name>')
def team_profile(name):
    data = Team.query.filter_by(short_name=name).first()
    if data is None:
        return render_template('404.html'), 404
    return render_template('team.html', data=data)

@app.route('/select')
def select_user():
    ulist = User.query.all()
    print(ulist)
    for item in ulist:
        print(item.nickname)
    return ulist

@app.route('/add')
def add_user():
    user = User(nickname='nioge',email='nioge@email.com')
    db.session.add(user)
    db.session.commit()

@app.route('/test')
def test():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is %s</p>' % user_agent

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

