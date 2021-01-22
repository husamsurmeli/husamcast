import json
from os import environ as env
from flask import Flask
from flask import jsonify
from flask import redirect
from flask import render_template
from loginhelper import *
import json
from flask import Flask, render_template, request, Response, redirect, url_for, jsonify
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import Form
from forms import *
from flask_migrate import Migrate
from datetime import datetime
from models import app, db, Actors, Movies
from sqlalchemy import Column, String, Integer, create_engine

app = Flask(__name__)
moment = Moment(app)
app.config.from_object('config')
db.init_app(app)
migrate = Migrate(app, db)
app.secret_key = constants.SECRET_KEY
app.debug = True

@app.errorhandler(Exception)
def handle_auth_error(ex):
  response = jsonify(message=str(ex))
  response.status_code = (ex.code if isinstance(ex, HTTPException) else 500)
  return response


@app.route('/')
def index():
  return render_template('pages/home.html')

@app.route('/callback')
def callback_handling():
  auth0.authorize_access_token()
  resp = auth0.get('userinfo')
  userinfo = resp.json()

  session[constants.JWT_PAYLOAD] = userinfo
  session[constants.PROFILE_KEY] = {
    'user_id': userinfo['sub'],
    'name': userinfo['name'],
    'picture': userinfo['picture']
    }
    return redirect('/casting')


@app.route('/casting')
def caating():
  return render_template('casting.html', userinfo=session[constants.PROFILE_KEY] )

@app.route('/actors')
def actors():
  actors = Actors.query.all()
  
  return  render_template('actors.html', actors=actors)

@app.route('/actors/delete')
def actorsdelete():
  actors = Actors.query.all()
  
  return  render_template('actorsdelete.html', actors=actors)

@app.route('/actors/delete/<int:actor_id>', methods=['GET', 'DELETE'])
def deleteactor(actor_id):
  actor = Actors.query.filter(Actors.id == actor_id).scalar()
  actor.delete()
  db.session.commit()
  db.session.close()
  return redirect(url_for('actors'))

@app.route('/actors/edit')
def actorsedit():
  actors = Actors.query.all()
  
  return  render_template('actorsedit.html', actors=actors)

@app.route('/actors/edit/<int:actor_id>', methods=['POST', 'PATCH'])
def editactor(actor_id):
  form = request.form
  name = form['name']
  age = form['age']
  gender = form['gender']
  actor = Actors.query.get(actor_id)
  actor.name = name
  actor.age = age
  actor.gender = gender
  db.session.commit()
  db.session.close()
  return redirect(url_for('actors'))

@app.route('/movies/edit')
def moviesedit():
  movies = Movies.query.all()
  
  return  render_template('moviesedit.html', movies=movies)

@app.route('/movies/edit/<int:movie_id>', methods=['POST', 'PATCH'])
def editmovie(movie_id):
  form = request.form
  title = form['title']
  release = form['release']
  movie = Movies.query.get(movie_id)
  movie.title = title
  movie.release = release
  db.session.commit()
  db.session.close()
  return redirect(url_for('movies'))


@app.route('/movies/delete')
def moviesdelete():
  movies = Movies.query.all()
  
  return  render_template('moviesdelete.html', movies=movies)

@app.route('/movies/delete/<int:movie_id>', methods=['GET', 'DELETE'])
def deletemovie(movie_id):
  movie = Movies.query.filter(Movies.id == movie_id).scalar()
  movie.delete()
  db.session.close()
  return redirect(url_for('movies'))

@app.route('/movies')
def movies():
  movies = Movies.query.all()
  
  return  render_template('movies.html', movies=movies)


@app.route('/actors/create', methods=['GET'])
def create_actor_form():
  form = ActorForm()
  return render_template('newactor.html', form=form)
@app.route('/actors/create', methods=['POST'])
def create_actor_submission():
    cractoritems = request.form
    db.session.add(Actors(
            name=cractoritems['name'],
            age=cractoritems['age'],
            gender=cractoritems['gender'],
        ))
    db.session.commit()
    db.session.close()
    return redirect(url_for('actors'))

@app.route('/movies/create', methods=['GET'])
def create_movie_form():
  form = MovieForm()
  return render_template('newmovie.html', form=form)

@app.route('/movies/create', methods=['POST'])
def create_movie_submission():
    crmovieitems = request.form
    db.session.add(Movies(
            title=crmovieitems['title'],
            release=crmovieitems['release'],
        ))
    db.session.commit()
    db.session.close()
    return redirect(url_for('movies'))


if __name__ == '__main__':
    app.run()
