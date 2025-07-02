import os


class Config:
    SECRET_KEY= os.getenv('SECRET_KEY', 'default_secret_key')
    DEBUG=True

class DevelopmentConfig(Config):
    JWT_VERIFY_SUB=False
    DEBUG=True

config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}
