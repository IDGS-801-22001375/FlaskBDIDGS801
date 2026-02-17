import os
from sqlalchemy import create_engine

class Config(object):
    SECRET_KEY = "Clave secreta"
    SESSION_COOKIE_SECURE = False

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:,vL&W}Z9dBXLJYjGGpux]itZ;-GNea_wgC{G}4Z6,gHX}.*hWh@127.0.0.1/bdidgs801'
    SQLALCHEMY_TRACK_MODIFICATIONS = False