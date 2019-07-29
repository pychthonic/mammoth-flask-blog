import json

"""
For full functionality, create a json file in your /etc folder 
called 'mfb_config.json with the following key/value pairs:
"""


with open('/etc/mfb_config.json') as config_file:
    config = json.load(config_file)


class Config:
    SECRET_KEY = config.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = config.get('SQLALCHEMY_DATABASE_URI')
    MAIL_SERVER = config.get('MAIL_SERVER')
    MAIL_PORT = int(config.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = config.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = config.get('MAIL_USERNAME')
    MAIL_PASSWORD = config.get('MAIL_PASSWORD')
    ADMINS = ['mammothflaskblog@gmail.com']
    MFB_EMAIL = "mammothflaskblog@gmail.com"
    SITE_NAME = "MAMMOTH FLASK BLOG"