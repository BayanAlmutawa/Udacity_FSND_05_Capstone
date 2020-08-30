# Udacity Full Stack Nanodegree (FSND) 

## Capstone App (Casting Agency)
The Casting Agency is a company that is responsible for creating movies and managing and assigning actors to those movies. 

## Getting Started

### Installing Dependencies

This will install all of the required packages we selected within the `requirements.txt` file.

```bash
pip install -r requirements.txt
```


### Running the server

within the root directory of the project, run the server:

```bash
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.
Setting the `FLASK_APP` variable to `app.py` directs flask to run `app.py` and run the application. 



## Database Setup
With Postgres running, restore a database using the capstone.psql file provided. From the terminal run:
```bash
psql capstone < capstone.psql
```


## Authentication using Auth0
in this application we rely on using Auth0 to ensure authentication. we have defferent Roles and Permissions.

### Auth0 Roles and Permissions
We have three types of roles and each role has its own permissions:
You can access to the app using this link and login with the following user information based on the role you need to test:
https://fsnd-bayan.us.auth0.com/authorize?audience=capstone&response_type=token&client_id=XIVuaEcQD8SrLBR6ms6jdgAqT82MsJWE&redirect_uri=http://127.0.0.1:5000/


#### Casting Assistant
Can view actors and movies
- get:actors
- get:movies

Login Information:

email: test_Assistant@hotmail.com
password: Aa@123456

jwt_token:
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ijl6elZkMGZhUEZYWVdLek5iYmNOSSJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtYmF5YW4udXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVmNGFlNjVmYzY0NzhiMDA2N2Q4NmU4YiIsImF1ZCI6ImNhcHN0b25lIiwiaWF0IjoxNTk4NzQ0MjI2LCJleHAiOjE1OTg3NTE0MjYsImF6cCI6IlhJVnVhRWNRRDhTckxCUjZtczZqZGdBcVQ4Mk1zSldFIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyJdfQ.EeBOgN4rVzEjmzzliaTBdsBjvd9KI453HDWOtgdPg0ukHXo-43KX9Bw8sMIMd6auEs0paVI8sBwsk8Nmti6EQ15-Jkgr_Gsnzu6LyyG-Solc-lgdybU99FZoxiHa-dBkUr_MeOBSfiQNPq4kwBvFHiuMEAATMD3F1NyTdNs9P49RmkKbSxv1DbgJDoDdUX9JAqwPrRW9XOj_7FzqSySv58wDW5pL0LQVxkyEkrlGG73A9JN38GKfiJJJEXovl3_ccSkd1vKcnc_NfHSlhHMwumI1blrWNCDSGFEGeZ9H13JgAzwZNE-qrkp4qpXdauVvN5gXj7DRxWP0yixCz14B4Q


#### Casting Director
All permissions a Casting Assistant has and some additional permissions:

Add or delete an actor from the database
- post:actors
- delete:actors

Modify actors or movies
- patch:actors
- patch:movies

Login Information:

email: test_Director@hotmail.com
password: Aa@123456

jwt_token:
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ijl6elZkMGZhUEZYWVdLek5iYmNOSSJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtYmF5YW4udXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVmNGFlNGIzMjA3NmE3MDA2NzhlZTM0NyIsImF1ZCI6ImNhcHN0b25lIiwiaWF0IjoxNTk4NzQzODM0LCJleHAiOjE1OTg3NTEwMzQsImF6cCI6IlhJVnVhRWNRRDhTckxCUjZtczZqZGdBcVQ4Mk1zSldFIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyJdfQ.n9CyoZnfDJkUawMc3hr-opqLHU3Aawki30gSkhZ4NmGw4WIXoK3uV8lfbSedUy0nK7_pQLHZ2GJwpLvk7oWeDKf83TQNoG5bQ_Vkpbs1_bj-dz9lSsCRGg9j4CRfp9P3nL93kQV0zyUvXRkpWGmSXQRCSs9QWuQ-5bc1wgCYUoa5IlggtQKscgKHZiFxtE_qtQT7LfBoEpchzOLk6NdBujLZErfKETNLGJ9dqzxklEiamxJXM9eXnXaxcPB0ESOw1mrsmVFd-HNCEUKJ65PcvW0XZJRTIWjbNGjztit5kfMVMrqvh7zWz_7DRbvZxtkaBHINe_ojqsqDGk20KN3Z_w


#### Executive Producer
All permissions a Casting Director has and some additional permissions:

Add or delete a movie from the database
- post:movies
- delete:movies

Login Information:

email: test_Executive@hotmail.com
password: Aa@123456

jwt_token:
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ijl6elZkMGZhUEZYWVdLek5iYmNOSSJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtYmF5YW4udXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVmNGFlNTdjZTllZjVmMDA2N2I1YWRmNiIsImF1ZCI6ImNhcHN0b25lIiwiaWF0IjoxNTk4NzQ0MDE3LCJleHAiOjE1OTg3NTEyMTcsImF6cCI6IlhJVnVhRWNRRDhTckxCUjZtczZqZGdBcVQ4Mk1zSldFIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.S9e35aXVF9C0I-WP_BC852dUGLrIBKY8ppcyBeaFasV7CYEybkyh4GrQDNR87AO-PtG1yi11GqybVcTAVspT29lMosGITSuRc1wnYiDj7GEY47KKG28myX00coqFucTFwcrqFVX3tIKBcMHaGkDrMg5Zz3QijTNdPPF7clMthOE0ItNxZSY-vb9-SMfgWGJjuDvi0fJVYHz7YXU5mrFQLHtGiVawQ5JKrYq8xbTe35AqwzERMpug2EstILxDQsVBBSxWmIPlA82saavEJJ-i908NdObEBUPbZydXdUbLJ96AsTS6OwpdvDqXK-QY-kMLKGYpOwY6H6XE797JJ5taZQ


## Endpoints

to test the endpoints you need to replace (jwt_token) by the actual value of valid jwt_token in all these curl requests.

### GET '/actors'
get a dictionary of all actors information from the database: 
` curl -H "Authorization: bearer jwt_token" http://127.0.0.1:5000/actors `

