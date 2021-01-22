import os, random
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, Actors, Movies, db
from sqlalchemy import func

cajwt='eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ino3a2J2eDRMOUNJNDVtbFdCaUhTYiJ9.eyJpc3MiOiJodHRwczovL2Nmc2hwLmV1LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MDA3YTBhYWI0ZTc0NzAwNzE4N2QzOTciLCJhdWQiOiJjZnNocCIsImlhdCI6MTYxMTI5NTk2MCwiZXhwIjoxNjExMzgyMzYwLCJhenAiOiJpYjZRNVNNNlZxUGVlZG9KRzJWUGlCMjRuTjZSUEc3bSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiXX0.jaiyX_pkFUwRdc88AgT1PaJNX5bf2b57JARVmRbPLRC0QN5mjoxiztbQsfbEOkGDzf8BHehf0bc0nuDwwqt-Mto6ydhDGvh-UAidml8qzsHFoy_fqEmKMkmoJzRRW8cpxdXmINM83zNsDD_hoVKLOhd4VLDZFgnL8fVdudGGY-87PKm2o71Qn4np6RJlfd6C1stioUS7JSOfU8fTjtiNawIvCh_cRssynyydKndyRdqNVV5c2x3gr2j6Osk6v6BNWEsUZArdm1YlwcaorJluwTP4d8tBmwiR6knbG9s7WRU8H8UV53pZPmMMfz02MJT7e3zLyJRNenefKkDE37vrQw'
cdjwt='eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ino3a2J2eDRMOUNJNDVtbFdCaUhTYiJ9.eyJpc3MiOiJodHRwczovL2Nmc2hwLmV1LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MDA3YTEzZmIxNWNjZTAwNmFhNjIyYjIiLCJhdWQiOiJjZnNocCIsImlhdCI6MTYxMTI5NjA0NCwiZXhwIjoxNjExMzgyNDQ0LCJhenAiOiJpYjZRNVNNNlZxUGVlZG9KRzJWUGlCMjRuTjZSUEc3bSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiXX0.Z62dzaojqwkIOPkY7nnsp1vmz61Cumr7pkDgY-xZdHi9Tl70hVNwlDmXHqazoLNuMPlquxGN3b32xWN3GWt__nELk3X2tS3vxlFM9fmAUX45qVFvi3con6pcwhvNgIEXDpk7G8kocYS-nJhaALnMzyEp3NMdNhudHeP_d27_Q1lbEK5D_EFuNXfdW5rw0RMpRQeFYkIPWgSnXOC9hFH2hyf0jjZkNhQGqhMhn6R9gqimVW9o2PMoYeVBu_4W8E__C8dr6XauVpugCKoBFQ6Jxz4ikOkgzx5sECiQJF3zkCsaS5fKQJpZjDXyzBgvpUnYxSiawcekWmEvFSuSqj3HtA'
epjwt='eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ino3a2J2eDRMOUNJNDVtbFdCaUhTYiJ9.eyJpc3MiOiJodHRwczovL2Nmc2hwLmV1LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MDA3YTIxM2IxNWNjZTAwNmFhNjIyY2EiLCJhdWQiOiJjZnNocCIsImlhdCI6MTYxMTI5NjEwNiwiZXhwIjoxNjExMzgyNTA2LCJhenAiOiJpYjZRNVNNNlZxUGVlZG9KRzJWUGlCMjRuTjZSUEc3bSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIiwicG9zdDptb3ZpZXMiXX0.SuTTFeiItCcAvSoe2D-FbcNbAUgKfU-pq3okpXscD__M3VS94D8ecveQU_vScHCNiDRb9gtO8TnCTlCVdZHMnD1xCRIKn_nnXvXPiMSBzkGs-fqakRgRuXWfXoWh2q6MbeDdWdGdVWO5rR6zEupFP58cc1aIxG2uIGCdGFlR9iACUOFRBLtviJOt3izAyc1xcL15J5F8q7_WMEdG5Zyl-5KDjqZ8pXgy5jRhluRKowisqowvyoazEFtJ0AAFLcf6kJwI51BqwTMLBEJ01ClXfrO73d_HQxrJpf9ZBSRrE1leQf-i4gKjcML7ouZRVQAONtN_lUKNlE1dWITp4WR7EQ'

def get_headers(token):
    return {'Authorization': f'Bearer {token}'}
