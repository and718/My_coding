'''
1,加密的数据
2，算法 Python模块
3，秘钥 flask_app SECRET_KEY
'''

from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app,request
from flask_shop.models import User
from flask_shop.until.message import to_dict_msg
import functools



def generate_auth_token(uid,expiration):#第二个参数为token有效期
    #生成加密对象
    s = Serializer(current_app.config['SECRET_KEY'],expires_in= expiration)#第一个参数为要加密的秘钥
    #生成token
    return s.dumps({'id':uid}).decode()

def verify_auth_token(token_str):
    #创建解密对象
    s = Serializer(current_app.config['SECRET_KEY'])
    try:
        data = s.loads(token_str)
    except Exception:
        return None
    usr = User.query.filter_by(id=data['id']).first()
    return usr

def login_required(view_func):
    functools.wraps(view_func)  #用于防止参数丢失
    def verify_token(*arg,**kwargs):
        try:
            token = request.headers['token']  #获得前端请求头【headers】中的token
        except Exception:
            return to_dict_msg(10016)
        #创建解密对象
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except Exception:
            return to_dict_msg(10017)
        return view_func(*arg,**kwargs)
    return verify_token
