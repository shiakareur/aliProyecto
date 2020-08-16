import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'mysql+mysqldb://{DB_USER}:{DB_PASS}@{DB_ADDR}/{DB_NAME}'.format(DB_USER="alicorp1",
                                                                                               DB_PASS="alicorp1",
                                                                                               DB_ADDR="aliproyecto.cyillckb4hp6.us-east-1.rds.amazonaws.com",
                                                                                               DB_NAME="masterdata")
    SQLALCHEMY_TRACK_MODIFICATIONS = False