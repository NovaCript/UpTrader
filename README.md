<h1 align="center">Hi there, I'm <a href="https://gitlab.com/frutez/" target="_blank">Gleb</a>
<img src="https://github.com/blackcater/blackcater/raw/main/images/Hi.gif" height="32"/></h1>
<h3 align="center">Template for a menu tree, with an example.</h3>

[![Typing SVG](https://readme-typing-svg.herokuapp.com?color=%2336BCF7&lines=\(\(\(\(\(:++^_^++:\)\)\)\)\))](https://git.io/typing-svg)

><h5> Stack:</h5>Django
<br>

<img width="116" alt="Снимок экрана 2024-02-15 191807" src="https://github.com/NovaCript/UpTrader/assets/114811823/da464410-c06f-49c8-beae-9608d5a64a36">


Зависимости можно установить при помощи pip
 >pip install -r requirements.txt
<br>

Либо poerty.
  >poetry install
<br>

Проводим миграции, создаем суперпользователя, запускаем сервер.
>python manage.py migrate<br>
>python manage.py createsuperuser<br>
>python manage.py runserver<br>
<br>
В меню создаем родителя который будет вызываться при помощи включения в файл нашей страницы<br>
(не забудте загрузить {% load menu_tags %} на страничке.) {% draw_menu 'main_menu' %}<br>

Если нет ни одного созданного меню, вернется пустая строка.
<br>
Для демонстрации было написано представление. <br>
<img width="213" alt="Снимок экрана 2024-02-15 191351" src="https://github.com/NovaCript/UpTrader/assets/114811823/3daba4d9-edfc-4a4f-a970-a3e4ac56f061">
<br>
Без наведения, содержимое скрыто.<br>
<img width="532" alt="Снимок экрана 2024-02-15 191511" src="https://github.com/NovaCript/UpTrader/assets/114811823/51faa4b2-0ca6-49d2-9c51-2b6056877a01">
<br>
При наведении список раскрываемся.<br>
<img width="539" alt="Снимок экрана 2024-02-15 191517" src="https://github.com/NovaCript/UpTrader/assets/114811823/a44192e2-1bd5-4d6c-bbbc-2f26ef745ab3">
<br>
