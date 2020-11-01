import os
class Config:
    HOSTNAME = '127.0.0.1'
    PORT = '3306'
    DATABASE = 'flask_shop'
    USERNAME = 'root'
    PASSWORD = 'root'

    DB_URI ="mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8mb4".format(username=USERNAME,password=PASSWORD,host=HOSTNAME,port=PORT,db=DATABASE)
    SQLALCHEMY_DATABASE_URI = DB_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = os.urandom(16)

    ALLOWED_IMG = set(['bmp','png','jpg','jpeg','gif'])
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    SERVER_IMG_UPLOADS = os.path.join(BASE_DIR,'flask_shop','static','img')
class DevelopmentConfig(Config):
    DEBUG = True
class ProductConfig(Config):
    pass


config_map = {
    'develop':DevelopmentConfig,
    'product':ProductConfig
}