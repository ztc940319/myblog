# -*- coding: utf-8 -*-


import os
import sys

basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

# SQLite URI compatible
#WIN = sys.platform.startswith('win')
#if WIN:
#    prefix = 'mysql:///'
#else:
#    prefix = 'mysql:////'


class BaseConfig(object):    #基本配置类
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev key')

    DEBUG_TB_INTERCEPT_REDIRECTS = False

    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    #SQLALCHEMY_RECORD_QUERIES = True

    CKEDITOR_ENABLE_CSRF = True
    CKEDITOR_FILE_UPLOADER = 'admin.upload_image'

    MAIL_SERVER = os.getenv('MAIL_SERVER')
    MAIL_PORT = 465
    MAIL_USE_TLS = True
    #MAIL_USE_SSL = True
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = ('Myblog Admin', MAIL_USERNAME)

    MYBLOG_EMAIL = os.getenv('MYBLOG_EMAIL')
    MYBLOG_POST_PER_PAGE = 4
    MYBLOG_MANAGE_POST_PER_PAGE = 10
    MYBLOG_COMMENT_PER_PAGE = 4
    # ('theme name', 'display name')
    MYBLOG_THEMES = {'perfect_blue': 'Perfect Blue', 'black_swan': 'Black Swan'}
    MYBLOG_SLOW_QUERY_THRESHOLD = 1

    MYBLOG_UPLOAD_PATH = os.path.join(basedir, 'uploads')
    MYBLOG_ALLOWED_IMAGE_EXTENSIONS = ['png', 'jpg', 'jpeg', 'gif']


class DevelopmentConfig(BaseConfig):   #测试配置类
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    #SQLALCHEMY_DATABASE_URI = prefix + os.pa(th.join(basedir, 'data-dev.db')

class TestingConfig(BaseConfig):       #
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")  # in-memory database
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'


class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    #SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', prefix + os.path.join(basedir, 'data.db'))


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}
