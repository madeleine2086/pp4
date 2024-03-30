<h1 id="top">BeWell - Testing</h1>

Back to the [README](README.md)

* [PEP8](http://pep8online.com/)<br>
   PEP8 was used to validate all the Python code:
   - bugs detected in some files (models.py)
   <img src="documentation/images/tests/models-py-minor-issues.png">

   - bugs then were fixed (models.py)
   <img src="documentation/images/tests/models-py-bugs-fixed.png">

   * All files in about, my_project and bewell_blog apps came back clear 
   except settings.py where's 1 line too long. It's in AUTH_PASSWORD_VALIDATORS and cannot be shortend.
   <img src="documentation/images/tests/issue-in-settings-py.png">
* [W3C - HTML](https://validator.w3.org/)<br>
   W3C- HTML was used to validate all the HTML code
   
* [W3C - CSS](https://jigsaw.w3.org/css-validator/)<br>
   W3C - CSS was used to validate the CSS code
   <img src="documentation/images/tests/W3c-validation-test.png">


   <h2 id="frontend">Frontend</h2>

<a href="#top">Back to the top</a>

* All the internal links are working and bring the user to the right page on the website.
* All the external links are working and bring the user to the right social media page by 
  opening a new browser tab.
* The pagination system is working, it adds another page when there's more than 6 posts on the page.
* The drop-down menu in the navbar shows a list of posts categories on every page of the website
<img src="documentation/images/navbar-desktop-notloggedin.png">


* The Login and Logout system is working correctly. It shows the right interactive message to the users on Login and Logout.


## Login

![Login Success](documentation/images/messages/sign-in-msg.png)


## Logout


![Logout Success](documentation/images/messages/sign-out-msg.png)

## CRUD
   * Full CRUD functionality is present. Users can view (Read) posts on the page, and once registered and logged in they can comment on a post (Create), update their posts (Update) and delete their posts (Delete) if they wish.


