from flask import flash,url_for,render_template,redirect
from zffsayhello import app,db
from zffsayhello.models import Message
from zffsayhello.forms import HelloForm

@app.route('/', methods=['POST', 'GET'])
@app.route('/index', methods=['POST', 'GET'])
def index():
    '''
    作用：显示数据库中所有的留言，并有一个提交留言的表单。
    :return:

    我的想法：先判断请求方式，
        如果是POST：用request来获取POST方式时，提交的数据
        如果是GET，就渲染页面，并显示从数据库请求的所有数据
    '''
    form = HelloForm()

    if form.validate_on_submit():
        name = form.name.data
        body = form.body.data

        message = Message(body=body,name=name)
        db.session.add(message)
        db.session.commit()

        flash('send a message to the world')
        return redirect(url_for('index'))

    messages = Message.query.order_by(Message.timestamp.desc()).all()
    return render_template('index.html', form=form, messages=messages)




