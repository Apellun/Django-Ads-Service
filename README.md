<i>Ридми на русском — ниже.</i>

# Django API for ads

<p><b>Technologies:</b> Django, Djoser, PostgresQL, SQLite.</p>

<p>This is a Django API for a service that allows users to create ads, view each other's ads and comment on them. The API is built with Django Rest Framework and Djoser with a custom user model.</p>

<p> <b>To launch:</b>
<br>1. Copy the repository to your computer
<br>2. You need to insert the following environment variables into the example.env file:
<li><b>SECRET_KEY</b> (any string, you can use the one in the example)
<li><b>DB_USER/DB_PASSWORD/DB_NAME/DATABASE_URL</b>
<br><i>You need those in case you want to run the app in production mode. Postgres host, engine, and port in the example.env are the default, you don't need to change them if you use the default settings.
If you don't want to run the API in production mode, change the DEBUG variable to True. The API will run in development mode and use an SQLite database.</i>
<li><b>EMAIL_HOST_USER/EMAIL_HOST_PASSWORD</b>
<br><i>The host/port in the example is the default host/port for the Gmail SMTP service, you don't need to change them if you use Gmail. You only need to enter your username and password for your SMTP server. If you don't know how to get them, ask Google.</i><br>
<br>3. Rename the example.env into .env
<br>3. In the terminal, from the project folder, run the following commands:<br>
  pip install -r requirements.txt<br>
  python3 skymarket/manage.py migrate<br>
  python3 skymarket/manage.py runserver<br>
  <br>

## Main viewpoints

The list of all API routes is going to be accessible at localhost:port/api/schema/swagger-ui (port is the port for the app you set up manually or the default port for the app).

<ins>api/ads/</ins>
<p><b>GET</b> — Returns a list of ads, 4 for each page. Anyone can view it. Also, anyone can search ads by title with the query parameter "title".<br>
<b>POST</b> - Creates a new ad, which requires the title and the price. Accessible for authenticated users only.</p>

<ins>api/ads/pk/</ins>
<p><b>GET</b> - Returns the detailed info on the ad. Anyone can view it.<br>
<b>PUT, PATCH</b> — Updates/partially updates the selected ad. Only the ad's owners and administrators can change ads.<br>
<b>DELETE</b> — Deletes the ad. Only the ad's owners and administrators can delete ads.</p>

<ins>api/comments/</ins>
<p><b>GET</b> - Returns a list of all users' comments. Accessible for authenticated users only.<br>
<b>POST</b> - Creates a comment, requires the text. Accessible for authenticated users only. Gets the id of the ad that is commented upon from the query parameter "ad".</p>

<ins>api/comments/pk/</u><br>
<p><b>GET</b> - Returns the detailed info on comment. Accessible for authenticated users only.<br>
<b>PUT, PATCH</b> — Updates/partially updates the selected comment. Only the comment's authors and administrators can change ads.<br>
<b>DELETE</b> — Deletes the comment. Only the comment's authors and administrators can delete comments.</p>

<ins>api/users/ and the authorization/authentication endpoints</u><br>

<p>All of the <ins>users/</ins> and authentication endpoints work exactly like they are described in Djoser documentation. More info on it here: <i>https://djoser.readthedocs.io/en/latest/base_endpoints.html</i></p>
<p>

## Challenges

### Djoser + custom user model and user manager

<p>For this project, I used Djoser for the first time. I used a custom User model and User manager provided by course tutors in order to implement it correctly.
It took some time to get the User manager to work properly. I had a constant issue with making a superuser through a ./manage.py command — the custom manager did not assign the admin role to the superuser. Eventually, what helped was separately specifying the roles for the each type of user and making some of the arguments optional in the functions for creating users.</p>

### Different permissions for different actions in a viewset

<p>In this project, I wrote multiple permissions for one viewset for the first time. It was not particularly hard, because there are multiple examples online. Nevertheless, it took me some time to understand how to implement them correctly.</p>

### Auto user id attachment

