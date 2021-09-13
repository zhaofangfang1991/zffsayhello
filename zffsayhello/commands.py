from zffsayhello import app,db
import click
from zffsayhello.models import Message

# 初始化数据库的initdb命令
@app.cli.commands('initdb')
@click.option('--drop', is_flag = True, help = 'drop db')
def init_db(drop):
    if drop:
        db.drop_all()
    db.create_all()
    click.echo('initialized database')

# 生成虚拟数据
@app.cli.commands('faker')
@click.option('--count', default=20, help='Quantity of messages, default is 20.')
def forge(count):
    from faker import Faker
    db.drop_all()
    db.create_all()

    fake = Faker()
    click.echo('Working...')
    for i in range(count):
        message = Message(
            name = fake.name(),
            body = fake.sentence(),
            timestamp = fake.date_time_this_year()
        )
        db.session.add(message)
    db.session.commit()
    click.echo('created fake messages!')