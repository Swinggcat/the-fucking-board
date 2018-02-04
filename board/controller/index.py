from .. import app, db
from ..model.Post import Post
from ..handler import session
from flask import render_template, request, url_for, redirect


@app.route('/')
def page_index():
    page = request.args.get('page', 1, type=int)
    pagination = Post.query.order_by(Post.id.desc()).paginate(page,per_page=32,error_out=False)
    posts = pagination.items

    return render_template('index.html', posts=posts, pagination=pagination, user=session.getname())


@app.route('/new',methods=['POST'])
def page_new():
    db.session.add(Post(session.getid(), request.form['content']))
    db.session.commit()
    return redirect(url_for('page_index'))


@app.route('/login',methods=['GET','POST'])
def page_login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        username = request.form['username']
        password = request.form['password']

        if session.login(username,password):
            return redirect(url_for('page_index'))
        else:
            return render_template('login.html', msg='You are not♂a♂philosopher!')


@app.route('/reg',methods=['GET','POST'])
def page_reg():
    if request.method == 'GET':
        return render_template('reg.html')
    else:
        if session.reg(request.form['username'], request.form['password']):
            return redirect(url_for('page_index'))
        else:
            return render_template('reg.html', msg='Fuck You!!!!!!!!!!!!!!')
