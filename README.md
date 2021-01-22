# husamcast
## How to use the app?
App resides on the link: <br>
https://husamcast.herokuapp.com/
Frontend completly operates, please login with below credentials to use it:<br>
Thanks to `jinja` you can only see relevant permissions according to your roles on the menu.<br>

### Login Credentials<br>
        Casting Assistant
                - name:ca@ca.com
                - pass:Aa123456
        Casting Director
                - name:cd@cd.com
                - pass:Aa123456
        Execcutive Producer
                - name:ep@ep.com
                - pass:Aa123456
        
 
### Authentication and Authorization
While Frontend showcases the use of authentication with id_tokens,<br>
apiandtesting provides unittest with RBAC background. showcases authorization with access_tokens,<br>

### How to test
while testing the api locally user only needs to download that folder `apiandtesting`.<br>
or should `src` to that folder (if all repo downloaded). apiandtesting folder also have its `Readme`, please refer to it.<br>
Reviewers may notice that app endpoints and api endpoints operate identical functions (so tests are healthy), but while one renders template (for frontend), other jsonifys (for testing).<br><br>

### Roles And permissions<br>
        Casting Assistant
                - Can view actors and movies
        Casting Director
                - All permissions a Casting Assistant has and…
                - Add or delete an actor from the database
                - Modify actors or movies
        Executive Producer
                - All permissions a Casting Director has and…
                - Add or delete a movie from the database
                
### Application Endpoints

| First Header  | Second Header |
| ------------- | ------------- |
| Content Cell  | Content Cell  |
| Content Cell  | Content Cell  |
                

  
