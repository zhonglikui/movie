from datetime import datetime

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@127.0.0.1:3306/movie'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


# 会员的数据模型
class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    name = db.Column(db.String(32), unique=True)  # 昵称
    pwd = db.Column(db.String(32))  # 密码
    email = db.Column(db.String(64), unique=True)  # 邮箱
    phone = db.Column(db.String(11), unique=True)  # 手机号码
    info = db.Column(db.Text)  # 个性简介
    face = db.Column(db.String(255), unique=True)  # 头像
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow())  # 注册时间
    uuid = db.Column(db.String(255), unique=True)  # 唯一标识符
    userlogs=db.relationship('userlog',backref='user')#会员日志外键关系关联
    def __repr__(self):
        return "<User %r>"% self.name

#会员登录日志
class Userlog(db.Model):
    __talename__="userlog"
    id=db.Column(db.Integer,primary_key=True)#编号
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'))#所属会员
    ip=db.COlumn(db.String(32))#登录IP
    addtime=db.Column(db.DateTime,index=True,default=datetime.utcnow())#登录时间