# App
# is 
# not
# live
# furthermore




## How to use the app?
App resides on the link: <br>
https://husamcast.herokuapp.com/ <br>
Frontend completly operates, please login with below credentials to use it:<br>
Thanks to `jinja`  and `Auth0 Python` implentation you can only see relevant permissions according to your roles on the menu.<br>

### Env tech stacks
Latest versions of Python and PostgreSQL <br>
And for dependincies please pip the requirements.txt <br>
`pip install -r requirements.txt`

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
`apiandtesting` provides unittest with RBAC background. showcases authorization with access_tokens,<br>

### How to test
while testing the api locally user only needs to download that folder `apiandtesting`.<br>
or should `cd` to that folder (if all repo downloaded). apiandtesting folder also have its `Readme`, please refer to it.<br>
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
                


<h2>Application Endpoints</h2>
<h4>Some endpoints haven't covered here for security. (login, callback etc.)</h4>
<table>
    <tr>
      <th>route</th>
      <th>requires</th>
      <th>returns</th>
    </tr>
          <tr>
     <td>casting</td>
      <td>none</td>
      <td>renders a template of RBAC menu</td>
    </tr>
          <tr>
     <td>actors</td>
      <td>none</td>
      <td>renders a template of all artists query</td>
    </tr>
          <tr>
     <td>actors/delete/</td>
      <td>integer</td>
      <td>executes db.delete returns to actors route</td>
    </tr>
          <tr>
     <td>actors/edit/</td>
      <td>integer and form data</td>
      <td>executes db.update returns to actors route</td>
    </tr>
          <tr>
     <td>movies/edit/</td>
      <td>integer and form data</td>
      <td>executes db.update returns to movies route</td>
    </tr>
          <tr>
     <td>movies/delete/</td>
      <td>integer</td>
      <td>executes db.delete returns to movies route</td>
    </tr>
          <tr>
     <td>movies</td>
      <td>none</td>
      <td>renders a template of all movies query</td>
    </tr>
    <tr>
     <td>actors/create</td>
      <td>form data</td>
      <td>executes db.add returns to actors route</td>
    </tr>
    <tr>
        <td>movies/create</td>
         <td>form data</td>
         <td>executes db.delete returns to movies route</td>
       </tr>
  </table>
