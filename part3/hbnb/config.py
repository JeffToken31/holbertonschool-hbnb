import os


class Config:
    SECRET_KEY=os.getenv('SECRET_KEY', 'default_secret_key')
    JWT_VERIFY_SUB=False
    DEBUG=True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///development.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True

class DevelopmentConfig(Config):
    DEBUG=True

config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}
