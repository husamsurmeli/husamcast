import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database


# TODO IMPLEMENT DATABASE URL
SQLALCHEMY_DATABASE_URI = 'postgres://yeavatnssrxsyv:95f17a21285484c359c3f197edf10e9580acee1ab9ca52b7a433e0c4c591eff6@ec2-54-158-1-189.compute-1.amazonaws.com:5432/dfmhmmv2vokrv2'
