import os
from flask import Flask, request, abort, jsonify, render_template, Response, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import setup_db, Movie, Actor, db
from auth import AuthError, requires_auth
from flask_migrate import Migrate


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    CORS(app)
    migrate = Migrate(app, db)
    #CORS(app, resources = {r"/api/": {"origins": "*"}})

    @app.after_request
    def after_request(response):
        response.headers.add(
            'Access-Control-Allow-Headers',
            'Content-Type,Authorization,true')
        response.headers.add(
            'Access-Control-Allow-Methods',
            'GET,PATCH,POST,DELETE')
        return response

    @app.route('/', methods=['GET'])
    def home_page():

        return render_template('pages/home.html')

        
    @app.route('/actors')
    @requires_auth('get:actors')
    def get_actors(jwt):

        try:
            # get the required actors information that we want to display
            actors_list = Actor.query.all()

            # abort 404 if we cannot get any results from the database
            if len(actors_list) == 0:
                abort(404)

            actors = [actor.format() for actor in actors_list]

            # return render_template('pages/actors.html', actors=actors)

            return jsonify({
                'success': True,
                'actors': actors
            }), 200

        except BaseException:
            abort(404)

    @app.route('/movies')
    @requires_auth('get:movies')
    def get_movies(jwt):
        # print(jwt)
        try:
            # get the required movies information that we want to display
            movies_list = Movie.query.all()

            # abort 404 if we cannot get any results from the database
            if len(movies_list) == 0:
                abort(404)

            movies = [movie.format() for movie in movies_list]

            return jsonify({
                'success': True,
                'movies': movies
            }), 200

            # return render_template('pages/movies.html', movies=movies)

        except BaseException:
            abort(404)

    # add a new actor to the database
    # it require "post:actors" permission for the user to add an actor

    @app.route("/actors", methods=['POST'])
    @requires_auth("post:actors")
    def post_actor(jwt):
        try:
            requested_body = request.get_json()
            name = requested_body['name']
            age = requested_body['age']
            gender = requested_body['gender']

            if 'movie_id' in requested_body:
                movie_id = requested_body['movie_id']
            else:
                movie_id = None

            # create a new actor object and insert it to the database
            actor = Actor(name=name, age=age, gender=gender, movie_id=movie_id)
            actor.insert()

            return jsonify({
                'success': True,
                'actors': [actor.format()]
            }), 200

        except BaseException:
            abort(422)

    # add a new movie to the database
    # it require "post:movies" permission for the user to add a movie

    @app.route("/movies", methods=['POST'])
    @requires_auth("post:movies")
    def post_movie(jwt):
        try:

            requested_body = request.get_json()
            title = requested_body['title']
            release_date = requested_body['release_date']

            # create a new movie object and insert it to the database
            movie = Movie(title=title, release_date=release_date)
            movie.insert()

            return jsonify({
                'success': True,
                'movies': [movie.format()]
            }), 200

        except BaseException:
            abort(422)

    # delete a specific actor from the database
    # it require "delete:actors" permission for the user to delete an actor

    @app.route('/actors/<actor_id>', methods=['DELETE'])
    @requires_auth('delete:actors')
    def delete_actor(jwt, actor_id):

        # return the required actor object that we want to delete it using
        # actor_id
        actor = Actor.query.get(actor_id)
        # abort 404 if we cannot find the actor object we want to delete
        if not actor:
            abort(404)

        try:
            # delete it form the database and commit
            actor.delete()

            return jsonify({
                'success': True, 'delete': actor_id
            }), 200

        except BaseException:
            abort(422)

    # delete a specific movie from the database
    # it require "delete:movies" permission for the user to delete a movie

    @app.route('/movies/<movie_id>', methods=['DELETE'])
    @requires_auth('delete:movies')
    def delete_movie(jwt, movie_id):

        # return the required movie object that we want to delete it using
        # movie_id
        movie = Movie.query.get(movie_id)
        # abort 404 if we cannot find the movie object we want to delete
        if not movie:
            abort(404)

        try:
            # delete it form the database and commit
            movie.delete()

            return jsonify({
                'success': True, 'delete': movie_id
            }), 200

        except BaseException:
            abort(422)

    # edit a specific actor information
    # it require "patch:actors" permission for the user to update these
    # information

    @app.route("/actors/<actor_id>", methods=['PATCH'])
    @requires_auth("patch:actors")
    def patch_actor(jwt, actor_id):

        # return the required actor object that we want to update using
        # actor_id
        actor = Actor.query.get(actor_id)
        # abort 404 if we cannot find the actor object we want to modify
        if not actor:
            abort(404)

        try:
            requested_body = request.get_json()

            # replace the new value of "name", "age" and "gender" with the old
            # ones
            if 'name' in requested_body:
                actor.name = requested_body['name']

            if 'age' in requested_body:
                actor.age = requested_body['age']

            if 'gender' in requested_body:
                actor.gender = requested_body['gender']

            if 'movie_id' in requested_body:
                actor.movie_id = requested_body['movie_id']

            # after that we commit the changes in the database
            actor.update()

            return jsonify({
                'success': True,
                'actors': [actor.format()]
            }), 200

        except BaseException:
            abort(422)

    # edit a specific movie information
    # it require "patch:movies" permission for the user to update these
    # information

    @app.route("/movies/<movie_id>", methods=['PATCH'])
    @requires_auth("patch:movies")
    def patch_movie(jwt, movie_id):

        # return the required movie object that we want to update using
        # movie_id
        movie = Movie.query.get(movie_id)
        # abort 404 if we cannot find the movie object we want to modify
        if not movie:
            abort(404)

        try:
            requested_body = request.get_json()

            # replace the new value of "title" and "release_date" with the old
            # ones
            if 'title' in requested_body:
                movie.title = requested_body['title']

            if 'release_date' in requested_body:
                movie.release_date = json.dumps(requested_body['release_date'])

            # after that we commit the changes in the database
            movie.update()

            return jsonify({
                'success': True,
                'movies': [movie.format()]
            }), 200

        except BaseException:
            abort(422)

    # Error Handling
    '''
    Example error handling for unprocessable entity
    '''

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
        }), 422

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "resource not found"
        }), 404

    @app.errorhandler(500)
    def internal_error(error):
        return jsonify({
            "success": False,
            "error": 500,
            "message": "internal server error"
        }), 500

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "bad request"
        }), 400

    @app.errorhandler(AuthError)
    def AuthError_handler(error):
        return jsonify(error.error), error.status_code

    return app


app = create_app()


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
    #APP.run(host='0.0.0.0', port=8080, debug=True)
