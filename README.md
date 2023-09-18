<i>Ридми на русском — ниже.</i>

# Django ad api

<p><b>Technologies:</b> Django, Djoser, PostgresQL, SQLite.</p>

<p>This is a Django api that provides a platform for users to create ads, comment on each other ads, and edit and delete the ads they have created. Users can also search ads by title. The app is built with Django Rest Framework and Djoser library with a custom user model.</p>

<p> <b>To launch:</b>
<br>1. Copy the repository to your computer
<br>2. You need to insert the following environment variables into the example.env file:
<li><b>SECRET_KEY</b> (any string, you can use the one in the example)
<li><b>DB_USER/DB_PASSWORD/DB_NAME/DATABASE_URL</b>
<br><i>You need those in case you want to run the app in production mode. Or chnage the DEBUG variable to True, so that the app runs in the development mode and uses an SQLite database.
Postgres host, engine, and port in the example.env are the default, you don't need to change them if you use the default settings.</i>
<li><b>EMAIL_HOST_USER/EMAIL_HOST_PASSWORD</b>
<br><i>The host/port in the example is the default host/port for the Gmail SMTP service, you don't need to change them if you decide to go with Gmail. You only need to enter your username and password for your SMTP server. If you don't know how to get them, ask Google.</i><br>
<br>3. Rename the example.env into .env
<br>3. Run the following commands in the terminal from the project folder:
  <p></p>
  pip install -r requirements.txt<br>
  python3 skymarket/manage.py migrate<br>
  python3 skymarket/manage.py runserver<br>
  <p></p>
The list of all routes and their possible usage is going to be accessible at localhost:port/api/schema/swagger-ui (port — the port for the app you set up manually or the default port for the app).

## Main viewpoints

<ins>api/ads/</ins>
<p><b>GET</b> — Returns a list of ads, 4 for each page. Everyone can view it. Everyone also can search ads by title with the query parameter "title".<br>
<b>POST</b> - Creates a new ad, which requires the title and the price (the "title" and the "price" fields). Accessible for authenticated users only.</p>

<ins>api/ads/pk/</ins>
<p><b>GET</b> - Returns the detailed info on the ad. Everyone can view it.<br>
<b>PUT, PATCH</b> — Updates/partially updates info on the selected ad. Only the ad's owners and admin users can change ads.<br>
<b>DELETE</b> — Deletes the selected ad. Only the ad's owners and admin users can delete ads.</p>

<ins>api/comments/</ins>
<p><b>GET</b> - Returns a list of all users' comments. Accessible for authenticated users only.<br>
<b>POST</b> - Creates a comment, for that requires the text (the "text" field). Accessible for authenticated users only. Gets the id of the ad that is commented upon from the query parameter "ad".</p>

<ins>api/comments/pk/</u><br>
<p><b>GET</b> - Returns the detailed info on comment. Accessible for authenticated users only.<br>
<b>PUT, PATCH</b> — Updates/partially updates the info on the selected comment. Only the comment's authors and admin users can change ads.<br>
<b>DELETE</b> — Deletes the selected comment. Only the comment's authors and admin users can delete comments.</p>

<ins>api/users/ and the authorization/authentication endpoints</u><br>

<p>All of the main <ins>users/</ins> and authentication endpoints work exactly like they are described in Djoser documentation. More info on it here: <i>https://djoser.readthedocs.io/en/latest/base_endpoints.html</i></p>
<p>

##Challenges

### Djoser + custom user model and user manager

<p>For this project, I used Djoser for the first time. I've read the documentation and used a custom User model and User manager provided by course tutors in order to implement it correctly.
But it took some time to get the User manager to work properly. I had the constant issue with making a superuser through a ./manage.py command — the custom manager did not assign the admin role to the superuser. I had to try some of the fixes and leave it with separately specified roles for the each type of the user.</p>

### Different permissions for different actions in a viewset

<p>I wrote multiple permissions for one viewset for the first time. It was not particularly hard, because I was able to find a solution online. Nevertheless, it took me some time to understand how to adjust it to the project correctly.</p>

### Auto user id attach

<p>At first, the ads' endpoint "create" method has been receiving value for the author field (a foreign key — the ad owner's user id) from the body of a query, like the title and the price of the ad. At some point, I thought that it is weird to pass the id like that. I asked a senior developer and he confirmed, that it is a weird thing to do indeed.
I decided to replace the default "create" method of the viewset so it could get the author's id not from the request body, but from the session details, automatically. My solution for that was a lengthy hardcode, since I couldn't find a reference for a better way to do that. I used that solution in the comments' endpoint "create" method as well.
After having done all that, after some time, I found a solution to replace all that hardcode with one string using the serializer.</p>

### Password reset email confirmation

<p>For this functionality, adjusting the settings.py was easy, but understanding how the Djoser reset_password endpoints and their methods work was not.
I found a tutorial for testing this functionality here https://saasitive.com/tutorial/django-rest-framework-reset-password/, put the tests into my project (skymarket/tests.py) and adjusted the code so that the test passes without mistakes. It helped me understand the functionality and become sure that I set everything correctly.
I kept the author's comments for future reference.
I'm also still in the process of trying to understand how to create a proper view for the password reset confirmation, it remains a work in progress.</p>

<i>Here starts the Readme in Russian.</i>

# Приложение для размещения объявлений на Django

<p><b>Технологии:</b> Django, Djoser, PostgresQL, SQLite.</p>

<p>Это приложение на Django, которое позволяет пользователям создавать объявления, комментировать объявления друг друга, а также редактировать и удалять свои объявления. Приложение построено с помощью Django Rest Framework и библиотеки Djoser, с кастомной моделью пользователя.</p>