class CastingTestCase(unittest.TestCase):
    

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "casting"
        self.database_path = "postgres://{}/{}".format('localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        pass
    
    def test_actors(self):
        res = self.client().get('/api/actors', headers=get_headers(cajwt))
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors'])

    def test_movies(self):
        res = self.client().get('/api/movies', headers=get_headers(cajwt))
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])
    ###testing absence of movies or actors is unneccesary, cause user alwyas may want to delete them all and start over

    def test_actors_create(self):
        test_actor = {
            'name': 'testestloremipsum12345testtest',
            'age': '35',
            'gender': 'male'
            }
        res = self.client().post('/api/actors/create', json=test_actor, headers=get_headers(cdjwt))
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        deltestactor = Actors.query.filter_by(name='testestloremipsum12345testtest').first_or_404()
        db.session.delete(deltestactor)
        db.session.commit()
        db.session.close()

    def test_400_new_actors(self):
        test_actor = {
            'name': '',
            'age': '',
            'gender': '',
            }
        res = self.client().post('/api/actors/create', json=test_actor, headers=get_headers(cdjwt))
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "bad request")

    def test_movies_create(self):
        test_movies = {
            'title': 'testestloremipsum12345testtest',
            'release': '2021-01-20',
            }
        res = self.client().post('/api/movies/create', json=test_movies, headers=get_headers(epjwt))
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        deltesmovie = Movies.query.filter_by(title='testestloremipsum12345testtest').first_or_404()
        db.session.delete(deltesmovie)
        db.session.commit()
        db.session.close()

    def test_400_new_movies(self):
        test_movie = {
            'title': '',
            'release': '',
            }
        res = self.client().post('/api/movies/create', json=test_movie, headers=get_headers(epjwt))
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "bad request")        

    def test_actors_delete(self):
        db.session.add(Actors(
            name="testestloremipsum12345testtest",
            age="99",
            gender="female"
        ))
        db.session.commit()
        db.session.close()
        testactor = Actors.query.filter(Actors.name == 'testestloremipsum12345testtest').with_entities(Actors.id)
        for testactorid in testactor:
            print(testactorid[0])
        res = self.client().delete('/api/actors/delete/{}'.format(testactorid[0]), headers=get_headers(cdjwt))
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
    
    def test_404_delete_actors(self):
        #instead of giving a very big number, i queried the max id and add one to it. imagine our app grows so fast :)
        actors = Actors.query.with_entities(Actors.id).order_by(func.max(Actors.id)).group_by(Actors.id).limit(1)
        for maxIdq in actors:
            maxactor=int(maxIdq[0])
            absentidq=maxactor+1
            return absentidq
        res = self.client().delete('/api/actors/delete/{}'.absentidq, headers=get_headers(cdjwt))
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "not found")

    def test_movies_delete(self):
        db.session.add(Movies(
            title="testestloremipsum12345testtest",
            release="2021-01-20", 
        ))
        db.session.commit()
        db.session.close()
        testmovie = Movies.query.filter(Movies.title == 'testestloremipsum12345testtest').with_entities(Movies.id)
        for testmovieid in testmovie:
            print(testmovieid[0])
        res = self.client().delete('/api/movies/delete/{}'.format(testmovieid[0]), headers=get_headers(epjwt))
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_404_delete_movies(self):
        movies = Movies.query.with_entities(Movies.id).order_by(func.max(Movies.id)).group_by(Movies.id).limit(1)
        for maxIdq in movies:
            maxmovie=int(maxIdq[0])
            absentidq=maxmovie+1
            return absentidq
        res = self.client().delete('/api/movies/delete/{}'.absentidq, headers=get_headers(epjwt))
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "not found")


    def test_actors_edit(self):
        ##### to make sure unittest always finds a valid id. 
        actors = Actors.query.with_entities(Actors.id, Actors.name, Actors.age, Actors.gender).order_by(func.random()).limit(1)
        for actor in actors:
            print(actor)
        ##### even it is not neccesary just to see it visiual incrementing the age 1    
        age=int(actor.age)+1    
        edit_actor = {
            'name': actor.name,
            'age': age,
            'gender': actor.gender,
            }
        res = self.client().patch('/api/actors/edit/{}'.format(actor[0]), json=edit_actor, headers=get_headers(cdjwt))
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
    
    def test_404_actors_edit(self):
        actors = Actors.query.with_entities(Actors.id).order_by(func.max(Actors.id)).group_by(Actors.id).limit(1)
        for maxIdq in actors:
            maxactor=int(maxIdq[0])
            absentidq=maxactor+1
            return absentidq  
        edit_actor = {
            'name': 'a',
            'age': '1',
            'gender': 'female',
            }
        res = self.client().patch('/api/actors/edit/{}'.absentidq, json=edit_actor, headers=get_headers(cdjwt))
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "not found")

    def test_movies_edit(self):
        ##### to make sure unittest always finds a valid id randomly. 
        movies = Movies.query.with_entities(Movies.id, Movies.title, Movies.release).order_by(func.random()).limit(1)
        for movie in movies:
            print(movie)       
        edit_movie = {
            'title': movie.title,
            'release': movie.release,
            }
        res = self.client().patch('/api/movies/edit/{}'.format(movie[0]), json=edit_movie, headers=get_headers(cdjwt))
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_404_movies_edit(self):
        movies = Movies.query.with_entities(Movies.id).order_by(func.max(Movies.id)).group_by(Movies.id).limit(1)
        for maxIdq in movies:
            maxmovie=int(maxIdq[0])
            absentidq=maxmovie+1
            return absentidq  
        edit_movie = {
            'title': 'a',
            'release': '2021-01-20',
            }
        res = self.client().patch('/api/movies/edit/{}'.absentidq, json=edit_actor, headers=get_headers(cdjwt))
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        
    

if __name__ == "__main__":
    unittest.main()