<p>At first, the "create" method for ads has been receiving value for the "author" field (a foreign key — the ad owner's user id) from the body of a query. At some point, I thought that it was weird to pass the id like that. I asked a senior developer and he confirmed, that it is a weird thing to do.
At first, I decided to replace the default "create" method of the viewset so it could get the author's id from the session details automatically. I couldn't find an example of a better way to do that. I wrote a lengthy hardcode and used the same solution in the "create" method for comments as well.
Some time later, I found a way to replace all that hardcode with one string in the serializer.</p>

### Password reset email confirmation

<p>Understanding how the Djoser reset_password endpoints and their methods work was not easy for me.
I found a tutorial for testing the password reset functionality here https://saasitive.com/tutorial/django-rest-framework-reset-password/, put the tests into the project (skymarket/tests.py) and adjusted the code so that the test passed. This helped me better understand the functionality. I kept the author's comments for the tests for future reference.
I'm still trying to understand how to create a proper view for the password reset confirmation.</p>

<i>Here starts the Readme in Russian.</i>

# API для размещения объявлений на Django

<p><b>Технологии:</b> Django, Djoser, PostgresQL, SQLite.</p>

<p>Это API на Django для сервиса, в котором пользователи могут создавать объявления и просматривать/комментировать объявления друг друга. Чтобы его построить, я использовала Django Rest Framework и Djoser с кастомной моделью пользователя.</p>

## Как запустить:
<br>1. Скопируйте репозиторий на компьютер
<br>2. В example.env внесите значения для переменных:
<li><b>SECRET_KEY</b> (можно использовать любую строку, даже ту, что уже указана в файле)
<li><b>DB_USER/DB_PASSWORD/DB_NAME/DATABASE_URL</b>
<br><i>Эти переменные нужно указать, если хотите запустить приложение в режиме production и использовать базу PostgreSQL. Переменные Postgres host, engine, port указаны дефолтные, их менять не нужно, если ваша база Postgres запущена с такими же дефолтными значениями.
Иначе, измените переменную DEBUG на True: приложение запустится в режиме разработки и использует базу SQLite.</i>
<li><b>EMAIL_HOST_USER/EMAIL_HOST_PASSWORD</b>
<br><i>Хост и порт в примере — дефолтные для Gmail SMTP, их менять не нужно, если вы исопльзуете Gmail. Нужно ввести только имя пользователя и пароль для вашего SMTP сервера. Если не знаете, откуда их взять, спросите Google.</i><br>
<br>3. Переименуйте example.env в .env
<br>3. Из папки проекта, в терминале, запустите следующие команды:
  <p></p>
  pip install -r requirements.txt<br>
  python3 skymarket/manage.py migrate<br>
  python3 skymarket/manage.py runserver<br>
  <p></p>

## Оновные адреса

Список всех адресов приложения и описание того, как их использовать, будет доступно по адресу localhost:port/api/schema/swagger-ui (port — заданный вами порт для приложения, либо порт приложения по умолчанию).

<ins>api/ads/</ins>
<p><b>GET</b> — Возвращает список объявлений, по 4 на страницу. Просматривать объявления могут все. Еще все могут искать объявления по вхождению текста в заголовок, через квери-параметр "title".<br>
<b>POST</b> - Создает новое объявление, нужно отправить название через поле "title" и цену через "price". Доступно только аутентифицированным мользователям.</p>

<ins>api/ads/pk/</ins>
<p><b>GET</b> - Возвращает детали объявления. Просматривать могут все.<br>
<b>PUT, PATCH</b> — Обновляет/частично обновляет объявление. Только хозяин объявления или администратор могут изменять объявления.<br>
<b>DELETE</b> — Удаляет объявление. Только хозяин объявления или администратор могут удалять объявления.</p>

<ins>api/comments/</ins>
<p><b>GET</b> - Возвращает список комментиариев пользователя. Доступно только аутентифицированным мользователям.<br>
<b>POST</b> - Создает комментарий, для этого нужно отправить текст в поле "text". Id объявления, к которому привязывается комментарий, берет из квери-параметра "ad". Доступно только аутентифицированным мользователям.</p>

<ins>api/comments/pk/</u><br>
<p><b>GET</b> - Возвращает детали комментария. Доступно только аутентифицированным пользователям.<br>
<b>PUT, PATCH</b> — Обновляет/частично обновляет комментарий. Только хозяин объявления или администратор могут изменять комментарии.<br>
<b>DELETE</b> — Удаляет комментарий. Только хозяин объявления или администратор могут удалять комментарии.</p>

<ins>api/users/ и адреса авторизации/аутентификации</u><br>

<p>Все адреса <ins>users/</ins>, а также адреса авторизации/аутентификации работают так, как описано в документации Djoser. Подробнее можно почитать здесь: <i>https://djoser.readthedocs.io/en/latest/base_endpoints.html</i></p>
<p>

## Трудности

### Djoser + кастомные модель и менеджер пользователя

<p>В этом проэкте я впервые исользовала Djoser. Я использовала кастомные модель и менеджер пользователя из подсказки по проекту на курсе, чтобы правильно использовать эту библиотеку в проекте.
Какое-то время ушло на то, чтобы поправить кастомный менеджер. У меня постоянно возникала проблема с тем, что при создании суперюзера через manage.py, ему не присваивалась роль администратора. Мне пришлось попробовать несколько вариантов это поправить. В итоге проблема решилась, когда я отдельно прописала задание ролей каждому типу пользователя, а также сделала опциональными некоторые аргументы функций создания пользователя.</p>

### Разные разрешения для разных действий во вьюсете

<p>Я писала несколько разных типов разрешений для одного вьюсета впервые. Не то, чтобы это было особо сложно, потому что в сети много примеров. Но какое-то время потребовалось, чтобы понять, как их правильно встроить в проект.</p>

### Автоматическая привязка id пользователя

<p>Изначально метод создания объявлений принимал значение для поля "автор" (внешний ключ — id пользователя-хозяина) из тела запроса. Я подумала, что странно передавать id таким образом. Спросила у коллеги-сениора и он подтвердил, что это странно.
Я решила переписать метод "create" вьюсета, чтобы он автоматически получал id автора из деталей сессии, потому что лучшего решения в интернете найти не получилось. У меня получился длинный хардкод, который я потом использовала еще и для комментариев.
Спустя какое-то время, я нашла замену всему этому хардкоду одной строчкой через сериализаторы.</p>

### Подвтерждение смены пароля по электронной почте

<p>Разобраться, как работают адреса Djoser reset_password и их методы было непросто.
Я нашла туториал для проверки этой функциональности здесь, https://saasitive.com/tutorial/django-rest-framework-reset-password/, добавила тесты в проект (skymarket/tests.py) и поправила код так, что тесты проходили без ощибок. Комментарии автора туториала в тестах я оставила себе на будущее.
Я все еще разбираюсь, как правильно создать вью для проверки пароля — это задача в процессе.</p>
