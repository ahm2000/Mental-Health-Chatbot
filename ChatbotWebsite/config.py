import os

# Config class to store all the configuration variables


class Config:
    DEBUG = False
    SECRET_KEY = "fy37n!fs9b#rk@s2l*$p6q&"
    # contain mysql database url with user and password
    # SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/users' #mysql
    SQLALCHEMY_DATABASE_URI = 'sqlite:///users.db'  #Alternative database if mysql not working
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = "hamzatera007@gmail.com"
    MAIL_PASSWORD = "hcfp qdiz tymv amne"
