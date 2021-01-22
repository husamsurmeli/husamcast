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
                

  <style>
table {
  font-family: arial, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

td, th {
  border: 1px solid #dddddd;
  text-align: left;
  padding: 8px;
}

tr:nth-child(even) {
  background-color: #dddddd;
}
</style>
</head>
<body>

<h2>HTML Table</h2>

<table>
  <tr>
    <th>Company</th>
    <th>Contact</th>
    <th>Country</th>
  </tr>
  <tr>
    <td>Alfreds Futterkiste</td>
    <td>Maria Anders</td>
    <td>Germany</td>
  </tr>
  <tr>
    <td>Centro comercial Moctezuma</td>
    <td>Francisco Chang</td>
    <td>Mexico</td>
  </tr>
  <tr>
    <td>Ernst Handel</td>
    <td>Roland Mendel</td>
    <td>Austria</td>
  </tr>
  <tr>
    <td>Island Trading</td>
    <td>Helen Bennett</td>
    <td>UK</td>
  </tr>
  <tr>
    <td>Laughing Bacchus Winecellars</td>
    <td>Yoshi Tannamuri</td>
    <td>Canada</td>
  </tr>
  <tr>
    <td>Magazzini Alimentari Riuniti</td>
    <td>Giovanni Rovelli</td>
    <td>Italy</td>
  </tr>
</table>
