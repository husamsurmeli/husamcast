# husamcast
App resides on the link:
https://husamcast.herokuapp.com/
Frontend completly operates, please login with below credentials to use it:
You only see relevant permissions to your roles as a frontend menu.
Casting assistant
        name:ca@ca.com     pass:Aa123456
Casting director
        name:cd@cd.com     pass:Aa123456
Execcutive producer
        name:ca@ca.com     pass:Aa123456
        
While Frontend showcases the use of authentication with id_tokens,
apiandtesting provides unittest with RBAC background. showcases authorization with access_tokens,
while testing the api locally user only needs to download that folder (apiandtesting).
or should 'src' to that folder (if all repo downloaded). apiandtesting folder also have its Readme, please refer to it.
Reviewers may notice that app endpoints and api endpoints operate identical functions (so tests are healthy), but while one renders template (for frontend), other jsonifys (for testing.

Roles And permissions
        Casting Assistant
                Can view actors and movies
        Casting Director
                All permissions a Casting Assistant has and…
                Add or delete an actor from the database
                Modify actors or movies
        Executive Producer
                All permissions a Casting Director has and…
                Add or delete a movie from the database
                
                

  
