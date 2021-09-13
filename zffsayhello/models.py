from datetime import datetime
from zffsayhello import db

# 用于存放留言的Message
class Message(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    body = db.Column(db.String(200))
    name = db.Column(db.String(20))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, index=True) # 时间戳
