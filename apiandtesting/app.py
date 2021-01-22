import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy, functools
from flask_cors import CORS
from models import setup_db, Actors, Movies, db
from sqlalchemy import func
from auth import *
from flask_migrate import Migrate


def create_app(test_config=None):
  app = Flask(__name__)
  app.config.from_object('config')
  db.init_app(app)
  migrate = Migrate(app, db)
  
  @app.route('/')
  def apiindex():
      return ('You have successfully connected to our API.')

  @app.route('/api/actors')
  @requires_authapi('get:actors')
  def apiactors(token):
      try:
          actors=[actor.format() for actor in Actors.query.all()]
          return jsonify({
              'success': True,
              'actors': actors,
              })
      except:
          abort(422)

  @app.route('/api/movies')
  @requires_authapi('get:movies')
  def apimovies(token):
      try:
          movies = Movies.query.all()
          movies=[movie.format() for movie in Movies.query.all()]
          return jsonify({
              'success': True,
              'movies': movies,
              })
      except:
          abort(422)
  @app.route('/api/actors/delete/<int:actor_id>', methods=['GET', 'DELETE'])
  @requires_authapi('delete:actors')
  def apideleteactor(token, actor_id):
      actor = Actors.query.filter(Actors.id == actor_id).scalar()
      if actor is None:
          abort(404)
      try:
          actor.delete()
          db.session.commit()
          db.session.close()
          return jsonify({
              'success': True,
              })
      except:
          abort(422)
  @app.route('/api/actors/edit/<int:actor_id>', methods=['POST', 'PATCH'])
  @requires_authapi('patch:actors')
  def apieditactor(token, actor_id):
      form = request.json
      name = form['name']
      age = form['age']
      gender = form['gender']
      actor = Actors.query.get(actor_id)
      if actor is None:
          abort(404)
      try:
          actor.name = name
          actor.age = age
          actor.gender = gender
          db.session.commit()
          db.session.close()
          return jsonify({
              'success': True,
              })
      except:
          abort(422)

  @app.route('/api/movies/edit/<int:movie_id>', methods=['POST', 'PATCH'])
  @requires_authapi('patch:movies')
  def apieditmovie(token, movie_id):
      form = request.json
      title = form['title']
      release = form['release']
      movie = Movies.query.get(movie_id)
      if movie is None:
          abort(404)
      try:
          movie.title = title
          movie.release = release
          db.session.commit()
          db.session.close()
          return jsonify({
              'success': True,
              })
      except:
          abort(422)       
  @app.route('/api/movies/delete/<int:movie_id>', methods=['GET', 'DELETE'])
  @requires_authapi('delete:movies')
  def apideletemovie(token, movie_id):
      movie = Movies.query.filter(Movies.id == movie_id).scalar()
      if movie is None:
          abort(404)
      try:
          movie.delete()
          db.session.close()
          return jsonify({
              'success': True,
              })
      except:
          abort(422)
  @app.route('/api/actors/create', methods=['POST'])
  @requires_authapi('post:actors')
  def apicreate_actor_submission(token):
      cractoritems = request.json
      name=cractoritems['name']
      age=cractoritems['age']
      gender=cractoritems['gender']
      if len(name)>0 and len(age)>0 and len(gender)>0:
          print ('form ok!')
      else:
          abort(400)
      try:
          db.session.add(Actors(
              name=name,age=age,
              gender=gender,
              ))
          db.session.commit()
          db.session.close()
          return jsonify({
              'success': True,
              })
      except:
          abort(422)
  @app.route('/api/movies/create', methods=['POST'])
  @requires_authapi('post:movies')
  def apicreate_movie_submission(token):
      crmovieitems = request.json
      title=crmovieitems['title']
      release=crmovieitems['release']
      if len(title)>0 and len(release)>0:
          print ('form ok!')
      else:
          abort(400)
      try:
          db.session.add(Movies(
              title=title,
              release=release,
              ))
          db.session.commit()
          db.session.close()
          return jsonify({
              'success': True,
              })
      except:
          abort(422)

  
  @app.errorhandler(404)
  def notfound(error):
      return jsonify({
          'success': False,
          'error': 404,
          'message': 'not found'
          }), 404

  @app.errorhandler(422)
  def unprocessable(error):
      return jsonify({
          'success': False,
          'error': 422,
          'message': 'unprocessable'
      }), 422
      
  @app.errorhandler(400)
  def bad_request(error):
    return jsonify({
      "success": False, 
      "error": 400,
      "message": "bad request"
      }), 400

  @app.errorhandler(500)
  def server(error):
    return jsonify({
      "success": False, 
      "error": 500,
      "message": "internal server error"
      }), 500

  return app