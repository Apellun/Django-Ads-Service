# Django course project

<p>This is a Django api that provides a platform for users to create ads, comment on each other ads, and edit and delete the ads they have created. Users can also search ads by title. The app is built with Django Rest Framework and Djoser library with a custom user model.</p>

## Main viewpoints

<ins>api/ads/</ins>
<p><b>GET</b> — Displays a list of ads, 4 for each page. Everyone can view it. Everyone also can search ads by title with the query parameter "title".<br>
<b>POST</b> - Creates a new ad, which requires the title and the price. Accessible for authorized users only.</p>

<ins>api/ads/pk/</ins>
<p><b>GET</b> - Displays detailed info on the ad. Everyone can view it.<br>
<b>PUT, PATCH</b> — Updates and partially updates info on the selected ad. Only the ad's owners and admin users can change ads.<br>
<b>DELETE</b> — Deletes the selected ad. Only the ad's owners and admin users can delete ads.</p>

<ins>api/comments/</ins>
<p><b>GET</b> - Displays a list of all users' comments. Accessible for authorized users only.<br>
<b>POST</b> - Creates a comment, for that requires the text. Accessible for authorized users only. Gets the ad's that is commented upon id from the query parameter "ad".</p>

<ins>api/comments/pk/</u><br>
<p><b>GET</b> - Displays detailed info on comment. Accessible for authorized users only.<br>
<b>PUT, PATCH</b> — Updates and partially updates info on the selected comment. Only the comment's authors and admin users can change ads.<br>
<b>DELETE</b> — Deletes the selected comment. Only the comment's authors and admin users can delete comments.</p>

<ins>api/users/ and authentication endpoints</u><br>

<p>All of the main <ins>users/</u> and authentication endpoints work exactly like they are described in Djoser documentation. More info on it here: <i>https://djoser.readthedocs.io/en/latest/base_endpoints.html</i></p>

## Challenges

### Djoser + custom user model and user manager

<p>For this project I used Djoser for the first time. I've read the documentation to implement it and used an example os custom User model and User manager to implement it correctly. Althogh the example of the User manager was provided by the course tutors, it still took some time to get it to work properly. I had the constant issue of it making a superuser through a ./manage.py command, but assign it a common user role, and then I got it to create superusers properly, it created common users with an admin role. I figured out the solution by now, but I still feel that I do not understand the User manager function in depth, information on the subject seems to be a bit scarce.</p>

### Different permissions for different actions of a viewset

<p>I also wrote multiple permissions for one viewset for the first time. It was not particularly hard, because I was able to find a solution online. Nevertheless, I took some time to figure out how to incorporate it into the project for everything to work correctly.</p>

### Auto user id attach

<p>At first, the ad "create" action recieved value for the author field (a foreign key — owner user id) from the body of a query, like the title and the price of the ad. At some point I thought that it is weird to pass the id like that. I asked a senior colleague and he confirmed, that it is a weird thing to do, indeed. So I decided to rewrite the create method of a viewset for it to gain the author's id not through the body, but from the session details, automatically. I replaced a comments' create method as well, with some extra logic to also get the ad's id from a query parameter so that the comment would be tied to an ad also automatically. It's hardcode in a lot of ways, but I couldn't find a reference for a better way to do that.</p>

### Password reset email confirmation

<p>For this part, adding Djoser settings to settings.py was easy, understanding how they work was hard. I found a tutorial for testing this functionality here <i>https://saasitive.com/tutorial/django-rest-framework-reset-password/</i>, put it into my project and adjusted it, so it would pass without mistakes. This way, I understood how the insides of Django + Djoser do the work and also became sure that I set everything correctly. Since it is not my code, an it helped me to understand the process, I kept author's comments for future reference.</p>