## Как запустить:
<br>1. Скопируйте репозиторий на компьютер
<br>2. В example.env нужно внести значения для переменных:
<li><b>SECRET_KEY</b> (можно использовать любую строку, даже ту, что уже указана в самом файле)
<li><b>DB_USER/DB_PASSWORD/DB_NAME/DATABASE_URL</b>
<br><i>Эти переменные нужно указать, если хотите запустить приложение в режиме production. Иначе, измените переменную DEBUG на True, чтобы приложение запустилось в режиме разработки и использовало базу SQLite.
В example.env еременные Postgres host, engine, port указаны дефолтные, их менять не нужно, если база Postgres запущена с такими же дефолтными значениями.</i>
<li><b>EMAIL_HOST_USER/EMAIL_HOST_PASSWORD</b>
<br><i>Хост и порт в примере — дефолтные для Gmail SMTP, их менять не нужно, если вы исопльзуете Gmail. Нужно ввести только имя пользователя и пароль для вашего SMTP сервера. Если не знаете, откуда их взять, спросите Google.</i><br>
<br>3. Переименуйте example.env в .env
<br>3. Из папки проекта, в терминале, запустите следующие команды:
  <p></p>
  pip install -r requirements.txt<br>
  python3 skymarket/manage.py migrate<br>
  python3 skymarket/manage.py runserver<br>
  <p></p>
Список всех адресов приложения и описание того, как их использовать, будет доступно по адресу localhost:port/api/schema/swagger-ui (port — заданный вами порт для приложения, либо порт приложения по умолчанию).

## Оновные адреса

<ins>api/ads/</ins>
<p><b>GET</b> — Возвращает список объявлений, по 4 на страницу. Просматривать объявления могут все. Еще все могут искать объявления по вхождению запроса в заголовок, через квери-параметр "title".<br>
<b>POST</b> - Создает новое объявление, нужно отправить название через поля "title" и цену через "price". Доступно только аутентифицированным мользователям.</p>

<ins>api/ads/pk/</ins>
<p><b>GET</b> - Возвращает детали объявления. Просматривать могут все.<br>
<b>PUT, PATCH</b> — Обновляет/частично обновляет значения полей для выбранного объявления. Только хозяин объявления или администратор могут изменять объявления.<br>
<b>DELETE</b> — Удаляет объявление. Только хозяин объявления или администратор могут удалять объявления.</p>

<ins>api/comments/</ins>
<p><b>GET</b> - Возвращает список комментиариев пользователя. Доступно только аутентифицированным мользователям.<br>
<b>POST</b> - Создает комментарий, для этого нужно отправить текст в поле "text". Id объявления, к которому привязывается комментарий, берет из квери-параметра "ad". Доступно только аутентифицированным мользователям.</p>

<ins>api/comments/pk/</u><br>
<p><b>GET</b> - Возвращает детали комментарий. Доступно только аутентифицированным мользователям.<br>
<b>PUT, PATCH</b> — Обновляет/частично обновляет значения полей для выбранного комментария. Только хозяин объявления или администратор могут изменять комментарии.<br>
<b>DELETE</b> — Удаляет комментарий. Только хозяин объявления или администратор могут удалять комментарии.</p>

<ins>api/users/ и адреса авторизации/аутентификации</u><br>

<p>Все основные адреса <ins>users/</ins>, а также адреса авторизации/аутентификации работают точно так же, как указано в документации Djoser. Подробнее можно почитать здесь: <i>https://djoser.readthedocs.io/en/latest/base_endpoints.html</i></p>
<p>

## Трудности

### Djoser + кастомные модель и менеджер пользователя

<p>В этом проэкте я впервые исользовала Djoser. Я прочитала документацию и использовала кастомные модель и менеджер пользователя, которые бяли предложены на курсе, чтобы правильно использовать инструменты Djoser в проекте.
Какое-то время ушло на то, чтобы поправить кастомный менеджер. У меня постоянно возникала проблема с тем, что при создании суперюзера через manage.py, ему не присваивалась роль администратора. Мне пришлось попробовать несколько вариантов это поправить, и в итоге отдельно прописать задание ролей каждому типу пользователя.</p>

### Разные разрешения для разных действий во вьюсете

<p>Я писала несколько разных типов разрешений для одного вьюсета впервые. Не то, чтобы это было особо сложно, потому что я смогла найти примеры в сети. Но какое-то время потребовалось, чтобы понять, как их правильно встроить в проект.</p>

### Автоматическая привязка id пользователя

<p>Изначально, метод создания объявлений принимал значение для поля "автор" (внешний ключ — id пользователя-хозяина) из тела запроса, так же как и заголовок объявления с ценой продажи. Я подумала, что странно передавать id таким образом. Спросила у коллеги-сениора и он подтвердил, что это странно.
Я решила переписать метод "create" вьюсета, чтобы он получал id автора не из тела запроса, а из деталей сессии, автоматически. У меня получился длинный хардкод, потому что лучшего решения в интернете найти не получилось. Для создания комментариев я использовала то же решение.
После, через какое-то время, я нашла замену всему этому хардкоду — это делалось одной строчкой через сериализаторы.</p>

### Подвтерждение смены пароля по электронной почте

<p>Настроить settings.py для этой функциональности было просто, но разобраться, как работают адреса Djoser reset_password и их методы — не очень.
Я нашла туториал для проверки этой функциональности здесь, https://saasitive.com/tutorial/django-rest-framework-reset-password/, добавила тест в проект (skymarket/tests.py) и поправила код так, что тест проходит без ощибок.
Я оставила комментарии автора туториала на будущее.
Еще я до сих пор в процессе попытки понять как правильно создать вью для проверки пароля во время его смены, это остается задачей в процессе.</p>