- Request Arguments: jwt_token
- Returns: 

```
{
  "actors": [
    {
      "age": 24,
      "gender": "female",
      "id": 1,
      "movie_id": null,
      "name": "bayan"
    },
    {
      "age": 19,
      "gender": "female",
      "id": 3,
      "movie_id": null,
      "name": "sara"
    },
    {
      "age": 33,
      "gender": "male",
      "id": 2,
      "movie_id": null,
      "name": "ibrahim"
    },
    {
      "age": 37,
      "gender": "male",
      "id": 4,
      "movie_id": null,
      "name": "Ahmed"
    }
  ],
  "success": true
}


```


### GET '/movies'
get a dictionary of all movies information from the database: 
` curl -H "Authorization: bearer jwt_token" http://127.0.0.1:5000/movies `

- Request Arguments: jwt_token
- Returns: 

```
{
  "movies": [
    {
      "id": 1,
      "release_date": "Mon, 01 Jan 2018 00:00:00 GMT",
      "title": "Moon Movie"
    },
    {
      "id": 2,
      "release_date": "Thu, 03 Sep 2015 00:00:00 GMT",
      "title": "Sun Movie"
    },
    {
      "id": 3,
      "release_date": "Fri, 07 Feb 2020 00:00:00 GMT",
      "title": "Star Movie"
    }
  ],
  "success": true
}

```


### POST '/actors'
add a new actor to the database: 
` curl http://127.0.0.1:5000/actors -X POST -H "Authorization: bearer jwt_token" -H "Content-Type: application/json" -d '{"name": "bayan", "age":"24", "gender":"female"}' `

- Request Arguments: jwt_token, name:string, age:int, gender:string
- Returns: 

```
{
  "actors": [
    {
      "age": 24,
      "gender": "female",
      "id": 1,
      "movie_id": null,
      "name": "bayan"
    }
  ],
  "success": true
}

```


### POST '/movies'
add a new movie to the database: 
` curl http://127.0.0.1:5000/movies -X POST -H "Authorization: bearer jwt_token" -H "Content-Type: application/json" -d '{"title": "Moon Movie title", "release_date":"2018-01-01"}' `


- Request Arguments: jwt_token, title:string, release_date:date
- Returns: 

```
{
  "movies": [
    {
      "id": 1,
      "release_date": "Mon, 01 Jan 2018 00:00:00 GMT",
      "title": "Moon Movie"
    }
  ],
  "success": true
}

```


### DELETE '/actors/<actor_id>'
delete an actor from the database using actor_id: 
` curl -X DELETE http://127.0.0.1:5000/actors/5 -H "Authorization: bearer jwt_token" `


- Request Arguments: jwt_token, actor_id:int
- Returns: 

```
{
  "delete": "5",
  "success": true
}

```


### DELETE '/movies/<movie_id>'
delete a movie from the database using movie_id: 
` curl -X DELETE http://127.0.0.1:5000/movies/4 -H "Authorization: bearer jwt_token" `

- Request Arguments: jwt_token, movie_id:int
- Returns: 

```
{
  "delete": "4",
  "success": true
}

```


### PATCH '/actors/<actor_id>'
edit some actor information using actor_id: 
` curl -X PATCH http://127.0.0.1:5000/actors/2 --data '{"movie_id": "3"}' -H "content-type: application/json" -H "Authorization: bearer jwt_token" `

- Request Arguments: jwt_token, actor_id:int, movie_id:int
- Returns: 

```
{
  "actors": [
    {
      "age": 33,
      "gender": "male",
      "id": 2,
      "movie_id": 3,
      "name": "ibrahim"
    }
  ],
  "success": true
}

```


### PATCH '/movies/<movie_id>'
edit some movie information using movie_id: 
` curl -X PATCH http://127.0.0.1:5000/movies/3 --data '{"title": "The STAR Movie"}' -H "content-type: application/json" -H "Authorization: bearer jwt_token" `


- Request Arguments: jwt_token, movie_id:int, title:string
- Returns: 

```
{
  "movies": [
    {
      "id": 3,
      "release_date": "Fri, 07 Feb 2020 00:00:00 GMT",
      "title": "The STAR Movie"
    }
  ],
  "success": true
}

```


## Testing
To run the tests, you need to create a new database called: capstone_test and restore it by running:
```
dropdb capstone_test
createdb capstone_test
psql capstone_test < capstone.psql

python test_app.py
```







